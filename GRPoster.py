


logo = """

 _______ _     ____ _______                  _             _             
|__   __| |   |___ \__   __|                (_)           | |            
   | |  | |__   __) | | | ___ _ __ _ __ ___  _ _ __   __ _| |_ ___  _ __ 
   | |  | '_ \ |__ <  | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | __/ _ \| '__|
   | |  | | | |___) | | |  __/ |  | | | | | | | | | | (_| | || (_) | |   
   |_|  |_| |_|____/  |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|\__\___/|_| 
					
		    TH3 TERMINATOR SCRIPT TOOL :")
		   Coded by Bido. => Abdallah Ahmed
		   https://www.facebook.com/bido.32
"""


print(logo)


# GRPoster Script :")
from selenium import webdriver
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import UnexpectedAlertPresentException
import time,os
import getpass
import glob
import sys

# The Script Code 
def main():
	u_name = input("Enter Your Facebook Username >> ")
	u_pass = input("Enter Your Facebook Password >> ")
	timer = input("Enter Seconds To Wait >> ")
	print("\n++[GRPoster]++ >> Choose Your Files \n")
	os.chdir(".")
	print("_______________")
	for file in glob.glob("*.txt"):
		print(" |_--> " + file)
	msg = input("\nEnter Your Msg file name >> ")
	msgfile = open(msg,'r').readlines()
	groups = input("Enter Your Groubs Linke File Name >> ")
	grfile = open(groups,'r').readlines()
	driver = webdriver.Chrome("C:\Selenium\Chrome\chromedriver.exe")
	driver.get('https://mbasic.facebook.com')
	print("\n++[GRPoster]++ >> Logging In Now ....\n")
	username = driver.find_element_by_name('email')
	password = driver.find_element_by_name('pass')
	sub = driver.find_element_by_name('login')
	username.send_keys(u_name)
	password.send_keys(u_pass)
	sub.click()
	time.sleep(2)
	print("++[GRPoster]++ >> Posting Now ....\n")
	for grp in grfile:
		driver.get(grp)
		time.sleep(int(timer))
		post_form = driver.find_element_by_name('xc_message')
		post_form.send_keys(msgfile)
		post_btn = driver.find_element_by_name('view_post')
		post_btn.click()
		print("++[GRPoster]++ >> Done Posting !...\n")
		time.sleep(2)
		
def about():
	print("++[GRPoster]++ >> All Done :') !.. \n")
	print("++[GRPoster]++ >> Coded By >> Bido\n")
	print("--*[ www.facebook.com/bido.32 ]*--\n")
	print("Thanks For Used My Scripts <3 \n")


if __name__ == '__main__':main()
about()