# Project name: Assignment 2a "Arnold's Amazing Eats"
# Author: Talea Fraemohs-Mitchell
# Date created: 06-08-25
# Last edited: 06-08-25

# Display welcome screen here, explain how to use program
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
# How many?

# Print order confirmation, require Y/N in a loop (sanitize this input)

# Ask if student (sanitize this input) and if so apply 10% discount

# Add sales tax 13%

# Print recipt including: Food ordered, quantity, price, student discount if applicable, sales tax