#!/usr/bin/python3

import os
import socket
import argparse
import requests
from prettytable import PrettyTable

# Vars
api_host = socket.gethostname()
api_port = 30800
api_endpoint = 'http://{}:{}'.format(api_host, api_port)

# Get current user
username = os.getlogin()

# Get Simple User Report
def getUserReport(api_endpoint,username,months):
    response = requests.get("{}/report/users/{}?months={}".format(api_endpoint,username,months))
    return response.json()

# Get Simple Group Report
def getGroupReport(api_endpoint,username,months):
    response = requests.get("{}/report/groups/{}?months={}".format(api_endpoint,username,months))
    return response.json()

# Print a Basic Key/Value Report in a Table
def printBasicReport(report,title):
    table = PrettyTable()
    table.field_names = [title,"Value"]
    for key, value in report.items():
        table.add_row([value['name'], value['value']])

    print(table)


# Parse Args
parser = argparse.ArgumentParser()
parser.add_argument("-u", action='store_true')
parser.add_argument("-g", action='store_true')
parser.add_argument("-m", type=int, default=1)
args = parser.parse_args()

if args.u or args.g:
    print("NOTICE: These figures are estimated based on job data as of the previous 24hours")
    print("        Final billing calculations are done by the billing team at the end of each cycle")
if args.u:
    # Print User Report
    printBasicReport(
        getUserReport(api_endpoint,username,args.m),
        "Estimated Usage Report"
    )

if args.g:
    # Print Group Report
    printBasicReport(
        getGroupReport(api_endpoint,username,args.m),
        "Estimated Usage Report"
    )