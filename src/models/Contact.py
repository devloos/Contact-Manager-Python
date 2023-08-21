from Relationship import Relationship


class Contact:
    name: str
    phoneNumber: str
    email: str
    relationship: Relationship

    def __init__(self) -> None:
        pass

    def setName(self, name: str) -> None:
        self.name = name

    def getName(self) -> str:
        return self.name

    def setPhoneNumber(self, phoneNumber: str) -> None:
        self.phoneNumber = phoneNumber

    def getPhoneNumber(self) -> str:
        return self.phoneNumber

    def setEmail(self, email: str) -> None:
        self.email = email

    def getEmail(self) -> str:
        return self.email

    def setRelationship(self, relationship: Relationship) -> None:
        self.relationship = relationship

    def getRelationship(self) -> Relationship:
        return self.relationship
