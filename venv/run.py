from class_flight import *
from class_passenger import *
from class_plane import *


flight = Flight('KTM', 'LHR', 'BA5626')
flight1 = Flight('AMS', 'LTN', 'BA5627')
flight2 = Flight('DOH', 'LGW', 'BA5628')

passenger = Passenger('Sharik', 'Gurung', '7555736178', 'sharikgrg@hotmail.com', '33656549')
passenger1 = Passenger('Felipe', 'Paiva', '7977564821', 'fpaiva@hotmail.com', '33654958')
passenger2 = Passenger('David', 'Rai', '75811346972', 'drai@hotmail.com', '34861950')
passenger3 = Passenger('Rory', 'Stokes', '7555738794', 'rstokes@hotmail.com', '33656550')
passenger4 = Passenger('Abror', 'Ilkhamov', '7849761794', 'Abror@hotmail.com', '33654951')
passenger5 = Passenger('Lennox', 'Addo', '7799164862', 'lennox@hotmail.com', '34861952')


flight.add_passenger(passenger, passenger1)
flight1.add_passenger(passenger2,passenger3)
flight2.add_passenger(passenger4, passenger5)

# print('///////////////////////FLIGHT DETAILS////////////////////////////////////')
# for f in (flight, flight1, flight2):
#     print(f.flightlist())
#
# print('/////////////////////////passenger details//////....////////////////////')
# for p in (passenger, passenger1, passenger2, passenger3, passenger4, passenger5):
#     print(p.pass_details())
choice = ' '
while choice != '3':
    choice = input('select 1 to see flights, 2 to see passengers, 3 to exit: ')
    if choice == '1':
        for f in (flight, flight1, flight2):
            print(f.flightlist())
    elif choice == '2':
        for p in (passenger, passenger1, passenger2, passenger3, passenger4, passenger5):
            print(p.pass_details())
    else:
        break
