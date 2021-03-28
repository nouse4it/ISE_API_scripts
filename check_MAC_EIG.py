#!/usr/bin/python

"""
Category: ISE ERS API Script
Author: nouse4it <github@schlueter-online.net>

check_MAC_in_Group_ISE_API.py
Illustrate the following conecepts:
- Check if given MAC-Address is in given Endpoint Group on ISE
- Scripts intended for Users without Admin User on ISE
"""

__author__ = "nouse4it"
__author_email__ = "github@schlueter-online.net"
__copyright__ = "Copyright (c) 2020 nouse4it"

# Importing all needed Modules
import urllib3
import requests
import json
import pprint

urllib3.disable_warnings()

ise_ip = input('Enter IP Address of ISE: ')
api_user = input('Enter API Username: ')
api_pw = input ('Enter API Password: ')

#------------------------------------------------------------------------------
def get_groupid(groupname):
    url = 'https://{}:9060/ers/config/endpointgroup?filter=name.EQ.{}'.format(ise_ip,groupname)
    headers = {'ACCEPT': 'application/json'}
    req = requests.get(url, headers=headers, auth=(api_user, api_pw), verify=False)
    myjson = req.text
    parsed_json = (json.loads(myjson))
    groupid = parsed_json['SearchResult']['resources'][0]['id'] # get EIG Group ID for next request
    return groupid
#------------------------------------------------------------------------------
def get_endpoints_in_group(groupid):
    url = 'https://{}:9060/ers/config/endpoint?filter=groupId.EQ.{}'.format(ise_ip,groupid)
    headers = {'ACCEPT': 'application/json'}
    req = requests.get(url, headers=headers, auth=(api_user, api_pw), verify=False)
    total = (json.loads(req.text))
    items = total['SearchResult']['total']
    page = items / 100
    pages = round(page)
    endpoints = []
    for i in range(1,pages+1):
        url_page = 'https://{}:9060/ers/config/endpoint?filter=groupId.EQ.{}&size=100&page={}'.format(ise_ip,groupid,i)
        req_page = requests.get(url_page, headers=headers, auth=(api_user, api_pw), verify=False)
        myjson = req_page.text
        parsed_json = (json.loads(myjson))
        for mac in parsed_json['SearchResult']['resources']:
            endpoints.append(mac['name'])
    return endpoints
#------------------------------------------------------------------------------
def search_for_endpoint(name,endpointlist):
    if (name in endpointlist):
        print('MAC in Group')
    else:
        print('MAC not in Group')

#==============================================================================
# ---- Main: Run Commands
#==============================================================================

groupname = input('Enter EIG Name you want to search in: ')
keyVal = input('Enter MAC Address you want to search for: ')

groupid = get_groupid(groupname)
allendpoints = get_endpoints_in_group(groupid)

search_for_endpoint(keyVal,allendpoints)
