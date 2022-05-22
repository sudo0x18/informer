#!/bin/python

#Importing Packages
from colorama import Fore, Back, Style #Coloring package
import argparse #Package for argument parsing
import os #For screen clearing

from modules.whois import Whois #Whois class from whois module file
from modules.dns import DNS #DNS class from whois module file
from modules.geolocation import Geolocation #Geolocation class from whois module file

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

	USAGE = f"{Fore.GREEN}python3 informer.py -t TARGET_DOMAIN [-d] [-g] [-s] [-o FILE] [--help]{Style.RESET_ALL}"

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
		self.argParse.add_argument("-g","--geolocation",nargs="?",help="Option for fetching Geolocation information.",const=True)
		self.argParse.add_argument("-s","--shodan",nargs="?",help="Option for fetching Shodan information.",const=True)
		self.argParse.add_argument("-o","--output",help="Save output to desired file.")
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

if __name__ == "__main__":
	Informer.screen_clear() #clearing screen
	Informer.show_banner() #Showing banner
	informer = Informer() #Initializing object

	whois = Whois(informer.args.target) #Creating Whois class object
	whois.get_whois() #Printing whois information

	if informer.args.dns:
		dns = DNS(informer.args.target) #Creating DNS class object
		dns.get_dns() #Printing DNS information

	if informer.args.geolocation:
		geo = Geolocation(informer.args.target) #Creating Geolocation class object
		geo.get_geolocation() #Printing Geolocation information