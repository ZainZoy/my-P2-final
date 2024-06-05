from Q2_user import *
from Q2 import *


class Host(User):
    def __init__(self, name, contact, User_ID, properties_owned: list):
        super().__init__(name, contact, User_ID)
        self.ID = User_ID
        self.pro_owned = properties_owned

    def add_property(self,ID, name, location, descp, price):
        # ID = input("enter property ID: ")
        # name = input("enter property name: ")
        # location = input("enter location of property: ")
        # descp = input("enter description of property: ")
        # price = input("enter the price per night of this property: ")
        # avail = input("enter the availibility status (yes/no): ")
        self.pro_owned.append(Property(ID, name, location, descp, price))

    def remove_property(self, ID):
        if ID in self.pro_owned:
            self.pro_owned.pop(ID.index())

    def display_properties(self):
        for i in self.pro_owned:
            print(i.ID,i.name,i.location,i.descp,i.price)



