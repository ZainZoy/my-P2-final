

class Property:
    def __init__(self,property_ID,name,location,description,price_per_night):
        self.ID = property_ID
        self.name = name
        self.location = location
        self.descp = description
        self.price = price_per_night
        self.availability_status = True

    def update_availability(self, availability_status):
            self.availability_status = availability_status

