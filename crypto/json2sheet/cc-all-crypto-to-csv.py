#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 00:18:59 2018

@author: brettwang
"""

import json
import csv
from urllib.request import Request, urlopen
url = 'https://ghost.computer/cx/cc-all-crypto.json'
req = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
f = urlopen(req)
datastore = json.load(f)
f.close()
 
while type(datastore) is dict:
# check main dict             
    maxlen = 0
    for key in datastore.keys():
        if type(datastore[key]) is int:
            dictlen = 1
        else:
            dictlen = len(datastore[key])
        if dictlen >= maxlen:
            maxlen = dictlen
            data = datastore[key]
                   
    # check if the main dict has any subdict.
    datastore = data
    if len(datastore.keys())>20:
        break


with open('cc-all-crypto.csv', 'w') as csvfile:
    fieldnames = list(datastore[list(datastore.keys())[0]].keys())
    mywriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    mywriter.writeheader() #write field name for first row
    for i in range(0, len(datastore)):
        mywriter.writerow(datastore[list(datastore.keys())[i]])
        
        
        
        
