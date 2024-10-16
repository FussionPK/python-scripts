#This is Shel bot! not shell terminal.... shell for shelby. 
#Shellbot is a state of the art secret. Meant to perform and deliver results on really sophisticated networks.
#shellbot will perform a ping scan first in order to see if the host is reachable and alive... then shellbot performs a vulnerability scan that will find open ports and services running on them. from there you can do -h for help :D

#importing required libraries

import time
import math



#Declaring variables.

varA = "shellbot"
varB = 10
varC = ""

#performing ping scan

print(f"Hi this is {varA} welcome... ")

rep = str(input("Would you like to begin the process...? Y/N.... "))

if rep == "Y" :
    print("Starting...")
    time.sleep(1)
    print("Beginning ping scan....")
    
    while varB > 0:
        print(varB)
        varB -= 1
        time.sleep(1)
    print("ping scan done")

elif rep == "N":
    print("Process Terminating....")

else:
    print("Not a valid input....!")
