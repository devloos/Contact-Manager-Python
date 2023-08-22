import json
import sys
import utils
from models.Database import Database
from models.Options import MainOption
from models.Options import RemoveOption
from models.Contact import Contact


REMOVE_OPTION_MAPPING = {
    RemoveOption.Name: {
        "label": "Name: ",
        "column": "Name",
    },
    RemoveOption.PhoneNumber: {"label": "Phone Number: ", "column": "Phone Number"},
    RemoveOption.Email: {"label": "Email: ", "column": "Email"},
}


def removeMenu(db: Database):
    while True:
        try:
            userInput = int(utils.removeMenuInput())
            option = RemoveOption(userInput)
        except ValueError:
            print("Invalid option try again!\n")
            continue

        removeInput = input(REMOVE_OPTION_MAPPING[option]["label"])

        result = db.removeContact(removeInput, REMOVE_OPTION_MAPPING[option]["column"])

        if result == None:
            print("No user found!")
        else:
            print(result)

        print()
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
        print()
        removeMenu(db)

    else:
        break

file.close()
