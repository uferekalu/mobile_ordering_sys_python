import datetime

users_information = []

def signup():
    full_name = input("Enter your full name: ")
    contact_number = input("Enter your contact number: ")
    date_of_birth = input("Enter Your Date of Birth # DD/MM/YYYY (No Space): ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    if (len(users_information) != 0):
        if (data['number'] == contact_number for data in users_information):
            print('Please User with Mobile Number {} already exists'.format(contact_number))
            print('Sign in instead')
            signin()         
    else:
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
                            print("You have successfully signed up!")
                            print(users_information)
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
    print(users_information)

    if (len(users_information) == 0):
        print("Please the user with Mobile Number " + number + " does not exist")
        print("Sign up instead")
        signup()
    else:
        for data in users_information:
            if (data['number'] == number):
                for k, v in data.items():
                    # print(k, v)
                    if (k == "password" and v == password):
                        print("You have successfully signed in")
                        print("Welcome " + data['name'])
                        password_reset_or_signout()
                    
                    if (k == "password" and v != password):
                        print("You have entered the wrong Password")
                        print("Please try again")
                        signin()
            else:
                print("You have entered incorrect username")
                print("Please try again")
                signin()
                                


    # with open("users_information.txt", "r") as f:
    #     stored_name, stored_number, stored_dob, stored_pass = f.read().split("\n")
    # f.close()

    # if number == stored_number and password == stored_pass:
        # print("You have successfully signed in")
        # print("Welcome " + stored_name)
        # password_reset_or_signout()
    # else:
        # print("You have entered the wrong Password or incorrect username")
        # print("Please try again")
    #     i = 0
    #     while (i < 2):
    #         signin()
    #         i += 1
    #     print("You have used the maximum attempts of Login:")
    #     print("Please reset the password by entering the below details:")
    #     password_reset_or_signout()

def password_reset_or_signout():
    print("Please enter 1 for Resetting the password.")
    print("Please enter 2 for Signout.")

    character = int(input("Enter your choice: "))
    if character == 1:
        reset_password()
    elif character == 2:
        exit_program()
    else:
        print("You have entered wrong choice.")
        password_reset_or_signout()

def reset_password():
    number = input("Please enter your Username (Mobile Number): ")
    password = input("Please enter your old password: ")
    new_password = input("please enter your new password: ")

    with open("users_information.txt", "r") as f:
        stored_name, stored_number, stored_dob, stored_pass = f.read().split("\n")
    f.close()

    if password != stored_pass:
        print("Wrong password")
        reset_password()
    
    if number == stored_number:
        with open("users_information.txt", "w") as f:
            f.write(stored_name + "\n")
            f.write(stored_number + "\n")
            f.write(stored_dob + "\n")
            f.write(new_password)
        f.close()
        print("Your password has been reset successfully!")
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
        