from datetime import datetime

import util
import package
from truck import Truck
from package import create_package_lists

"""
Ashley Barone 002660549
"""
# initialize set_time to EOD(end of day 5:00PM)
set_time = (datetime.now().replace(hour=17, minute=0, second=0))

# create truck 1
truck1 = Truck(1, datetime.now().replace(hour=8, minute=0, second=0))

# create truck 2 with trip 1 start time
truck2 = Truck(2, datetime.now().replace(hour=9, minute=5, second=0))

'''# create and load truck 3 // no longer needed 
truck3 = Truck(3, datetime.now().replace(hour=10, minute=19, second=0))
truck3.load_packages(3, package.truck3_packages)'''

# begin ui
if __name__ == '__main__':
    print("\nWelcome to Western Governors University Parcel Service Delivery Lookup System!\nThe current time is "
          "07:59AM.")

    # provides user with options including package statuses by time, deliver all packages, lookup package, and exit
    isOpen = True
    while isOpen:
        print("\nChoose from the following options using the number keys:")
        print("1. Lookup Package Statuses By Specific Time")
        print("2. Load and Deliver All Packages For Day")
        print("3. Lookup Package By ID")
        print("4. Exit the Program")
        option = input("Chose an option (1,2,3, or 4): ")

        # allows user to enter a time with hour and minutes to see the status of trucks packages at that time
        if option == "1":
            print("\n")
            set_time_hour = int(input("Please enter a specific hour: "))
            set_time_minute = int(input("Please enter a specific minute: "))
            set_time = datetime.now().replace(hour=set_time_hour, minute=set_time_minute, second=0)

            # checks if the set time entered by user is before truck 1 departure
            if set_time >= datetime.now().replace(hour=8, minute=0, second=0):
                try:
                    truck1.clear_packages()
                    truck2.clear_packages()
                    # truck3.clear_packages()

                    package.my_hash_table.clear()
                    create_package_lists()

                    '''set_time_hour = int(input("Please enter a specific hour: "))
                    set_time_minute = int(input("Please enter a specific minute: "))
                    set_time = datetime.now().replace(hour=set_time_hour, minute=set_time_minute, second=0)'''
                    # print("SET TIME: ")
                    # print(set_time)

                    # create and load truck 1
                    truck1 = Truck(1, datetime.now().replace(hour=8, minute=0, second=0))
                    truck1.load_packages(1, package.truck1_packages)

                    # create and load truck 2 trip 1
                    if set_time >= datetime.now().replace(hour=9, minute=5, second=0):
                        truck2 = Truck(2, datetime.now().replace(hour=9, minute=5, second=0))
                        truck2.load_packages(2, package.truck2_packages_trip1)

                    # create and load truck 3
                    '''truck3 = Truck(3, datetime.now().replace(hour=10, minute=19, second=0))
                    truck3.load_packages(3, package.truck3_packages)'''
                    '''for p in truck3.loaded_packages:
                        print("Loaded Package: ")
                        print(p)'''

                    # create a graph of the addresses from csv
                    util.create_address_graph()

                    # create empty list of the alg results for each truck
                    truck1_alg_results = []
                    truck2_trip1_alg_results = []
                    truck2_trip2_alg_results = []
                    # truck3_alg_results = []

                    # get alg results from loaded packages in each truck except truck 2 trip 2
                    truck1_alg_results = util.find_shortest_distance(truck1.curr_location, truck1.loaded_packages)
                    truck2_trip1_alg_results = util.find_shortest_distance(truck2.curr_location, truck2.loaded_packages)
                    # truck3_alg_results = util.find_shortest_distance(truck3.curr_location, truck3.loaded_packages)

                    '''print("Optimized Package List Truck 1: ")
                    for p in truck1_alg_results[0]:
                        print(p)'''

                    # truck 1 trip
                    print("\nTruck 1:\n")
                    truck1.deliver_packages(set_time, truck1_alg_results[0],
                                            truck1_alg_results[1])
                    # truck1.return_truck()
                    print("\nTruck 1 Current Location and Miles Traveled: ")
                    print(truck1.curr_location)
                    print(truck1.get_miles_traveled())
                    print("\n")

                    # truck 2 trip 1
                    print("Truck 2 Trip 1:\n")
                    truck2.deliver_packages(set_time,
                                            truck2_trip1_alg_results[0],
                                            truck2_trip1_alg_results[1])
                    # truck2.return_truck()
                    print("\nTruck 2 Current Location and Miles Traveled: ")
                    print(truck2.curr_location)
                    print("Miles traveled first trip: ")
                    print(str(truck2.get_miles_traveled()))
                    print("\n")

                    # truck trip 2
                    print("Truck 2 Trip 2:\n")
                    if set_time >= datetime.now().replace(hour=10, minute=44, second=0):
                        truck2.set_departure_time(datetime.now().replace(hour=10, minute=44, second=0))
                        truck2.load_packages(2, package.truck2_packages_trip2)
                    truck2_trip2_alg_results = util.find_shortest_distance(truck2.curr_location, truck2.loaded_packages)
                    truck2.deliver_packages(set_time,
                                            truck2_trip2_alg_results[0],
                                            truck2_trip2_alg_results[1])
                    # truck2.return_truck()
                    print("\nTruck 2 Current Location and Miles Traveled: ")
                    print(truck2.curr_location)
                    print("Miles traveled: ")
                    print(truck2.get_miles_traveled())
                    print("\n")

                    print("Packages still at hub: ")
                    for package in package.get_all_packages():
                        if (package not in truck1.get_delivered_packages() and \
                                package not in truck2.get_delivered_packages()) and package is not None:
                            print(package)

                    # truck 3 trip
                    '''truck3.deliver_packages(set_time, truck3_alg_results[0],
                                            truck3_alg_results[1])
                    # truck3.return_truck()
                    print("\nTruck 3 Current Time and Location:")
                    print(truck3.curr_time.strftime("%H:%M:%S"))
                    print(truck3.curr_location)
                    print(truck3.get_miles_traveled())
                    print("\n")'''

                    print("\nTOTAL MILES TRAVELED: ")
                    print(truck1.get_miles_traveled() + truck2.get_miles_traveled())
                    print("\n")

                except ValueError:
                    print("Invalid input. Please try again.")

            # checks if the set time entered by user is after packages arrived but before truck 1 departure
            elif (datetime.now().replace(hour=7, minute=29, second=0)) < set_time < (datetime.now().replace(hour=7,
                                                                                                            minute=59,
                                                                                                            second=0)):
                create_package_lists()
                print("\nPackages at hub have not been loaded onto trucks yet. Below is today's list of packages.\n")
                for i in range(len(package.my_hash_table.table) + 1):
                    print("Package: {}".format(package.my_hash_table.search(i)))

            # for times before any packages have arrived
            else:
                print("There are currently no packages at the hub. First delivery is expected at 07:30AM "
                      "with any delays arriving later.")

        # allows user to run enter day of deliveries and see miles and time last truck completed
        elif option == "2":
            print("\n")
            set_time = (datetime.now().replace(hour=17, minute=0, second=0))
            # clear truck lists
            truck1.clear_packages()
            truck2.clear_packages()
            # truck3.clear_packages()

            package.my_hash_table.clear()
            create_package_lists()

            # create and load truck 1
            truck1 = Truck(1, datetime.now().replace(hour=8, minute=0, second=0))
            truck1.load_packages(1, package.truck1_packages)

            # create and load truck 2 trip 1
            truck2 = Truck(2, datetime.now().replace(hour=9, minute=5, second=0))
            truck2.load_packages(2, package.truck2_packages_trip1)

            # create and load truck 3
            '''truck3 = Truck(3, datetime.now().replace(hour=10, minute=19, second=0))
            truck3.load_packages(3, package.truck3_packages)'''
            '''for p in truck3.loaded_packages:
                print("Loaded Package: ")
                print(p)'''

            # create a graph of the addresses from csv
            util.create_address_graph()

            # get alg results from loaded packages in each truck except truck 2 trip 2
            truck1_alg_results = util.find_shortest_distance(truck1.curr_location, truck1.loaded_packages)
            truck2_trip1_alg_results = util.find_shortest_distance(truck2.curr_location, truck2.loaded_packages)
            # truck3_alg_results = util.find_shortest_distance(truck3.curr_location, truck3.loaded_packages)

            '''print("Optimized Package List Truck 1: ")
            for p in truck1_alg_results[0]:
                print(p)'''

            # truck 1 trip
            print("Truck 1:\n")
            truck1.deliver_packages((datetime.now().replace(hour=17, minute=0, second=0)), truck1_alg_results[0],
                                    truck1_alg_results[1])
            # truck1.return_truck()
            print("\nTruck 1 Current Time and Location:")
            print(truck1.curr_time.strftime("%H:%M:%S"))
            print(truck1.curr_location)
            print(truck1.get_miles_traveled())
            print("\n")

            # truck 2 trip 1
            print("Truck 2 Trip 1:\n")
            truck2.deliver_packages((datetime.now().replace(hour=17, minute=0, second=0)), truck2_trip1_alg_results[0],
                                    truck2_trip1_alg_results[1])
            # truck2.return_truck()
            print("\nTruck 2 Current Time and Location: ")
            print(truck2.curr_time.strftime("%H:%M:%S"))
            print(truck2.curr_location)
            print("Miles traveled first trip: ")
            print(str(truck2.get_miles_traveled()))
            print("\n")

            # truck trip 2
            print("Truck 2 Trip 2:\n")
            truck2.set_departure_time(datetime.now().replace(hour=10, minute=44, second=0))
            truck2.load_packages(2, package.truck2_packages_trip2)
            truck2_trip2_alg_results = util.find_shortest_distance(truck2.curr_location, truck2.loaded_packages)
            truck2.deliver_packages((datetime.now().replace(hour=17, minute=0, second=0)), truck2_trip2_alg_results[0],
                                    truck2_trip2_alg_results[1])
            # truck2.return_truck()
            print("\nTruck 2 Current Time and Location: ")
            print(truck2.curr_time.strftime("%H:%M:%S"))
            print(truck2.curr_location)
            print("Miles traveled: ")
            print(truck2.get_miles_traveled())
            print("\n")

            '''# truck 3 trip // no longer needed but could be used if more packages than 40 added
            truck3.deliver_packages((datetime.now().replace(hour=17, minute=0, second=0)), truck3_alg_results[0],
                                    truck3_alg_results[1])
            # truck3.return_truck()
            print("\nTruck 3 Current Time and Location:")
            print(truck3.curr_time.strftime("%H:%M:%S"))
            print(truck3.curr_location)
            print(truck3.get_miles_traveled())
            print("\n")'''

            # print total miles traveled to show efficiency
            print("TOTAL MILES TRAVELED: ")
            print(truck1.get_miles_traveled() + truck2.get_miles_traveled())
            print("\n")

        # allows user to look up a package using the package id
        elif option == "3":
            lookup_id = int(input("Please enter a package ID: "))
            print("Package info accessed at 07:59AM.")
            print("Package: ")
            create_package_lists()
            print(package.my_hash_table.search(lookup_id))

        # allows user to exit the program
        elif option == "4":
            print("Goodbye!")
            isOpen = False

        # warns user of invalid input so they can try again
        else:
            print("Invalid input. Please try again.")
