from class_flight import *
class Passenger(Flight):
    def __init__(self, destination, origin, flight_number, departure, arrivals, f_name, l_name, customerID, phnnumber, email, passportNO):
        super().__init__( destination, origin, flight_number, departure, arrivals)
        self.f_name = f_name
        self.l_name = l_name
        self.customerID = customerID
        self.phonenumber = phnnumber
        self.email = email
        self.passportNO = passportNO

    def create_passenger(self, f_name, l_name, email, phnnumber, passportNO):
        return f_name + l_name + email + phnnumber + passportNO