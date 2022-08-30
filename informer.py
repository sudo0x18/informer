#!/bin/python

#Importing Packages
from colorama import init, Fore, Back, Style #Coloring package
import argparse #Package for argument parsing
import os #For screen clearing
import sys #System package
import re #regular expression

from modules.whois import Whois #Whois class from whois module file
from modules.dns import DNS #DNS class from dns module file
from modules.geolocation import Geolocation #Geolocation class from geolocation module file
from modules.shodan import Shodan #Shodan class from shodan module file
from modules.logger import Logger #Logger class from logger module file
from modules.subdomain import SubDomain #SubDomain class from subdomain module file 

#Defining informer class
class Informer:
	#Creating banner, description and usage
	BANNER = f"""{Style.BRIGHT}
  _____       __                               
 |_   _|     / _|                              
   | | _ __ | |_ ___  _ __ _ __ ___   ___ _ __ 
   | || '_ \|  _/ _ \| '__| '_ ` _ \ / _ \ '__|
  _| || | | | || (_) | |  | | | | | |  __/ |   
  \___/_| |_|_| \___/|_|  |_| |_| |_|\___|_|   
                                               
 {Back.RED}  Created by Jay Vadhaiya, Github: sudo0x18  {Back.RESET}{Style.RESET_ALL}
"""
	DESCRIPTION = f"""\n{Fore.BLUE}DESCRIPTION {Fore.RESET}:\n-------------\nInformer is a OSINT information gathering tool that gathers whois, Sub-domain, DNS, geolocation and shodan information of the target."""

	USAGE = f"{Fore.GREEN}python3 informer.py -t TARGET_DOMAIN [-d] [-g] [-s] [-o FILE] [--help]{Fore.RESET}"

	#Contructor
	def __init__(self):
		#initializing and setting argument options to be received.
		self.argParse = argparse.ArgumentParser(
			formatter_class = argparse.RawDescriptionHelpFormatter,
			description = self.DESCRIPTION,
			usage = self.USAGE
			)
		self.argParse.add_argument("-t","--target",help="Target domain name.",required=True)
		self.argParse.add_argument("-d","--dns",nargs="?",help="Get DNS Information",const=True)
		self.argParse.add_argument("-g","--geolocation",nargs="?",help="Get Geolocation Information.",const=True)
		self.argParse.add_argument("-s","--shodan",nargs="?",help="Get Shodan Information.",const=True)
		self.argParse.add_argument("-sd","--subdomain",nargs="?",help="Get Subdomain Information.",const=True)
		self.argParse.add_argument("-o","--output",help="Save output to desired file.")
		self.args = self.argParse.parse_args() #parsing the arguments

		#Setting output class
		if self.args.output:
			sys.stdout = Logger(self.args.output)

		#Initializing colorama instance for cross platform coloring
		init()

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

if __name__ == "__main__":
	Informer.screen_clear() #clearing screen
	Informer.show_banner() #Showing banner
	informer = Informer() #Initializing object

	whois = Whois(informer.args.target) #Creating Whois class object
	whois.get_whois() #Printing whois information
	try:
		if informer.args.dns:
			dns = DNS(informer.args.target) #Creating DNS class object
			dns.get_dns() #Printing DNS information

		if informer.args.geolocation:
			geo = Geolocation(informer.args.target) #Creating Geolocation class object
			geo.get_geolocation() #Printing Geolocation information

		if informer.args.shodan:
			shodan = Shodan(informer.args.target) #Creating shodan class object
			shodan.get_shodan() #Printing shodan information

		if informer.args.subdomain:
			subdomain = SubDomain(informer.args.target) #Creating subdomain class object
			subdomain.get_subdomain() #Printing subdomain data

	except KeyboardInterrupt as e:
		print(f"{Fore.RED}\n[-] Process terminated by user ..{Fore.RESET}")