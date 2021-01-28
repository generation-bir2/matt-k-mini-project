import sys
import os

welcome_message_menu = print("Welcome to the App!\n" + "Please select an input: \n")
food_products = ["Tea", "Toast", "Bacon", "Sausage", "Egg", "Coffee", "Beans"]

user_added_food = food_products.append(str(custom_food))

while True:
    menu_selection = print("Input '0' to exit from the app\n" + "Input '1' to display product menu")
    user_input = int(input("Please enter a number: "))
    if user_input == 0:
        print(welcome_message_menu)
    elif user_input == 1:
        print(food_products)
    elif user_input == 3:
        custom_food = input("Please type in your desired food or drink item:")
        print(user_added_food)
        
# needs more work