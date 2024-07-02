# import sys

import re


var_name = input("Enter your name:")
var_task = int(input("Enter the number task you want to do:"))
print("=======================================================")
var_choose = print("Please Choose your task:")
print("=======================================================")
list = ["LG: Login", "RG: Register", "US: User", "EMP: Employee", "TS: TimeSheet"] 
for index, item in enumerate(list): 
    print (item)

print("=======================================================")
var_choose_task = input("Choose a task:")
if var_choose_task != list:
    print("Entry is valid!")
else:
    print("Entry is not valid!")  

var_wo = int(input("Enter your working hour for login (in float, e.g 1.5 for 1 hour 30 minutes): "))

    
