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
		print(f"{Fore.GREEN}\n[+] Gathering DNS Information .. {Fore.RESET}")
		try:
			print(f"{Fore.GREEN}[+] DNS Information found .. {Fore.RESET}")
			print("DNS Information :")
			print("-"*95)
			print ("{:<20} {:<20}".format('| RECORD', '| DATA'))
			print("-"*95)
			try:
				for soa in dns.resolver.resolve(self.domain, "SOA"):
					print ("{:<20} {:<20}".format('| SOA Record', f'| {soa}'))
			except:
				print(f"{Fore.YELLOW}[!] SOA record Information not found ..{Fore.RESET}")
			try:
				for a in dns.resolver.resolve(self.domain, "A"):
					print ("{:<20} {:<20}".format('| A Record', f'| {a}'))
			except:
				print(f"{Fore.YELLOW}[!] A record Information not found ..{Fore.RESET}")
			try:
				for ns in dns.resolver.resolve(self.domain, "NS"):
					print ("{:<20} {:<20}".format('| NS Record', f'| {ns}'))
			except:
				print(f"{Fore.YELLOW}[!] NS Information not found ..{Fore.RESET}")
			try:
				for mx in dns.resolver.resolve(self.domain, "MX"):
					print ("{:<20} {:<20}".format('| MX Record', f'| {mx}'))
			except:
				print(f"{Fore.YELLOW}[!] MX Information not found ..{Fore.RESET}")
			try:
				for txt in dns.resolver.resolve(self.domain, "TXT"):
					print ("{:<20} {:<20}".format('| TXT Record', f'| {txt}'))
			except:
				print(f"{Fore.YELLOW}[!] TXT Information not found ..{Fore.RESET}")
			print("-"*95+"\n")
		except KeyboardInterrupt as e:
			print(f"{Fore.RED}\n[-] Process terminated by user ..{Fore.RESET}")
		except Exception as e:
			print(f"{Fore.RED}[!] DNS Information not found ..{Fore.RESET}")