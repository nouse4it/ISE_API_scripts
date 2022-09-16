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


def get_user():
    url = 'https://{}:9060/ers/config/guestuser/'.format(ise_ip)
    headers = {'ACCEPT': 'application/json',
               'content-type': 'application/json'}
    req = requests.get(url, headers=headers, auth=(
        api_user, api_pw), verify=False)
    myjson = req.text
    parsed_json = (json.loads(myjson))
    users = []
    with open('export_guestuser_ise.csv', 'w') as f:
        writer = csv.writer(f)
        # for i in range(1, pages+1):
        # url_page = 'https://{}:9060/ers/config/guestuser?size=100&page={}'.format(
        # ise_ip, i)
        # req_page = requests.get(url_page, headers=headers, auth=(
        # api_user, api_pw), verify=False)
        #myjson = req_page.text
        #parsed_json = (json.loads(myjson))
        for user in parsed_json['SearchResult']['resources']:
            users.append(user['id'])
        for id in users:
            url = 'https://{}:9060/ers/config/guestuser/{}'.format(ise_ip, id)
            req = requests.get(url, headers=headers, auth=(
                api_user, api_pw), verify=False)
            myjson = req.text
            parsed_json = (json.loads(myjson))
            username = parsed_json['GuestUser']['guestInfo']['userName']
            firstname = parsed_json['GuestUser']['guestInfo']['firstName']
            lastname = parsed_json['GuestUser']['guestInfo']['lastName']
            company = parsed_json['GuestUser']['guestInfo']['company']
            enabled = parsed_json['GuestUser']['guestInfo']['enabled']
            validdays = parsed_json['GuestUser']['guestAccessInfo']['validDays']
            fromdate = parsed_json['GuestUser']['guestAccessInfo']['fromDate']
            todate = parsed_json['GuestUser']['guestAccessInfo']['toDate']
            location = parsed_json['GuestUser']['guestAccessInfo']['location']
            row = [username, firstname, lastname, company,
                   enabled, validdays, fromdate, todate, location]
            writer.writerow(row)

# ==============================================================================
# ---- Main: Get Devices
# ==============================================================================


get_user()
