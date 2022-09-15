#!/usr/bin/python

"""
Category: API Script
Author: nouse4it <github@schlueter-online.net>

get_guest_user_ISE_API.py
Illustrate the following conecepts:
- Get detailled informations about active guest users
"""

__author__ = "nouse4it"
__author_email__ = "github@schlueter-online.net"
__copyright__ = "Copyright (c) 2022 nouse4it"

# Importing all needed Modules
import json
import csv
import pprint
import requests
import urllib3
import sys
import getpass

requests.packages.urllib3.disable_warnings()

ise_ip = input('Enter IP Address of ISE: ')
api_user = input('Enter API Username: ')
api_pw = getpass.getpass(prompt='Enter API Password: ')

# ------------------------------------------------------------------------------


def get_devices():
    url = 'https://{}:9060/ers/config/networkdevice/'.format(ise_ip)
    headers = {'ACCEPT': 'application/json',
               'content-type': 'application/json'}
    req = requests.get(url, headers=headers, auth=(
        api_user, api_pw), verify=False)
    total = (json.loads(req.text))
    items = total['SearchResult']['total']
    page = items / 100
    pages = round(page)
    devices = []
    with open('export_ise.csv', 'w') as f:
        writer = csv.writer(f)
        for i in range(1, pages+1):
            url_page = 'https://{}:9060/ers/config/networkdevice?size=100&page={}'.format(
                ise_ip, i)
            req_page = requests.get(url_page, headers=headers, auth=(
                api_user, api_pw), verify=False)
            myjson = req_page.text
            parsed_json = (json.loads(myjson))
            for device in parsed_json['SearchResult']['resources']:
                devices.append(device['id'])
        for id in devices:
            url_page = 'https://{}:9060/ers/config/networkdevice/{}'.format(
                ise_ip, id)
            req_page = requests.get(url_page, headers=headers, auth=(
                api_user, api_pw), verify=False)
            myjson = req_page.text
            parsed_json = (json.loads(myjson))
            name = parsed_json['NetworkDevice']['name']
            ip = (parsed_json['NetworkDevice']
                  ['NetworkDeviceIPList'][0]['ipaddress'])
            row = [name, ip]
            writer.writerow(row)

# ==============================================================================
# ---- Main: Get Devices
# ==============================================================================


get_devices()
