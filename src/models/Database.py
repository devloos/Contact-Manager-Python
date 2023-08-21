import pandas as pd
from pandas import DataFrame
from .Contact import Contact


class Database:
    contacts: list[Contact] = []
    df: DataFrame

    def __init__(self) -> None:
        self.df = pd.read_csv("index.csv")

        for index in self.df.index:
            contact = Contact()
            contact.setName(self.df["Name"][index])
            contact.setPhoneNumber(self.df["Phone Number"][index])
            contact.setEmail(self.df["Email"][index])
            contact.setRelationship(self.df["Relationship"][index])
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

    def removeContact(self, removeInput: str, column: str):
        self.df.loc[self.df[column] == removeInput]
