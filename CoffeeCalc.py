# CoffeeCalc.py
# Dylan House
# 2/3/2016
# An algorithm for determining how much coffee to grind for how many cups to be
# produced.

from fractions import Fraction

coffeeGrounds = 0.0
coffeeCups = 0.0
print ("This program is designed to determine the amount of coffee one needs")
print ("to grind in order to make a certain amount of coffee.")

coffeeCups = float(input( "\nHow many cups of coffee are you trying to brew? "))

coffeeGrounds = coffeeCups / 6

print("\nThank you.\n\nBrew yield:\t\t" + str(coffeeCups) + " cups.\n")
print("Amount of grounds:\t" + str(Fraction(coffeeGrounds)) + " cups.")
print("\tOr:\t\t%.2f" %(coffeeGrounds), "cups.")
