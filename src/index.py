import json
import sys

filename = "config.json"

try:
    file = open(filename)
    obj = dict(json.load(file))

    if "user" not in obj.keys():
        raise ValueError()
    elif "password" not in obj.keys():
        raise ValueError()
except (IOError, ValueError):
    print("Missing|Incorrect config.json file.")
    print("Example config:")
    print(json.dumps({"user": "xxxx", "password": "xxxxxxxxxx"}, indent=4))
    sys.exit(1)

print(f"Hey {obj['user']}!\n")

passwordIncorrect = True

while passwordIncorrect:
    password = input("Please enter password: ")

    if obj["password"] != password:
        print("Wrong password try again!\n")
    else:
        passwordIncorrect = False


file.close()
