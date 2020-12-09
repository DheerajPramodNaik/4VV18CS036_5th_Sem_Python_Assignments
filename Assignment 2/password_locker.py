import sys
import pyperclip

users = {'DHEERAJ':'dheeraj123', 'AVANISH':'avanish123'}

passwords = {'gmail':'vvce@123', 'blog':'blog@456', 'luggage':'54321'}

user = input("Enter the Username :\n")
print()
if user.upper() in users:
    password = input("Enter the Password of the Program :\n")
    print()
    if password != users[user.upper()]:
        print("Wrong Password : Access Denied")
        sys.exit()
    else:
        print("Access Granted...\n")
        print("***Available Passwords***")
        print("-------------------------")
        for i in passwords.keys():
            print("\t"+i+"\n")
        choice = input("\nEnter Your Choice :\n")
        if choice in passwords:
            pyperclip.copy(passwords[choice])
            print("\nYour Password for "+ choice + " has been copied to the Clipboard")
        else:
            print("\nNo such Account is found in storage")
            sys.exit()
else:
    print("Invalid User")