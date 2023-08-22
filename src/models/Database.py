import pandas as pd
from pandas import DataFrame
from .Contact import Contact


class Database:
    # Maintaining a copy of contacts since it would be expensive to go through
    # DataFrame and computing it every access
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

    # take contact append it to contacts and update csv
    def addContact(self, contact: Contact):
        self.contacts.append(contact)
        obj = {
            "Name": [contact.getName()],
            "Phone Number": [contact.getPhoneNumber()],
            "Email": [contact.getEmail()],
            "Relationship": [contact.getRelationship()],
        }

        # create new DataFrame and append it to file hence mode="a"
        df = pd.DataFrame(obj)
        df.to_csv("index.csv", mode="a", index=False, header=False)

    # remove contact based on column and input
    def removeContact(self, removeInput: str, column: str) -> str | None:
        # using local DataFrame snapshot to grab rows that passed condition
        localDf = self.df.loc[self.df[column] == removeInput]

        if localDf.empty:
            return None
        else:
            self.df.drop(localDf.index, inplace=True)
            self.df.to_csv("index.csv", index=False)

            # cant use join unfortunately since its under localDf.index
            result = "Dropped "
            for index in localDf.index:
                result += localDf["Name"][index]

            return result + "!"

    def sortByName(self):
        self.contacts.sort(key=lambda el: el.getName())
        self.df = self.df.sort_values(by=["Name"], ascending=True)
        self.df.to_csv("index.csv", index=False)
