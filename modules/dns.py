#!/bin/python

#Importig packages
import dns.resolver
from colorama import Fore, Back, Style #Coloring package

#class DNS
class DNS:
	#constructor
	def __init__(self,target):
		self.domain = target

	#Getting DNS information
	def get_dns(self):
		print(f"{Fore.GREEN}\n[+] Gathering DNS Information .. {Style.RESET_ALL}")
		try:
			print(f"{Fore.GREEN}[+] DNS Information found .. {Style.RESET_ALL}")
			print("DNS Information :")
			print("-----------------------------------------------------------------------------------------------")
			print ("{:<20} {:<20}".format('| RECORD', '| DATA'))
			print("-----------------------------------------------------------------------------------------------")
			try:
				for soa in dns.resolver.resolve(self.domain, "SOA"):
					print ("{:<20} {:<20}".format('| SOA Record', f'| {soa}'))
			except:
				print(f"{Fore.YELLOW}[!] SOA record Information not found ..{Style.RESET_ALL}")
			try:
				for a in dns.resolver.resolve(self.domain, "A"):
					print ("{:<20} {:<20}".format('| A Record', f'| {a}'))
			except:
				print(f"{Fore.YELLOW}[!] A record Information not found ..{Style.RESET_ALL}")
			try:
				for ns in dns.resolver.resolve(self.domain, "NS"):
					print ("{:<20} {:<20}".format('| NS Record', f'| {ns}'))
			except:
				print(f"{Fore.YELLOW}[!] NS Information not found ..{Style.RESET_ALL}")
			try:
				for mx in dns.resolver.resolve(self.domain, "MX"):
					print ("{:<20} {:<20}".format('| MX Record', f'| {mx}'))
			except:
				print(f"{Fore.YELLOW}[!] MX Information not found ..{Style.RESET_ALL}")
			try:
				for txt in dns.resolver.resolve(self.domain, "TXT"):
					print ("{:<20} {:<20}".format('| TXT Record', f'| {txt}'))
			except:
				print(f"{Fore.YELLOW}[!] TXT Information not found ..{Style.RESET_ALL}")
			print("-----------------------------------------------------------------------------------------------\n")
		except KeyboardInterrupt as e:
			print(f"{Fore.RED}\n[-] Process terminated by user ..{Style.RESET_ALL}")
		except Exception as e:
			print(f"{Fore.RED}[!] DNS Information not found ..{Style.RESET_ALL}")