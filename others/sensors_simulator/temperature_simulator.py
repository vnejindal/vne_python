"""
Simulator for getting temperature readings based on temperature_simulator.json config file 
OpenWeatherMap APIs 
Includes a temperature units convertor as well
"""

import urllib2
import json
from array import array
from config import log_json_config

json_config = {}

def c2f(t):
    return (t*9/5.0)+32

def c2k(t):
    return t+273.15

def f2c(t):
    return (t-32)*5.0/9

def f2k(t):
    return (t+459.67)*5.0/9

def k2c(t):
    return t-273.15

def k2f(t):
    return (t*9/5.0)-459.67


index_dict = {'kelvin':0, 'celcius': 1, 'fahrenheit': 2}
marray = [[s2s, k2c, k2f], [c2k, s2s, c2f], [f2k, f2c, s2s]]

def convert_unit(reading, funit, tunit):
    """
    Converts 'reading' from 'funit' to 'tunit'
      funit, tunit: kelvin, celcius, fahrenheit (all in lowercase) 
    
                 kelvin   celcius    fahrenheit 
      kelvin       s2s      k2c         k2f 
      celcius      c2k      s2s         c2f
      fahrenheit   f2k      f2c         s2s
    """
    global index_dict
    global marray
    return marray[index_dict[funit]][index_dict[tunit]](reading)



def read_json_file(file_name):
    json_config = open(file_name).read()
    file_json = json.loads(json_config)
    #print file_json
    return file_json

def get_json_config(file_name):
    global json_config
    json_config = read_json_file(file_name)
    
    
def get_temperature_data():
    location = json_config['location_zip'] + '.json'
    url = json_config['url'] + \
                      '?zip=' + \
                      json_config['location_zip'] + \
                      ',' + \
                      json_config['country_code'] + \
                      '&appid=' + \
                      json_config['apikey'] \
                      
    url_data = urllib2.urlopen(url)
    json_string = url_data.read()
    parsed_json = json.loads(json_string)
    
	print convert_unit(parsed_json['main']['temp'], 'kelvin', 'celcius')
    
    url_data.close()
    

def start(file_name):
    get_json_config(file_name)
    get_temperature_data()
    
start('temperature_simulator.json')
