import json
import sys
import utils
from models.Database import Database
from models.Options import MainOption
from models.Options import RemoveOption
from models.Contact import Contact


def removeMenu(db: Database):
    while True:
        try:
            userInput = int(utils.removeMenuInput())
            option = RemoveOption(userInput)
        except ValueError:
            print("Invalid option try again!\n")
            continue

        column = ""
        inputLabel = ""
        if option == RemoveOption.Name:
            inputLabel = "Phone Number: "
            column = "Name"
        elif option == RemoveOption.Email:
            inputLabel = "Email: "
            column = "Email"
        else:
            inputLabel = "Phone Number: "
            column = "Phone Number"

        removeInput = input(inputLabel)

        result = db.removeContact(removeInput, column)

        if result == None:
            print("No user found!")
        else:
            print(result)

        break


filename = "config.json"

try:
    file = open(filename)

    # result -> dict
    obj = dict(json.load(file))

    # validating needed keys are in dict
    if "user" not in obj.keys():
        raise ValueError()
    elif "password" not in obj.keys():
        raise ValueError()
except (IOError, ValueError):
    # fatal error give example config and exit
    print("Missing|Incorrect config.json file.")
    print("Example config:")
    print(json.dumps({"user": "xxxx", "password": "xxxxxxxxxx"}, indent=4))
    sys.exit(1)

print(f"Hey {obj['user']}!\n")

wrongPassword = True

# repeat until correct password
while wrongPassword:
    password = input("Please enter password: ")

    if obj["password"] != password:
        print("Wrong password try again!\n")
    else:
        wrongPassword = False

db = Database()

print()

while True:
    try:
        userInput = int(utils.mainMenuInput())
        option = MainOption(userInput)
    except ValueError:
        print("Invalid option try again!\n")
        continue

    if option == MainOption.List:
        utils.printContacts(db.getContacts())

    elif option == MainOption.Add:
        contact = Contact()
        contact.setName(input("Name: "))
        contact.setPhoneNumber(input("Phone Number: "))
        contact.setEmail(input("Email: "))
        contact.setRelationship(input("Relationship: "))
        db.addContact(contact)

    elif option == MainOption.Remove:
        removeMenu()

    else:
        break

file.close()
