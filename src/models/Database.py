import pandas as pd
from .Contact import Contact


class Database:
    contacts: list[Contact] = []

    def __init__(self) -> None:
        df = pd.read_csv("index.csv")

        for index in df.index:
            contact = Contact()
            contact.setName(df["Name"][index])
            contact.setPhoneNumber(df["Phone Number"][index])
            contact.setEmail(df["Email"][index])
            contact.setRelationship(df["Relationship"][index])
            self.contacts.append(contact)

    def getContacts(self) -> list[Contact]:
        return self.contacts

    def addContact(self, contact: Contact):
        self.contacts.append(contact)
        obj = {
            "Name": [contact.getName()],
            "Phone Number": [contact.getPhoneNumber()],
            "Email": [contact.getEmail()],
            "Relationship": [contact.getRelationship()],
        }
        df = pd.DataFrame(obj)
        df.to_csv("index.csv", mode="a", index=False, header=False)
