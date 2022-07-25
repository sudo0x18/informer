#!/bin/python

#Importing Packages
from colorama import Fore, Back, Style #Coloring package
import shodan #Getting shodan information
import json #Convert dict to json

#shodan class
class Shodan:
	#contructor
	def __init__(self,target):
		self.domain = target

	#Getting shodan info
	def get_shodan(self):
		print(f"{Fore.GREEN}\n[+] Gathering Shodan Information .. {Fore.RESET}")
		try:
			self.shodan = shodan.Shodan("wbETG8kiTinJaNch4632rp6vE1sH228h")
			self.info = self.shodan.search(str(self.domain),limit=5)
			if(len(self.info) > 0):
				with open(f"shodan_{self.domain}.json", "w") as sdata:
					sdata.write(json.dumps(self.info, indent=4))
					sdata.close()
				print(f"{Fore.GREEN}[+] Shodan info stored in shodan_{self.domain}.json {Fore.RESET}")
			else:
				print(f"{Fore.RED}[!] Shodan Information not found ..{Fore.RESET}")
		except KeyboardInterrupt as e:
			print(f"{Fore.RED}\n[-] Process terminated by user ..{Fore.RESET}")
		except Exception as e:
			print(e)
			print(f"{Fore.RED}[!] Shodan Information not found ..{Fore.RESET}")