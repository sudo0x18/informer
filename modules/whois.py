#!/bin/python

#Importing packages
import whois #Package for whois information
from colorama import Fore, Back, Style #Coloring package

#Defining whois class
class Whois:
	#Constructor
	def __init__(self, target):
		self.domain = target

	#Getting whois information
	def get_whois(self):
		print(f"{Fore.GREEN}[+] Gathering whois Information .. {Style.RESET_ALL}")
		try:
			self.whois = whois.query(self.domain) #fetching details
			if self.whois is not None:
				print(f"{Fore.GREEN}[+] whois Information Found ..{Style.RESET_ALL}")
				print("-----------------------------------------------------------------------------------------------")
				print ("{:<20} {:<20}".format('| RECORD', '| DATA'))
				print("-----------------------------------------------------------------------------------------------")
				try:
					print("{:<20} {:<20}".format("| Name",f"| {self.whois.name}"))
				except:
					pass
				try:
					print("{:<20} {:<20}".format("| Registrar",f"| {self.whois.registrar}"))
				except:
					pass
				try:
					print("{:<20} {:<20}".format("| Registrant Country",f"| {self.whois.registrant_country}"))
				except:
					pass
				try:
					print("{:<20} {:<20}".format("| Creation Date",f"| {self.whois.creation_date}"))
				except:
					pass
				try:
					print("{:<20} {:<20}".format("| Expiration Date",f"| {self.whois.expiration_date}"))
				except:
					pass
				try:
					print("{:<20} {:<20}".format("| Last Updated",f"| {self.whois.last_updated}"))
				except:
					pass
				try:
					for i in self.whois.statuses:
						print("{:<20} {:<20}".format("| Status",f"| {i}"))
				except:
					pass
				try:
					print("{:<20} {:<20}".format("| DNS Sec",f"| {self.whois.dnssec}"))
				except:
					pass
				try:
					for i in name_servers:
						print("{:<20} {:<20}".format("| Name Server",f"| {i}"))
				except:
					pass
				try:
					print("{:<20} {:<20}".format("| Registrant",f"| {self.whois.registrant}"))
				except:
					pass
				print("-----------------------------------------------------------------------------------------------\n")
			else:
				print(f"{Fore.RED}[!] whois Information not found ..{Style.RESET_ALL}")
		except KeyboardInterrupt as e:
			print(f"{Fore.RED}\n[-] Process terminated by user ..{Style.RESET_ALL}")
		except Exception as e:
			print(f"{Fore.RED}[!] whois Information not found ..{Style.RESET_ALL}")