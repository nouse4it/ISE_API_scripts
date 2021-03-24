[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

# ISE_API_scripts
Use API calls to gather informations from Cisco ISE (tested with v2.7 Patch3)

Author: nouse4it <github@schlueter-online.net>


## get_devices_ISE_API.py

Illustrate the following conecepts:
- Get all network devices for from ISE and store them in csv format

## Use Case Description

The scripts is used to gather all Network Devices from Cisco ISE by Rest API.
It then saves alle the informations into a csv file.
The script leverages the Cisco ISE ERS API
For more informations see [ERS API Documentation](https://community.cisco.com/t5/security-documents/ise-ers-api-examples/ta-p/3622623#toc-hId--721274487)

## Installation
You will need the Python Module [requests](https://pypi.org/project/requests/)
You can install it via `pip install requests`

[Documentation](https://requests.readthedocs.io/en/master/) for more informations regardings requests.

Python Version must be at least v3.6

## Usage
When you run the script, you will asked to input the following informations:
* IP of Cisco ISE
* Username of ERS API user
* Password of ERS API user

## How it works
The script queries the API for the wanted informations (you can adjust this script to gather other informations aswell)
When there are a lot of information, the API pages the returned Informations.
Maximum a 100 results can be received at one page.
So when you have more than 100 devices, the script checks for how many pages would be available and writes the results of every page into the csv.
