import requests
import os
import pprint
while True:
	def ip():
		ip=str(input("\n\n\nEnter Ip Address :  "))
		url=f"https://ipapi.co/{ip}/json/"
		r=requests.get(url)
		pprint.pprint(r.json())
	ip()
