from models.Contact import Contact


def mainMenuInput() -> str:
    print("1. List Contacts")
    print("2. Add Contact")
    print("3. Remove Contact")
    print("4. Sort Contacts By Name")
    print("5. Exit\n")

    result = input("Option: ")
    return result


def removeMenuInput() -> str:
    print("1. Remove by Name")
    print("2. Remove by Phone Number")
    print("3. Remove by Email\n")

    result = input("Option: ")
    return result


def printContacts(contacts: list[Contact]):
    for contact in contacts:
        contact.printModel()
        print()
