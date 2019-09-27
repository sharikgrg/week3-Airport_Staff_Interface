from class_flight import *
from class_passenger import *
from class_plane import *

print('///////////////Flight Test/////////////////////////')
flight = Flight('KTM', 'LHR', 'LHX002', '18:00', '06:00')
flight1 = Flight('DOH', 'LHR', 'LHX001', '14:00', '17:00')

# destination, origin, flight_number, departure, arrivals
print(flight.add('vinu', 'siva', 'siva@vinu.com'))
print(f'flight from {flight.destination}, flight to {flight.origin}') # check if the parameters are working


print('///////////////Passenger Test/////////////////////////')
passenger = Passenger('KTM', 'LHR', 'LHX002', '18:00', '06:00', 'Sharik', 'Gurung', 1, '775727182', 'sgurung@spartaglobal.com', '66623651')
print(passenger)


print('///////////////Passenger Test/////////////////////////')
plane = Plane('KTM', 'LHR', 'LHX002', '18:00', '06:00', 'Boeing', ['Capt.Morgan', 'CoCapt.lewis', 'Katie'], 'Gas turbine', 114)
print(plane)