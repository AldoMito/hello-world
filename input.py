# p3input.py
# Dylan House
# Python Version 3.2.5.1
# 2/3/2016
# Practicing input/output.

name = input ("Please enter your name: ")
weightLbs = float(input ("Please enter your weight in lbs: "))
print ("\nDon't worry, no one is judging you!\n")
age = int(input ("Please enter your age: "))
weightKg = weightLbs*0.453592
title = "Unbeliever"

print ("\nHello,", title, name + "! Your weight is: ", end='')
print (weightLbs, "lbs.")
print ("In case you were curious, that comes out to _%.2f_ " %weightKg, end='')
print ("kilograms.")
'''
>>> ================================ RESTART ================================
>>> 
Please enter your name: Dylan
Please enter your weight in lbs: 135

Don't worry, no one is judging you!

Please enter your age: 25

Hello, Unbeliever Dylan! Your weight is: 135.0 lbs.
In case you were curious, that comes out to _61.23_ kilograms.
>>>
'''
