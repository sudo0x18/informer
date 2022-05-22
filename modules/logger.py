#!/bin/python

#Importing packages
import sys #system module
 
#logger class
class Logger:

    BANNER = f"""
  _____       __                               
 |_   _|     / _|                              
   | | _ __ | |_ ___  _ __ _ __ ___   ___ _ __ 
   | || '_ \|  _/ _ \| '__| '_ ` _ \ / _ \ '__|
  _| || | | | || (_) | |  | | | | | |  __/ |   
  \___/_| |_|_| \___/|_|  |_| |_| |_|\___|_|   
                                               
"""
    DESCRIPTION = f"""Informer is a Basic information gathering tool that provides\nvarious information about target like whois info,\nDNS info, Geolocation info of server and Shodan info."""

    #defining contructor
    def __init__(self, filename):
        self.console = sys.stdout
        self.file = open(filename, 'w')
        self.file.write(self.BANNER)
        self.file.write(self.DESCRIPTION)
 
    #Write function
    def write(self, message):
        self.console.write(message)
        if "[+]" not in message and "[!]" not in message and "[*]" not in message and "[-]" not in message:
            self.file.write(message)
 
    #Flush function
    def flush(self):
        self.console.flush()
        self.file.flush()