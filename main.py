from datetime import datetime

import util
import packages
from hash import HashTable
from trucks import Truck

# from packages import create_package_lists

"""
Ashley Barone 002660549
"""
# initialize set_time to EOD(end of day 5:00PM)
set_time = (datetime.now().replace(hour=17, minute=0, second=0))

# create truck 1
truck1 = Truck(1, datetime.now().replace(hour=8, minute=0, second=0))

# create truck 2
truck2 = Truck(2, datetime.now().replace(hour=9, minute=5, second=0))

# create truck 3
truck3 = Truck(3, datetime.now().replace(hour=10, minute=35, second=0))

# hash_table = HashTable()

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
            set_time_hour = input("Please enter a specific hour. If requesting EOD(End of Day), please type EOD: ")
            if set_time_hour != "EOD":
                set_time_minute = input("Please enter a specific two digit minute.: ")
                while len(set_time_minute) != 2:
                    set_time_minute = input("Invalid input. Please enter a specific two digit minute including "
                                            "leading zero: ")
                set_time = datetime.now().replace(hour=int(set_time_hour), minute=int(set_time_minute), second=0)
            else:
                set_time = datetime.now().replace(hour=17, minute=0, second=0)

            # checks if the set time entered by user is before truck 1 departure
            if set_time >= datetime.now().replace(hour=8, minute=0, second=0):
                try:
                    truck1.clear_packages()
                    truck2.clear_packages()
                    truck3.clear_packages()

                    packages.hash_table.clear()
                    packages.create_package_lists()

                    '''for i in range(len(packages.hash_table.table) + 1):
                        package_to_reset = packages.hash_table.search(i)
                        package_to_reset.reset_delivery_status()'''

                    '''set_time_hour = int(input("Please enter a specific hour: "))
                    set_time_minute = int(input("Please enter a specific minute: "))
                    set_time = datetime.now().replace(hour=set_time_hour, minute=set_time_minute, second=0)'''
                    # print("SET TIME: ")
                    # print(set_time)

                    # create and load truck 1
                    truck1 = Truck(1, datetime.now().replace(hour=8, minute=0, second=0))
                    truck1.load_packages(1, packages.truck1_packages, set_time)

                    # create and load truck 2 trip 1
                    # if set_time >= datetime.now().replace(hour=9, minute=5, second=0):
                    truck2 = Truck(2, datetime.now().replace(hour=9, minute=5, second=0))
                    truck2.load_packages(2, packages.truck2_packages_trip1, set_time)

                    # create and load truck 3
                    truck3 = Truck(3, datetime.now().replace(hour=10, minute=35, second=0))
                    truck3.load_packages(3, packages.truck3_packages, set_time)
                    '''for p in truck3.loaded_packages:
                        print("Loaded Package: ")
                        print(p)'''

                    # create a graph of the addresses from csv
                    util.create_address_graph()

                    # create empty list of the alg results for each truck
                    truck1_alg_results = []
                    truck2_trip1_alg_results = []
                    truck3_alg_results = []
                    # truck3_alg_results = []

                    # get alg results from loaded packages in each truck except truck 2 trip 2
                    truck1_alg_results = util.find_shortest_distance(truck1.curr_location, truck1.loaded_packages)
                    truck2_trip1_alg_results = util.find_shortest_distance(truck2.curr_location, truck2.loaded_packages)
                    truck3_alg_results = util.find_shortest_distance(truck3.curr_location, truck3.loaded_packages)

                    '''print("Optimized Package List Truck 1: ")
                    for p in truck1_alg_results[0]:
                        print(p)'''

                    # truck 1 trip
                    print("\nTruck 1:\n")
                    truck1.deliver_packages(set_time, truck1_alg_results[0],
                                            truck1_alg_results[1])
                    # truck1.return_truck()
                    print("\nTruck 1 Current Location and Miles Traveled: ")
                    if truck1.departure_time > set_time:
                        truck1.curr_time = set_time
                        print(truck1.curr_time)
                    else:
                        print(truck1.curr_time)
                    print(truck1.curr_location)
                    print(truck1.get_miles_traveled())
                    print("\n")

                    # truck 2
                    print("Truck 2:\n")
                    truck2.deliver_packages(set_time,
                                            truck2_trip1_alg_results[0],
                                            truck2_trip1_alg_results[1])
                    # truck2.return_truck()
                    print("\nTruck 2 Current Location and Miles Traveled: ")
                    if truck2.departure_time > set_time:
                        truck2.curr_time = set_time
                        print(truck2.curr_time)
                    else:
                        print(truck2.curr_time)
                    print(truck2.curr_location)
                    print(str(truck2.get_miles_traveled()))
                    print("\n")

                    # truck trip 2
                    '''print("Truck 2 Trip 2:\n")
                    truck2.set_departure_time(datetime.now().replace(hour=10, minute=44, second=0))
                    if set_time >= datetime.now().replace(hour=10, minute=44, second=0):
                        truck2.load_packages(2, package.truck2_packages_trip2, set_time)
                        truck2_trip2_alg_results = util.find_shortest_distance(truck2.curr_location,
                                                                               truck2.loaded_packages)
                        truck2.deliver_packages(set_time,
                                                truck2_trip2_alg_results[0],
                                                truck2_trip2_alg_results[1])
                    # truck2.return_truck()
                    print("\nTruck 2 Current Location and Miles Traveled: ")
                    print(truck2.curr_location)
                    print("Miles traveled: ")
                    print(truck2.get_miles_traveled())
                    print("\n")'''

                    # truck 3 trip
                    print("Truck 3:")
                    truck3.deliver_packages(set_time, truck3_alg_results[0],
                                            truck3_alg_results[1])
                    # truck3.return_truck()
                    print("\nTruck 3 Current Location and Miles Traveled:")
                    if truck3.departure_time > set_time:
                        truck3.curr_time = set_time
                        print(truck3.curr_time)
                    else:
                        print(truck3.curr_time)
                    print(truck3.curr_location)
                    print(truck3.get_miles_traveled())
                    print("\n")

                    print("Packages still at hub: ")
                    # print(truck3.get_loaded_packages())
                    # print(truck3.get_delivered_packages())
                    at_hub_string = "at hub "

                    # Space-time complexity of O(n)
                    for i in range(len(packages.hash_table.table) + 1):
                        search_result = str(packages.hash_table.search(i))
                        if at_hub_string in search_result:
                            print(packages.hash_table.search(i))
                            found_package = True
                        '''if p not in truck1.get_delivered_packages() and p not in truck1.get_loaded_packages() \
                                and p not in truck2.get_delivered_packages() and p not in truck2.get_loaded_packages() \
                                and p not in truck3.get_delivered_packages() and p not in truck3.get_loaded_packages()\
                                and p is not None:
                            print(p)'''

                    print("\nTOTAL MILES TRAVELED: ")
                    print(truck1.get_miles_traveled() + truck2.get_miles_traveled() + truck3.get_miles_traveled())
                    print("\n")

                    if set_time_hour == "EOD" or ((len(truck1.loaded_packages) == 0
                                                   and truck1.curr_time == datetime.now().replace(hour=10, minute=34,
                                                                                                  second=0).strftime("%H:%M:%S"))
                                                  and (len(truck2.loaded_packages) == 0
                                                       and truck2.curr_time == datetime.now().replace(hour=10,
                                                                                                      minute=51, second=0).strftime("%H:%M:%S"))
                                                  and (len(truck3.loaded_packages) == 0
                                                       and truck3.curr_time == datetime.now().replace(hour=12,
                                                                                                      minute=43, second=0).strftime("%H:%M:%S"))):
                        print("TIME ALL TRUCKS COMPLETED ROUTE BACK AT HUB: ")
                        print("Truck 1: " + str(truck1.curr_time))
                        print("Truck 2: " + str(truck2.curr_time))
                        print("Truck 3: " + str(truck3.curr_time))

                except ValueError:
                    print("Invalid input. Please try again.")

            # checks if the set time entered by user is after packages arrived but before truck 1 departure
            elif (datetime.now().replace(hour=7, minute=29, second=0)) < set_time < (datetime.now().replace(hour=7,
                                                                                                            minute=59,
                                                                                                            second=0)):
                packages.create_package_lists()
                print("\nPackages at hub have not been loaded onto trucks yet. Below is today's list of packages.\n")
                # Space-time complexity is O(n)
                for i in range(len(packages.my_hash_table.table) + 1):
                    print("Package: {}".format(packages.my_hash_table.search(i)))

            # for times before any packages have arrived
            else:
                print("There are currently no packages at the hub. First delivery is expected at 07:30AM "
                      "with any delays arriving later.")

        # allows user to run enter day of deliveries and see miles and time last truck completed
        elif option == "2":
            try:
                print("\n")
                set_time = (datetime.now().replace(hour=17, minute=0, second=0))
                # clear truck lists
                truck1.clear_packages()
                truck2.clear_packages()
                truck3.clear_packages()

                packages.hash_table.clear()
                packages.create_package_lists()

                # create and load truck 1
                truck1 = Truck(1, datetime.now().replace(hour=8, minute=0, second=0))
                truck1.load_packages(1, packages.truck1_packages, set_time)

                # create and load truck 2 trip 1
                truck2 = Truck(2, datetime.now().replace(hour=9, minute=5, second=0))
                truck2.load_packages(2, packages.truck2_packages_trip1, set_time)

                # create and load truck 3
                truck3 = Truck(3, datetime.now().replace(hour=10, minute=35, second=0))
                truck3.load_packages(3, packages.truck3_packages, set_time)
                '''for p in truck3.loaded_packages:
                    print("Loaded Package: ")
                    print(p)'''

                # create a graph of the addresses from csv
                util.create_address_graph()

                # get alg results from loaded packages in each truck except truck 2 trip 2
                truck1_alg_results = util.find_shortest_distance(truck1.curr_location, truck1.loaded_packages)
                truck2_trip1_alg_results = util.find_shortest_distance(truck2.curr_location, truck2.loaded_packages)
                truck3_alg_results = util.find_shortest_distance(truck3.curr_location, truck3.loaded_packages)

                '''print("Optimized Package List Truck 1: ")
                for p in truck1_alg_results[0]:
                    print(p)'''

                # truck 1 trip
                print("Truck 1:\n")
                truck1.deliver_packages((datetime.now().replace(hour=17, minute=0, second=0)), truck1_alg_results[0],
                                        truck1_alg_results[1])
                # truck1.return_truck()
                print("\nTruck 1 Current Time, Location, and Miles Traveled:")
                print(truck2.curr_time)
                print(truck1.curr_location)
                print(truck1.get_miles_traveled())
                print("\n")

                # truck 2 trip 1
                print("Truck 2 Trip 1:\n")
                truck2.deliver_packages((datetime.now().replace(hour=17, minute=0, second=0)),
                                        truck2_trip1_alg_results[0],
                                        truck2_trip1_alg_results[1])
                # truck2.return_truck()
                print("\nTruck 2 Current Time, Location, and Miles Traveled: ")
                print(truck2.curr_time)
                print(truck2.curr_location)
                print(str(truck2.get_miles_traveled()))
                print("\n")

                # truck trip 2
                '''print("Truck 2 Trip 2:\n")
                truck2.set_departure_time(datetime.now().replace(hour=10, minute=44, second=0))
                truck2.load_packages(2, package.truck2_packages_trip2, set_time)
                truck2_trip2_alg_results = util.find_shortest_distance(truck2.curr_location, truck2.loaded_packages)
                truck2.deliver_packages((datetime.now().replace(hour=17, minute=0, second=0)), truck2_trip2_alg_results[0],
                                        truck2_trip2_alg_results[1])
                # truck2.return_truck()
                print("\nTruck 2 Current Time and Location: ")
                print(truck2.curr_time.strftime("%H:%M:%S"))
                print(truck2.curr_location)
                print("Miles traveled: ")
                print(truck2.get_miles_traveled())
                print("\n")'''

                # truck 3 trip
                truck3.deliver_packages((datetime.now().replace(hour=17, minute=0, second=0)), truck3_alg_results[0],
                                        truck3_alg_results[1])
                # truck3.return_truck()
                print("\nTruck 3 Current Time, Location, and Miles Traveled:")
                print(truck3.curr_location)
                print(truck3.get_miles_traveled())
                print("\n")

                print("Packages still at hub: ")
                # print(truck3.get_loaded_packages())
                # print(truck3.get_delivered_packages())
                at_hub_string = "at hub "
                for i in range(len(packages.hash_table.table) + 1):
                    search_result = str(packages.hash_table.search(i))
                    if at_hub_string in search_result:
                        print(packages.hash_table.search(i))
                        found_package = True

                # print total miles traveled to show efficiency
                print("\nTOTAL MILES TRAVELED: ")
                print(truck1.get_miles_traveled() + truck2.get_miles_traveled() + truck3.get_miles_traveled())
                print("\n")

                print("TIME ALL TRUCKS COMPLETED ROUTE BACK AT HUB: ")
                print("Truck 1: " + str(truck1.curr_time.strftime("%H:%M:%S")))
                print("Truck 2: " + str(truck2.curr_time.strftime("%H:%M:%S")))
                print("Truck 3: " + str(truck3.curr_time.strftime("%H:%M:%S")))

                truck1.update_delivery_status("hub")
                truck2.update_delivery_status("hub")
                truck3.update_delivery_status("hub")
            except ValueError:
                print("Invalid input. Please try again.")

        # allows user to look up a package using the package id
        elif option == "3":
            lookup_id = str(input("Please enter a package ID: "))
            print("Package info accessed at 07:59AM.")
            packages.create_package_lists()
            lookup_str = "ID: " + lookup_id + ","
            found_package = False
            for i in range(len(packages.hash_table.table) + 1):
                search_result = str(packages.hash_table.search(i))
                if lookup_str in search_result:
                    print("Package: ")
                    print(packages.hash_table.search(i))
                    found_package = True
            if not found_package:
                print("Package not found. Please try again.")
                # print("Package: {}".format(packages.hash_table.search(i)))

        # allows user to exit the program
        elif option == "4":
            print("Goodbye!")
            isOpen = False

        # warns user of invalid input so they can try again
        else:
            print("Invalid input. Please try again.")
