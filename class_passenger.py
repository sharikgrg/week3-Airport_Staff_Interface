from class_flight import *
class Passenger():
    def __init__(self, f_name, l_name, phnnumber, email, passportNO):
        self.f_name = f_name
        self.l_name = l_name
        self.phonenumber = phnnumber
        self.email = email
        self.passportNO = passportNO


    def name(self):
        return self.f_name + ' ' + self.l_name + ', ' + self.passportNO

    def pass_details(self):
        return self.f_name + ' ' + self.l_name + ', '  + self.passportNO + ', ' + self.phonenumber + ', ' + self.email
    def passlist(self):
        return