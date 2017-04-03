"""
Simulator for getting temperature readings based on temperature_simulator.json config file 
OpenWeatherMap APIs 
"""

import urllib2
import json
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
    
    print k2c(parsed_json['main']['temp'])
    
    url_data.close()
    

def start(file_name):
    get_json_config(file_name)
    get_temperature_data()
    
start('temperature_simulator.json')
