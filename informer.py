#!/bin/python

#Importing Packages
from colorama import Fore, Back, Style #Coloring package
import argparse #Package for argument parsing
import whois #Package for whois information
import os #For screen clearing

#Defining informer class
class Informer:
	#Creating banner, description and usage
	BANNER = f"""
  _____       __                               
 |_   _|     / _|                              
   | | _ __ | |_ ___  _ __ _ __ ___   ___ _ __ 
   | || '_ \|  _/ _ \| '__| '_ ` _ \ / _ \ '__|
  _| || | | | || (_) | |  | | | | | |  __/ |   
  \___/_| |_|_| \___/|_|  |_| |_| |_|\___|_|   
                                               
 {Back.RED}  Created by Jay Vadhaiya, Github: sudo0x18  {Style.RESET_ALL}
"""
	DESCRIPTION = f"""\n{Fore.BLUE}DESCRIPTION {Style.RESET_ALL}:\n-------------\nInformer is a Basic information gathering tool that provides\nvarious information about target like whois info,\nDNS info, Geolocation info of server and Shodan info."""

	USAGE = f"{Fore.GREEN}python3 informer.py -t TARGET_DOMAIN [-d] [-s] [--help]{Style.RESET_ALL}"

	#Contructor
	def __init__(self):
		#initializing and setting argument options to be received.
		self.argParse = argparse.ArgumentParser(
			formatter_class = argparse.RawDescriptionHelpFormatter,
			description = self.DESCRIPTION,
			usage = self.USAGE
			)
		self.argParse.add_argument("-t","--target",help="Target domain name.",required=True)
		self.argParse.add_argument("-d","--dns",nargs="?",help="Option for fetching DNS information.",const=True)
		self.argParse.add_argument("-s","--shodan",nargs="?",help="Option for fetching Shodan information.",const=True)
		self.args = self.argParse.parse_args() #parsing the arguments

	#Class method for printing banner
	@classmethod
	def show_banner(self):
		print(self.BANNER)

	@classmethod
	#screen clearer function
	def screen_clear(self):
		if os.name == "posix":
			#For linux and mac
			os.system("clear")
		else:
			#for windows
			os.system("cls")

	#Getting whois information
	def get_whois(self):
		print(f"{Fore.GREEN}[+] Gathering whois Information .. {Style.RESET_ALL}")
		try:
			self.domain = self.args.target #Target
			self.whois = whois.query(self.domain) #fetching details
			if self.whois is not None:
				print(f"{Fore.GREEN}[+] whois Information Found ..{Style.RESET_ALL}")
				print("-----------------------------------------------------------------------------------------------")
				print ("{:<20} {:<20}".format('| NAME', '| DATA'))
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

if __name__ == "__main__":
	Informer.screen_clear() #clearing screen
	Informer.show_banner() #Showing banner
	informer = Informer() #Initializing object
	informer.get_whois() #Printing whois information