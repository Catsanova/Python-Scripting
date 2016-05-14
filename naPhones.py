#April 25 2015
#Niall Wiggins
#CNT 4603

'''
Created on Apr 27, 2015

@author: Niall
'''
import re


fileObject = input("Please enter the name of the file containing the input North American phone number: ")
file = open(fileObject, "r")

print("\n")

for string in open(fileObject):
     

    if re.search("([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})", string):
        print("Match found - valid North American phone number:\n", string, "\n")
    else: print("Error - no match - invalid North American phone number:\n", string, "\n")
file.close()