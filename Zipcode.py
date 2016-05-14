#April 25 2015
#Niall Wiggins
#CNT 4603

'''
Created on Apr 27, 2015

@author: Niall
'''
import re

pattern = '([0-9]{5}(\-[0-9]{4})?)$'

fileObject = input("Please enter the name of the file containing the input zipcodes: ")
file = open(fileObject, "r")
print("\n")
for string in open(fileObject):
    
    m = re.match(pattern, string)
    if m is not None:
        print("Match found - valid U.S.  zipcode:", string, "\n")
    else: print("Error - no match - invalid U.S. zipcode:", string, "\n")
file.close()