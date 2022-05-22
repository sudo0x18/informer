#!/bin/python

#Importing Packages
from colorama import Fore, Back, Style #Coloring package
import shodan #Getting shodan information

#shodan class
class Shodan:
	#contructor
	def __init__(self,target):
		self.domain = target

	#Getting shodan info
	def get_shodan(self):
		print(f"{Fore.GREEN}\n[+] Gathering Shodan Information .. {Style.RESET_ALL}")
		try:
			self.shodan = shodan.Shodan("wbETG8kiTinJaNch4632rp6vE1sH228h")
			self.info = self.shodan.search(str(self.domain),limit=5)
			if(len(self.info['matches']) > 0):
				print(f"{Fore.GREEN}[+] Shodan Information found .. {Style.RESET_ALL}")
				for i in self.info['matches']:
					print(f"\n[+]-------------------------------------------------------------------------------------------------------------------------------\n")
					print(f"{Fore.GREEN}[*] IP : {i['ip_str']}{Style.RESET_ALL}")
					print(f"[*] Data : \n{i['data']}")
			else:
				print(f"{Fore.RED}[!] Shodan Information not found ..{Style.RESET_ALL}")
		except KeyboardInterrupt as e:
			print(f"{Fore.RED}\n[-] Process terminated by user ..{Style.RESET_ALL}")
		except Exception as e:
			print(e)
			print(f"{Fore.RED}[!] Shodan Information not found ..{Style.RESET_ALL}")