#!/bin/python

#Importing packages
from colorama import Fore, Back, Style #Coloring package
import socket #Socket for converting domain into IP
import requests #Doing request to the resource

#Geolocation class
class Geolocation:
	#defining constructor
	def __init__(self, target):
		self.domain = target

	#Getting geolocation information
	def get_geolocation(self):
		print(f"{Fore.GREEN}\n[+] Gathering Geolocation Information .. {Style.RESET_ALL}")
		try:
			result = requests.request("GET",f"https://geolocation-db.com/json/{socket.gethostbyname(self.domain)}").json()
			print(f"{Fore.GREEN}[+] Geolocation Information found .. {Style.RESET_ALL}")
			print("-----------------------------------------------------------------------------------------------")
			print ("{:<20} {:<20}".format('| RECORD', '| DATA'))
			print("-----------------------------------------------------------------------------------------------")
			print ("{:<20} {:<20}".format('| IPv4', f"| {result['IPv4']}"))
			print ("{:<20} {:<20}".format('| Country Name', f"| {result['country_name']}"))
			print ("{:<20} {:<20}".format('| Country Code', f"| {result['country_code']}"))
			print ("{:<20} {:<20}".format('| Postal Code', f"| {result['postal']}"))
			print ("{:<20} {:<20}".format('| State', f"| {result['state']}"))
			print ("{:<20} {:<20}".format('| Lalitude', f"| {result['latitude']}"))
			print ("{:<20} {:<20}".format('| Longitude', f"| {result['longitude']}"))
			print("-----------------------------------------------------------------------------------------------\n")
		except KeyboardInterrupt as e:
			print(f"{Fore.RED}\n[-] Process terminated by user ..{Style.RESET_ALL}")
		except Exception as e:
			print(f"{Fore.RED}[!] Geolocation Information not found ..{Style.RESET_ALL}")