from models.Contact import Contact


def mainMenuInput() -> str:
    print("1. List Contacts")
    print("2. Add Contact")
    print("3. Remove Contact")
    print("4. Exit\n")

    result = input("Option: ")
    return result


def removeMenuInput() -> str:
    print("1. Remove by name")
    print("2. Remove by phone number")
    print("3. Remove by email\n")

    result = input("Option: ")
    return result


def printContacts(contacts: list[Contact]):
    for contact in contacts:
        contact.printContent()
        print()
