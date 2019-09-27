class Flight():
    def __init__(self, destination, origin, flight_number, departure, arrivals):
        self.destination = destination
        self.origin = origin
        self.flight_number = flight_number
        self.departure = departure
        self.arrivals = arrivals

    def delays(self):
        return 'Sorry the flight has been delayed, Please check the information board'

    def gateNO(self):
        return'Gate numbers are displayed on the information boards'

    def add(self,f_name, l_name, email):
        return f_name + ' ' + l_name + ' ' + email
