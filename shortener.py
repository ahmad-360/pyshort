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
    f= open("apis.txt","w+")
    f.write("api2")
    f.close()


elif shorter == 2:
    url2=input(colored("\nEnter the url : " ,"red"))
    api2= str(input(colored("\nEnter Your api : ",'yellow')))
    id2=input(colored("\nEnter your adfly User Id : ",'blue'))
    shortener= pyshorteners.Shortener(api_key=api2, user_id=id2)
    short= shortener.adfly.short(url2)
    print (colored(short,"green"))
    f= open("apis.txt","w+")
    f.write(api2)
    f.close()
    print("your api has benn saved")


elif shorter is 3 : 
    url3=input(colored("\nEnter the url : " ,"red"))
    api3= input(colored("\nEnter Your api : ",'yellow'))
    shortener= pyshorteners.Shortener(api_key=api3)

    short= shortener.bitly.short(url3)
    print (colored(short,"green"))    

    with open('apis.txt', 'a') as s:
        s.write(api3 + '\n')

        print('your api has benn saved')