class Flight():
    def __init__(self, destination, origin, flight_number):
        self.destination = destination
        self.origin = origin
        self.flight_number = flight_number
        self.passengerlist = []
        self.planelist = []


    def delays(self):
        return 'Sorry the flight has been delayed, Please check the information board'

    def gateNO(self):
        return'Gate numbers are displayed on the information boards'

    def add_passenger(self,*passenger):
        for passenger in passenger:
            self.passengerlist.append(passenger)




    def flightlist(self):
        list = []
        for passenger in self.passengerlist:
            list.append(passenger.name())
        return f'Flight {self.flight_number} is from {self.origin} to {self.destination} ,' \
            f' passengers on the flight: {list}'
