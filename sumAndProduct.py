# p5sumAndProduct.py
# Dylan House
# Python version: 3.2.5.1
# 2/3/2016
# Receive input of two different numbers, multiply them, and sum them.

print ("I'm going to need two numbers from you.")
num1 = int(input ("Please enter a number: "))
num2 = int(input ("And the second:        "))

print ("The sum of " + str(num1) + " and " + str(num2) + " is ", end='\n\t')
print (num1*num2, end='')
print ('.')
print ("The product of " + str(num1) + " and " + str(num2) + " is ", end='\n\t')
print (num1+num2, end='')
print ('.')

'''
>>> ================================ RESTART ================================
>>> 
I'm going to need two numbers from you.
Please enter a number: 10
And the second:        20
The sum of 10 and 20 is 
	200.
The product of 10 and 20 is 
	30.
>>> 
'''
