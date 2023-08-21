import pandas as pd
from Contact import Contact


class Database:
    def __init__(self) -> None:
        pass

    def readCSV(self) -> [Contact]:
        contacts = [Contact]
        df = pd.read_csv("index.csv")

        for index in df.index:
            contact = Contact()
            contact.setName(df["Name"][index])
            contact.setPhoneNumber(df["Phone Number"][index])
            contact.setEmail(df["Email"][index])
            contact.setRelationship(df["Relationship"][index])
            contacts.append(contact)

        return contacts
