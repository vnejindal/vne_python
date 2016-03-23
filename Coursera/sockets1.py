#!/usr/bin/python

import socket
import re

def process_data(data):
    d = data.lstrip()
    d1 = d.split('\r\n')
    for item in d1: 
        if(item.startswith("Content-Length:")):
            ln = item.split(':')
            print ln[1]
        if(item.startswith("Last-Modified:")):
            ln = item.split(':')
            print ln[1]        
   
    print d1 
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

fdata = ""
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    fdata += data
    
process_data(fdata)

mysock.close()