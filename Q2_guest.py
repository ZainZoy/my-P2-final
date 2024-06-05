from Q2_user import *
from Q2_booking import *


class Guest(User):
    def __init__(self, name, contact, User_ID, properties_booked: list):
        super().__init__(name, contact, User_ID)
        self.bookings = properties_booked

    def book_property(self, property, check_in_date, check_out_date):
        if property.availability_status:
            booking = Booking(self, property, check_in_date, check_out_date)
            self.bookings.append(booking)
            property.update_availability(False)
            return booking
        else:
            print("Property is not available for booking.")
