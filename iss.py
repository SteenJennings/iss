#! /usr/bin/python

import urllib
import json

'''
Retrieves and prints information on various spatial and other relevant parameters for the ISS
'''

baseurl = 'https://api.wheretheiss.at/v1/satellites/'

def retrieve_satellites():
    url = baseurl
    satellites_l = json.load(urllib.urlopen(url))
    return satellites_l

def retrieve_satellite_info(id):
    url = baseurl + str(id)
    satellite_info = json.load(urllib.urlopen(url))
    return satellite_info

def print_all_satellites(satellites_l):
    print len(satellites_l), ' satellite(s) found:'
    for satellite in satellites_l:
        print ' Satellite name: ', satellite['name'].upper(), ' , with ID: ', satellite['id']
        print '*' * 50
        
def print_satellite_info(satellite_info):
    print 'Satellite information for ', satellite_info['name'].upper()
    for key in sorted(satellite_info.keys()):
        print ' ', key, ' : ', satellite_info[key]

if __name__ == '__main__':
    satellites_l = retrieve_satellites()
    print_all_satellites(satellites_l)
    for satellite in satellites_l:
        print_satellite_info(retrieve_satellite_info(satellite['id']))
