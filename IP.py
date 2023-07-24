import requests
import os
import pprint

def ip():
    ip = str(input("\n\n\nEnter IP Address: "))
    url = f"https://ipapi.co/{ip}/json/"
    r = requests.get(url)
    pprint.pprint(r.json())

while True:
    ip()
