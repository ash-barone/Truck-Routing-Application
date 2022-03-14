from datetime import datetime

import util
import package
from graph import Graph
from truck import Truck
from package import create_package_lists

# create package list from csv and sort by truck
create_package_lists()

# create and load truck 1
truck1 = Truck(1, datetime.now().replace(hour=8, minute=0, second=0))
truck1.load_packages(1, package.truck1_packages)

# create and load truck 2 trip 1
truck2 = Truck(2, datetime.now().replace(hour=9, minute=5, second=0))
truck2.load_packages(2, package.truck2_packages_trip1)

# create and load truck 3
truck3 = Truck(3, datetime.now().replace(hour=10, minute=19, second=0))
truck3.load_packages(3, package.truck3_packages)
'''for p in truck3.loaded_packages:
    print("Loaded Package: ")
    print(p)'''

# create a graph of the addresses from csv
util.create_address_graph()

# create empty list of the alg results for each truck
truck1_alg_results = []
truck2_trip1_alg_results = []
truck2_trip2_alg_results = []
truck3_alg_results = []

# get alg results from loaded packages in each truck except truck 2 trip 2
truck1_alg_results = util.find_shortest_distance(truck1.curr_location, truck1.loaded_packages)
truck2_trip1_alg_results = util.find_shortest_distance(truck2.curr_location, truck2.loaded_packages)
truck3_alg_results = util.find_shortest_distance(truck3.curr_location, truck3.loaded_packages)

'''print("Optimized Package List Truck 1: ")
for p in truck1_alg_results[0]:
    print(p)'''

# truck 1 trip
truck1.deliver_packages((datetime.now().replace(hour=17, minute=0, second=0)), truck1_alg_results[0], truck1_alg_results[1])
truck1.return_truck()
print("Truck 1 Return home time and location:")
print(truck1.curr_time)
print(truck1.curr_location)
print(truck1.get_miles_traveled())


# truck trip 1
truck2.deliver_packages((datetime.now().replace(hour=17, minute=0, second=0)), truck2_trip1_alg_results[0], truck2_trip1_alg_results[1])
truck2.return_truck()
print("Truck 2 Return home time and location: ")
print(truck2.curr_time)
print(truck2.curr_location)
print("Miles traveled first trip: ")
print(truck2.get_miles_traveled())
# TODO packages 25 and 34 are late why help

# truck trip 2
truck2.set_departure_time(datetime.now().replace(hour=10, minute=42, second=0))
truck2.load_packages(2, package.truck2_packages_trip2)
truck2_trip2_alg_results = util.find_shortest_distance(truck2.curr_location, truck2.loaded_packages)
truck2.deliver_packages((datetime.now().replace(hour=17, minute=0, second=0)), truck2_trip2_alg_results[0], truck2_trip2_alg_results[1])
truck2.return_truck()
print("Truck 2 Return home time and location: ")
print(truck2.curr_time)
print(truck2.curr_location)
print("Miles traveled: ")
print(truck2.get_miles_traveled())

# truck 3 trip
truck3.deliver_packages((datetime.now().replace(hour=17, minute=0, second=0)), truck3_alg_results[0], truck3_alg_results[1])
truck3.return_truck()
print("Truck 3 Return home time and location:")
print(truck3.curr_time)
print(truck3.curr_location)
print(truck3.get_miles_traveled())

print("TOTAL MILES TRAVELED: ")
print(truck1.get_miles_traveled() + truck2.get_miles_traveled() + truck3.get_miles_traveled())



