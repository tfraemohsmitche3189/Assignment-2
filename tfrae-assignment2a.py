# Project name: Assignment 2a "Arnold's Amazing Eats"
# Author: Talea Fraemohs-Mitchell
# Date created: 06-08-25
# Last edited: 06-08-25

# Display welcome screen here, explain how to use program
from ast import While


print("Welcome to Arnold's Amazing Eats!\nThis program is used to order from our menu quickly and easily. Simply enter your information at each prompt, or press the corresponding number when given a menu. You will have a chance to confirm your information at the end before ordering.")

# Get the following information (Display prompts, recieve input). Don't sanitize these inputs.
print("Please fill out the following information. A log in feature to save information is coming soon.")
# First name
firstName = input("First name: ").strip()
# Last name
lastName = input("Last name: ").strip()
# Street address
streetAddress = input("FULL Street address (Please include unit or building number, if applicable): ").strip()
# City
cityAddress = input("City: ").strip()
# Province
provinceAddress = input("Province: ").strip()
# Postal Code
postalAddress = input("Postal Code: ").strip()
# Phone number
contactNumber = input("Phone number (We may reach out to you if there is an issue with your order): ").strip()
# Special instructions for delivery
specialInstructions = input("Any special instructions for delivery? (If not, simply press Enter) ").strip()

# # Testing to make sure the inputs are functioning as intended. Debug feature, not part of the final product
# print("Your name is ", firstName, lastName, ".")
# print("You live at ", streetAddress, ", ", cityAddress, ", ", provinceAddress, ", ", postalAddress, ".")
# print("Your phone number is ", contactNumber, ".")
# print("Special instructions: ", specialInstructions) 

# Menu: 2 options available, item and price
menuChoice = 3
menuOrder = ""
menuPrice = 0
totalPrice = 0
while menuChoice > 2:
    menuChoice = int(input("Please select from the following menu:\n1. Chicken Alfredo ($18)\n2. Spaghetti and Garlic Bread ($16.50) "))
    if menuChoice == 1:
        menuOrder = "Chicken Alfredo"
        menuPrice = float(18)
    elif menuChoice == 2:
        menuOrder = "Spaghetti and Garlic Bread"
        menuPrice = 16.5
    else:
        print("I'm sorry, that is an invalid input. Please answer 1 or 2.")

# How many?
menuAmount = int(input("How many orders would you like? "))
totalPrice = menuPrice * menuAmount

# Print order confirmation, require Y/N in a loop (sanitize this input)
userConfirm = input("You would like {0} orders of {1}? ".format(menuAmount, menuOrder)).upper()
while userConfirm != "Y" and userConfirm != "N":
    userConfirm = input("Please confirm Y/N: ").upper()
    if userConfirm != "Y" and userConfirm != "N":
        print("Invalid input.")

# Ask if student Y/N (sanitize this input) and if so apply 10% discount
userStudent = input("Are you a student? ").upper()
while userStudent != "Y" and userStudent != "N":
    print("Invalid input.")
    userStudent = input("Are you a student? ").upper()

# Print recipt including: Food ordered, quantity, price, student discount if applicable, sales tax
# This took longer than the entire rest of the assignment combined
print("{0:^20s} {1:^20s} {2:^20s} {3:^20s}".format('Order', 'Amt', 'Price', 'Total'))
print("{0:_^80s}".format('_'))
print("{0:^20s} {1:^20d} {2:^20.2f} {3:^20.2f}".format(menuOrder, menuAmount, menuPrice, totalPrice))
# You know, this is kind of a bad discount. It doesn't even cover the sales tax. Who greenlit this?
studentDiscount = 1.0
if userStudent == "Y":
    studentDiscount = totalPrice * .1
    totalPrice = totalPrice - studentDiscount
    print("{0:^20s} {1:^20s} {2:^20.2%} {3:^20.2f}".format('Student Discount', ' ', studentDiscount * .01, totalPrice))
# Add sales tax 13%. Yes it's absurd that I multiply something by .01 in order to format it as a % but this is what works 
# and I'm afraid of fiddling with it more and breaking everything
salesTax = totalPrice * .13
totalPrice = totalPrice + salesTax
print("{0:^20s} {1:^20s} {2:^20.2%} {3:^20.2f}".format('Sales Tax', '', salesTax * .01, totalPrice))