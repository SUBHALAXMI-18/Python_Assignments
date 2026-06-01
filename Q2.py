# Login System

correct_username = "SUBHALAXMI-18"
correct_password = "623636"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login Successful!")

elif username != correct_username:
    print("Invalid Username!")

elif password != correct_password:
    print("Invalid Password!")