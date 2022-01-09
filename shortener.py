############### LYBS ##############################
import pyshorteners
import random  
import os
import termcolor
from termcolor import colored
import numpy as np
############## VARIABLES ##########################
#os.system("clear")

list1=["white","green","yellow","blue","cyan","magenta"]

colors=random.choice(list1)

list2=["yellow","white","magenta","cyan", "blue" ,"green"]

colors2=random.choice(list1)

Title=colored("""
                 _                _   
 _ __  _   _ ___| |__   ___  _ __| |_ 
| '_ \| | | / __| '_ \ / _ \| '__| __|
| |_) | |_| \__ \ | | | (_) | |  | |_ 
| .__/ \__, |___/_| |_|\___/|_|   \__|
|_|    |___/                          

      
                        by Mal4D
""",colors)

print(Title)

################## SHORTERS ##############################

user=input('Is this your first time use this app ? (Yes/No) : ')

if user == "yes":


    shorter=int(input (colored("""\nThis the services of shorting url  \n
    1 ==> tiny url(whitout Api)
    2 ==> Adfly
    3 ==> Bitly\n
    Enter the number of what de you want:  """, 'cyan')))


    if shorter is 1 : 
        url1=input(colored("\nEnter the url : " ,'yellow'))
        shortener= pyshorteners.Shortener()
        short= shortener.tinyurl.short(url1)
        print (colored(short,"green"))    


    elif shorter == 2:
        url2=input(colored("\nEnter the url : " ,"red"))
        api2= str(input(colored("\nEnter Your api : ",'yellow')))
        id2=input(colored("\nEnter your adfly User Id : ",'blue'))
        shortener= pyshorteners.Shortener(api_key=api2, user_id=id2)
        short= shortener.adfly.short(url2)
        print (colored(short,"green"))
        f= open("apiadfly.txt","w+")
        f.write(api2)
        f2=open("idadfly.txt","w+")
        f2.write(id2)
        f.close()
        f2.close()
        print("your api and id  has been saved")


    elif shorter is 3 : 
        url3=input(colored("\nEnter the url : " ,"red"))
        api3= input(colored("\nEnter Your api : ",'yellow'))
        shortener= pyshorteners.Shortener(api_key=api3)
        short= shortener.bitly.short(url3)
        print (colored(short,"green"))    
        f= open("apibitly.txt","w+")
        f.write(api3)
        f.close()
        print("your api and id  has been saved")

if user == "no":
    shorter1=int(input (colored("""\nThis the services of shorting url  \n
    1 ==> tiny url(whitout Api)
    2 ==> Adfly
    3 ==> Bitly
    4 == > Erase Api and Id Info \n
    Enter the number of what de you want:  """, 'cyan')))


    if shorter1 is 1 : 
        url1=input(colored("\nEnter the url : " ,'yellow'))
        shortener= pyshorteners.Shortener()
        short= shortener.tinyurl.short(url1)
        print (colored(short,"green"))    


    elif shorter1 == 2:
        url2=input(colored("\nEnter the url : " ,"red"))
        f= open('apiadfly.txt', 'r')
        api2= f.read()
        f2= open('idadfly.txt', 'r')
        id2= f.read()
        shortener= pyshorteners.Shortener(api_key=api2, user_id=id2)
        short= shortener.adfly.short(url2)
        print (colored(short,"green"))


    elif shorter1 is 3 : 
        url3=input(colored("\nEnter the url : " ,"red"))
        f1= open("apibitly.txt","r")
        api3=f1.read()
        shortener= pyshorteners.Shortener(api_key=api3)
        short= shortener.bitly.short(url3)
        print (colored(short,"green"))    
        f= open("apibitly.txt","r+")
        f.close()

    elif shorter1 is 4:
        erase=int(input(colored("""
        1 ==> Adfly data 
        2 ==> Bitly  data
        3 ===> All\n

        Enter the number of data you want erase : 
        """, 'red')))
        if erase is 1:
            os.remove("apiadfly.txt")
            os.remove("idadfly.txt")

        if erase is 2:
            os.remove("apibitly.txt")

        if erase is 3:
            os.remove("apiadfly.txt")
            os.remove("idadfly.txt")

            os.remove("apibitly.txt")

        