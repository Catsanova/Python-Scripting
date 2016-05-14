#April 25 2015
#Niall Wiggins
#CNT 4603

'''
Created on Apr 27, 2015

@author: Niall
'''
import re


fileObject = input("Please enter the name of the file containing the input Canadian postal code: ")
file = open(fileObject, "r")

print("\n")

for string in open(fileObject):
     

    if re.search("[ABCEGHJKLMNPRSTVXY][0-9][ABCEGHJKLMNPRSTVWXYZ] [0-9][ABCEGHJKLMNPRSTVWXYZ][0-9]$", string):
        print("Match found - valid Canadian address:\n", string, "\n")
    else: print("Error - no match - invalid Canadian address:\n", string, "\n")
file.close()