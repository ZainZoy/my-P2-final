import random
class Booking:
    def __init__(self, property, guest, check_in_date, check_out_date):
        self.booking_id = generate_booking_id()
        self.property = property
        self.guest = guest
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.booking_status = "confirmed"

    def cancel_booking(self):
        self.booking_status = "canceled"
        self.property.update_availability(True)

booking_ID_taken = []
def generate_booking_id():
    temp = random.randint(100000,999999)
    while not temp in booking_ID_taken:
        return temp




