import json
import sys
from models.Database import Database

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

passwordIncorrect = True

# repeat until correct password
while passwordIncorrect:
    password = input("Please enter password: ")

    if obj["password"] != password:
        print("Wrong password try again!\n")
    else:
        passwordIncorrect = False

db = Database()

contacts = db.readCSV()

print(contacts)

file.close()
