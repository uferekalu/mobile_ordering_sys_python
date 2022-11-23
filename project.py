import datetime

users_information = []

def signup():
    full_name = input("Enter your full name: ")
    contact_number = input("Enter your contact number: ")
    date_of_birth = input("Enter Your Date of Birth # DD/MM/YYYY (No Space): ")
    password = input("Enter your password: ")
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
                        users_information.append(user_info)
                        print("||||||||||")
                        print("||||||||||")
                        print("||||||||||")
                        print("||||||||||")
                        print("You have successfully signed up!")
                        # print(users_information)
                    else:
                        print("Your passwords are not matching")
                        print("Please start again:")
                        signup()
                else:
                    print("Password must begin with alphabets followed by either one of @, & and ends with numbers (For Example: Sam@0125, Sam&25)")
                    print("Please start again")
                    signup()
            else:
                print("Mobile Numbers must all be numbers and must be 10 digits and starts with 0")
                print("Please start again")
                signup()
        else:
            print("You must be at least 21 years old to be able to signup")
            print("Please start again")
            signup()
    else:
        print("You have entered the Date of Birth in Invalid format")
        print("Please start again")
        signup()


def signin():
    number = input("Please enter your Username (Mobile Number): ")
    password = input("please enter your password: ")
    # print(users_information)

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
        else:
            print("Mobile Numbers must all be numbers and must be 10 digits and starts with 0")
            print("Please start again")
            signin()
    
    for data in users_information:
        if (mobile_check(number)):
            if (data['number'] != number and data['password'] == password):
                print("||||||||||")
                print("||||||||||")
                print("||||||||||")
                print("||||||||||")
                print("You have entered incorrect username")
                print("Please try again")
                signin()
        else:
            print("Mobile Numbers must all be numbers and must be 10 digits and starts with 0")
            print("Please start again")
            signin()

    
    for data in users_information:
        if (data['number'] == number):
            for k, v in data.items():
                if (k == "password" and v != password):
                    print("||||||||||")
                    print("||||||||||")
                    print("||||||||||")
                    print("||||||||||")
                    print("You have entered the wrong Password")
                    print("Please try again")
                    signin()
    
    for data in users_information:
        if (data['number'] == number):
            for k, v in data.items():
                if (k == "password" and v == password):
                    print("||||||||||")
                    print("||||||||||") 
                    print("||||||||||")
                    print("||||||||||")
                    print("You have successfully signed in")
                    print("Welcome " + data['name'])
                    password_reset_or_signout()        

                                
def password_reset_or_signout():
    while 1:
        print("Please enter 1 for Resetting the password.")
        print("Please enter 2 for Signout.")

        character = int(input("Enter your choice: "))
        if character == 1:
            reset_password()
        elif character == 2:
            exit_program()
            break
        else:
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("You have entered wrong choice.")
            password_reset_or_signout()

def reset_password():
    number = input("Please enter your Username (Mobile Number): ")
    password = input("Please enter your old password: ")
    new_password = input("please enter your new password: ")

    for data in users_information:
        if (data['number'] != number):
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("You have entered wrong Username")
            print("Please try again")
            reset_password()

    for data in users_information:
        if (data['password'] != password):
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("You have entered wrong old password")
            print("Please try again")
            reset_password()
    
    for data in users_information:
        if (data['password'] == new_password):
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("You cannot use the password used earlier")
            reset_password()
    
    if (password_check(new_password)):
        for data in users_information:
            data['password'] = new_password
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("||||||||||")
            print("Your password has been reset successfully!")
    else:
        print("||||||||||")
        print("||||||||||")
        print("||||||||||")
        print("||||||||||")
        print("Password must begin with alphabets followed by either one of @, & and ends with numbers (For Example: Sam@0125, Sam&25)")
        password_reset_or_signout()
        

def validate_dob(date):
    format = "%d/%m/%Y"

    # check if format matches the date
    res = True
    
    try:
        res = bool(datetime.datetime.strptime(date, format))
    except ValueError:
        res = False
    
    return res

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
        