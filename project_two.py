import datetime
from random import randint
import random

users_information = []
self_pickup_choices = []
self_pickup_drink_choices = []
dine_in_choices = []
dine_in_drink_choices = []
self_pickup_order = {}
dine_in_order = {}

def signup():
    full_name = input("Please enter your name: ")
    contact_number = input("Pleaase enter your mobile number : ")
    address = input("Please enter your address or press enter to Skip: ")
    date_of_birth = input("Please Enter Your Date of Birth # DD/MM/YYYY (No Space): ")
    password = input("Please enter your password: ")
    confirm_password = input("Confirm your password: ")

    for data in users_information:
        if (data['number'] == contact_number):
            print('Please User with Mobile Number {} already exists'.format(contact_number))
            print('Sign in instead')
            signin()
    
    if (validate_dob(date_of_birth)):
        if (age_eligibility(date_of_birth) >= 21):
            if (mobile_check(contact_number)):
                if (password_check(password)):
                    if confirm_password == password:
                        user_info = {
                            "name": full_name,
                            "number": contact_number,
                            'dob': date_of_birth,
                            "password": password
                        }
                        user_info_with_address = {
                            "name": full_name,
                            "number": contact_number,
                            'dob': date_of_birth,
                            "password": password,
                            "address": address
                        }
                        if not address:
                            users_information.append(user_info)
                        else:
                            users_information.append(user_info_with_address)
                        
                        print(users_information)
                        print("||||||||||")
                        print("||||||||||")
                        print("||||||||||")
                        print("||||||||||")
                        print("You have successfully signed up!")
                        # print(users_information)
                    else:
                        print("||||||||||")
                        print("||||||||||")
                        print("||||||||||")
                        print("||||||||||")
                        print("Your passwords are not matching")
                        print("Please start again:")
                        signup()
                else:
                    print("||||||||||")
                    print("||||||||||")
                    print("||||||||||")
                    print("||||||||||")
                    print("Password must begin with alphabets followed by either one of @, & and ends with numbers (For Example: Sam@0125, Sam&25)")
                    print("Please start again")
                    signup()
            else:
                print("||||||||||")
                print("||||||||||")
                print("||||||||||")
                print("||||||||||")
                print("Mobile Numbers must all be numbers and must be 10 digits and starts with 0")
                print("Please start again")
                signup()
        else:
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("You must be at least 21 years old to be able to signup")
            print("Please start again")
            signup()
    else:
        print("||||||||||")
        print("||||||||||")
        print("||||||||||")
        print("||||||||||")
        print("You have entered the Date of Birth in Invalid format")
        print("Please start again")
        signup()

def signin():
    number = input("Please enter your Username (Mobile Number): ")
    password = input("please enter your password: ")
    print(users_information)

    if (len(users_information) == 0):
        print("||||||||||")
        print("||||||||||")
        print("||||||||||")
        print("||||||||||")
        print("You have not signed up with this Contact Number, Please sign up first.")
        signup()
        return
    
    for data in users_information:
        if (mobile_check(number)):
            if (data['number'] != number and data['password'] != password):
                print("||||||||||")
                print("||||||||||")
                print("||||||||||")
                print("||||||||||")
                print("You have not signed up with this Contact Number, Please sign up first.")
                signup()
                return
            elif (data['number'] != number and data['password'] == password):
                print("||||||||||")
                print("||||||||||")
                print("||||||||||")
                print("||||||||||")
                print("You have entered incorrect username")
                print("Please try again")
                signin()
            elif (data['number'] == number):
                for k, v in data.items():
                    if (k == "password" and v != password):
                        print("||||||||||")
                        print("||||||||||")
                        print("||||||||||")
                        print("||||||||||")
                        print("You have entered the wrong Password")
                        print("Please try again")
                        signin()
                        
        else:
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("Mobile Numbers must all be numbers and must be 10 digits and starts with 0")
            print("Please start again")
            signin()

    for data in users_information:
        if (data['number'] == number and data['password'] == password):
            for k, v in data.items():
                if (k == "password" and v == password):
                    print("||||||||||")
                    print("||||||||||") 
                    print("||||||||||")
                    print("||||||||||")
                    print("You have successfully signed in")
                    print("Welcome " + data['name'])
                    postlogin()

def postlogin():
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    while 1:
        print("Please enter 2.1 to Start Ordering.")
        print("Please enter 2.2 to Print Statistics.")
        print("Please enter 2.3 for Logout.")

        character = float(input("Enter your choice: "))
        if character == 2.1:
            post_ordering_page()
        elif character == 2.2:
            statistics()
        elif character == 2.3:
            exit_program()
            break
        else:
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("You have entered wrong choice.")
            postlogin()
                     
def post_ordering_page():
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    while 1:
        print("Please enter 1 for Dine in")
        print("Please enter 2 for Order Online.")
        print("Please enter 3 for Login Page")

        character = int(input("Enter your choice: "))
        if character == 1:
            dine_in()
        elif character == 2:
            order_online()
        elif character == 3:
            signin()
        else:
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("You have entered wrong choice.")
            post_ordering_page()

def dine_in():
    general_option()
    while 1:
        character = int(input("Enter your choice: "))
        if character == 1:
            dine_in_choices.append(1)
            print("The pick up choices", dine_in_choices)
            options()
        elif character == 2:
            dine_in_choices.append(2)
            print("The pick up choices", dine_in_choices)
            options()
        elif character == 3:
            dine_in_choices.append(3)
            print("The pick up choices", dine_in_choices)
            options()
        elif character == 4:
            dine_in_choices.append(4)
            print("The pick up choices", dine_in_choices)
            options()
        elif character == 5:
            dine_in_choices.append(5)
            print("The pick up choices", dine_in_choices)
            options()
        elif character == 6:
            dine_in_choices.append(6)
            print("The pick up choices", dine_in_choices)
            options()
        elif character == 7:
            dine_in_drinks_menu()
        else:
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("You have entered wrong choice.")
            self_pickup()

def order_online():
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    while 1:
        print("Enter 1 for Self Pickup")
        print("Enter 2 for Home Delivery.")
        print("Enter 3 to go to Previous Menu.")

        character = int(input("Enter your choice: "))
        if character == 1:
            self_pickup()
        elif character == 2:
            home_delivery()
        elif character == 3:
            post_ordering_page()
        else:
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("You have entered wrong choice.")
            order_online()

def self_pickup():
    general_option()

    while 1:
        character = int(input("Enter your choice: "))
        if character == 1:
            self_pickup_choices.append(1)
            print("The pick up choices", self_pickup_choices)
            options()
        elif character == 2:
            self_pickup_choices.append(2)
            print("The pick up choices", self_pickup_choices)
            options()
        elif character == 3:
            self_pickup_choices.append(3)
            print("The pick up choices", self_pickup_choices)
            options()
        elif character == 4:
            self_pickup_choices.append(4)
            print("The pick up choices", self_pickup_choices)
            options()
        elif character == 5:
            self_pickup_choices.append(5)
            print("The pick up choices", self_pickup_choices)
            options()
        elif character == 6:
            self_pickup_choices.append(6)
            print("The pick up choices", self_pickup_choices)
            options()
        elif character == 7:
            drinks_menu()
        else:
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("You have entered wrong choice.")
            self_pickup()

def drinks_menu():
    pickup_drink_options()

    while 1:
        character = int(input("Enter your choice: "))
        if character == 1:
            self_pickup_drink_choices.append(1)
            print("The pick up drink choices", self_pickup_drink_choices)
            pickup_drink_options()
        elif character == 2:
            self_pickup_drink_choices.append(2)
            print("The pick up drink choices", self_pickup_drink_choices)
            pickup_drink_options()
        elif character == 3:
            self_pickup_drink_choices.append(3)
            print("The pick up drink choices", self_pickup_drink_choices)
            pickup_drink_options()
        elif character == 4:
            pick_up_checkout()
        else:
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("You have entered wrong choice.")
            drinks_menu()

def dine_in_drinks_menu():
    pickup_drink_options()
    while 1:
        character = int(input("Enter your choice: "))
        if character == 1:
            dine_in_drink_choices.append(1)
            print("The pick up drink choices", dine_in_drink_choices)
            pickup_drink_options()
        elif character == 2:
            dine_in_drink_choices.append(2)
            print("The pick up drink choices", dine_in_drink_choices)
            pickup_drink_options()
        elif character == 3:
            dine_in_drink_choices.append(3)
            print("The pick up drink choices", dine_in_drink_choices)
            pickup_drink_options()
        elif character == 4:
            dine_in_checkout()
        else:
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("You have entered wrong choice.")
            drinks_menu()

def pickup_drink_options():
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    print("Enter 1 for Coffee Price AUD 2")
    print("Enter 2 for Colddrink Price AUD 4")
    print("Enter 3 for Shake Price AUD 6")
    print("Enter 4 for Checkout")

def pick_up_checkout():
    total_amount = 0
    order_id = guess_letter() + str(random_with_N_digits(3))
    type_of_order = "Self Pickup"
    self_pickup_order["order_id"] = order_id
    self_pickup_order["type_of_order"] = type_of_order

    for number in self_pickup_choices:
        if (number == 1):
            total_amount += 2
        elif (number == 2):
            total_amount += 4
        elif (number == 3):
            total_amount += 6
        elif (number == 4):
            total_amount += 8
        elif (number == 5):
            total_amount += 10
        elif (number == 6):
            total_amount += 20
        else: 
            total_amount += 0
    
    for number in self_pickup_drink_choices:
        if (number == 1):
            total_amount += 2
        elif (number == 2):
            total_amount += 4
        elif (number == 3):
            total_amount += 6
        else:
            total_amount += 0
    
    self_pickup_order["total_amount"] = total_amount
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    print("Please Enter Y to proceed to Checkout or Enter N to cancel the order:")

    while 1:
        letter = input("Enter your choice: ")
        if (letter == "Y" or letter == "y"):
            proceed_to_pickup_checkout()
        elif (letter == "N" or letter =="n"):
            postlogin()
        else:
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("You have entered wrong choice.")
            pick_up_checkout()

def dine_in_checkout():
    total_amount = 0
    order_id = guess_letter() + str(random_with_N_digits(3))
    type_of_order = "Dine In"
    dine_in_order["order_id"] = order_id
    dine_in_order["type_of_order"] = type_of_order

    for number in dine_in_choices:
        if (number == 1):
            total_amount += 2
        elif (number == 2):
            total_amount += 4
        elif (number == 3):
            total_amount += 6
        elif (number == 4):
            total_amount += 8
        elif (number == 5):
            total_amount += 10
        elif (number == 6):
            total_amount += 20
        else: 
            total_amount += 0
    
    for number in dine_in_drink_choices:
        if (number == 1):
            total_amount += 2
        elif (number == 2):
            total_amount += 4
        elif (number == 3):
            total_amount += 6
        else:
            total_amount += 0
    
    dine_in_order["total_amount"] = total_amount
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    print("Please Enter Y to proceed to Checkout or Enter N to cancel the order:")

    while 1:
        letter = input("Enter your choice: ")
        if (letter == "Y" or letter == "y"):
            proceed_to_dine_in_checkout()
        elif (letter == "N" or letter =="n"):
            postlogin()
        else:
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("You have entered wrong choice.")
            dine_in_checkout()
        

def proceed_to_pickup_checkout():
    date = input("Please enter the Date of Pickup DD/MM/YYYY: ")
    time = input("Please enter the Time of Pickup HH:MM")
    name = input("Please enter the Name of Person picking up: ")

    self_pickup_order["date"] = date
    self_pickup_order["time"] = time
    self_pickup_order["name"] = name

    # print(self_pickup_order)
    confirmation = "Thank you for entering the details, Your Booking is confirmed."
    result = "Your total payable amount is: {}".format(self_pickup_order["total_amount"])
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    print(result)
    print(confirmation)
    postlogin()

def proceed_to_dine_in_checkout():
    date = input("Please enter the Date of Booking for Dine in: ")
    time = input("Please enter the Time of Booking for Dine in: ")
    num_of_persons = input("Please enter the number of Persons: ")

    dine_in_order["date"] = date
    dine_in_order["time"] = time
    dine_in_order["num_of_persons"] = num_of_persons

    fiften_percent_increase = (dine_in_order["total_amount"] / 100) * 15
    # print(dine_in_order)
    confirmation = "Thank you for entering the details, Your Booking is confirmed."
    result = "Your total payable amount is: {} including AUD {} for Service Charges".format(dine_in_order["total_amount"], fiften_percent_increase)
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    print(result)
    print(confirmation)
    postlogin()

    
def home_delivery():
    print("the home delivery")

def statistics():
    print("the statistics")

def general_option():
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    print("ID\tName\t\tPrice")
    print("1\tNoodles\t\tAUD 2")
    print("2\tSandwich\tAUD 4")
    print("3\tDumpling\tAUD 6")
    print("4\tMuffins\t\tAUD 8")
    print("5\tPasta\t\tAUD 10")
    print("6\tPizza\t\tAUD 20")
    options()

def options():
    print("Enter 1 for Noodles Price AUD 2")
    print("Enter 2 for Sandwich Price AUD 4")
    print("Enter 3 for Dumpling Price AUD 6")
    print("Enter 4 for Muffins Price AUD 8")
    print("Enter 5 for Pasta Price AUD 10")
    print("Enter 6 for Pizza Price AUD 20")
    print("Enter 7 for Drinks Menu")

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def guess_letter():
    return random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def validate_dob(date):
    format = "%d/%m/%Y"

    # check if format matches the date
    res = True
    
    try:
        res = bool(datetime.datetime.strptime(date, format))
    except ValueError:
        res = False
    
    return res

def mobile_check(number):
    numbers = "0123456789"
    val = True
    for num in number:
        if num not in numbers:
            val = False
        
    if (len(number) != 10 and number[0] != 0):
        val = False
            
    return val

def age_eligibility(date_of_birth):
    today = datetime.date.today()

    year = today.strftime("%Y")
    return int(year) - int(date_of_birth[-4:])

def password_check(password):
    specialSym = ['@', '&']
    val = True

    characters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"

    if not any(password.lower().startswith(char) for char in characters):
        val = False
    
    if not any(password.endswith(num) for num in numbers):
        val = False
    
    if not any(char in specialSym for char in password):
        val = False
    
    return val

def exit_program():
    print("Thank you for using this application")
    return

while 1:
    print("*********** Mobile Ordering System (Registration System) **********")
    print("Please Enter 1 for Sign up.")
    print("Please Enter 2 for Sign in.")
    print("Please Enter 3 for Quit")
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")
    print("||||||||||")

    character = int(input("Enter your choice: "))
    if character == 1:
        signup()
    elif character == 2:
        signin()
    elif character == 3:
        exit_program()
        break
    else:
        print("You have entered wrong choice.")