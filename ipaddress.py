#April 25 2015
#Niall Wiggins
#CNT 4603

'''
Created on Apr 27, 2015

@author: Niall
'''
import re

pattern = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

fileObject = input("Please enter the name of the file containing the input IP addresses: ")
file = open(fileObject, "r")
print("\n")

for string in open(fileObject):
    
    m = re.match(pattern, string)
    if m is not None:
        print("Match found - valid IP address:", string, "\n")
    else: print("Error - no match - invalid IP address:", string, "\n")
file.close()