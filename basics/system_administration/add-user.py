import os

#adding users
def new_user():
    confirm = "N"
    while confirm != "Y":
        username =input("Enter the name of the user to add: ")
        print("Use the username '"  + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo adduser " + username)

        
#removing users