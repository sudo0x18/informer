#!/bin/python

#Importing packages
from colorama import Fore, Back, Style #Coloring package
import socket #Socket for converting domain into IP
from pycrtsh import Crtsh #For subdomain finding

#SubDomain class
class SubDomain:
	#defining constructor
	def __init__(self, target):
		self.domain = target

	#Getting subdomain information
	def get_subdomain(self):
		print(f"{Fore.GREEN}\n[+] Finding Subdomain Information .. {Fore.RESET}")
		try:
			self.crtsh = Crtsh()
			self.certs = self.crtsh.search(self.domain)
			print(f"{Fore.GREEN}[+] Subdomain Information found .. {Fore.RESET}")
			print("Subdomain Information :")
			print("-"*95)
			print ("{:<20}".format('| Subdomain'))
			print("-"*95)
			self.domains = []
			for cert in self.certs:
				self.data = cert['name'].split("\n")
				for i in self.data:
					self.domains.append(i)
			self.domains = list(set(self.domains))
			
			for domain in self.domains:
				print ("{:<20}".format(f'| {domain}'))	
		
			print("-"*95+"\n")
		except KeyboardInterrupt as e:
			print(f"{Fore.RED}\n[-] Process terminated by user ..{Fore.RESET}")
		except Exception as e:
			print(e)
			print(f"{Fore.RED}[!] Subdomain Information not found ..{Fore.RESET}")