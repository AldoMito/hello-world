'''
IF statements and booleans
Dylan House
Python 3.2.5.1
'''
# TRUE/ FALSE -- BOOLEAN DATA TYPE
# if (condition):
#     some statement # the statement happens only if the condition is true

# RELATIONAL OPERATORS
# == equal to
# != not equal
# >= greater than or equal to
# <= less than or equal to
# > greater than
# < less than

age = 25
age = int( input( "Please enter your age:"))
if age < 0:
    print ("Error! This is an invalid age!")
elif age < 18:
    print ("You are under 18!")
#if age >= 18:
#    if age < 21:
#        print ("You are between 18 and 21 years of age! Enjoy it!")
if age < 21:
    if age >= 18:
        print ("You are between 18 and 21 years of age! Enjoy it!")
        print ("You can vote! And purchase cigarettes!")
        print ("And pay more taxes than before!\nAnd go to prison!")
        print ("Welcome to adulthood in America!")
if age >=21 and age < 122:
    print ("You can now buy alcohol! Congratulations on making it this far!")
if age >= 122:
    print ("You're breaking records! Keep at it! (Also, what's your secret?)")
