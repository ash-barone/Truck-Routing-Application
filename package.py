import csv
from datetime import datetime

from hash import HashTable

truck1_packages = []
truck2_packages_trip1 = []
truck2_packages_trip2 = []
truck3_packages = []
my_hash_table = HashTable()


class Package:
    def __init__(self, package_id, address, city, state, package_zip, delivery_deadline, weight, special_notes,
                 delivery_status):
        """
        Initializes package object with all information pertinent to lookup.
        :param package_id: The package ID and key used for hash table storage
        :param address: The delivery address
        :param city: The delivery city
        :param state: The delivery state
        :param package_zip: The delivery zip code
        :param delivery_deadline: The latest a delivery can be delivered
        :param weight: The weight of the package
        :param special_notes: Special notes for the delivery
        :param delivery_status: Status of the package's delivery
        """
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.package_zip = package_zip
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.special_notes = special_notes
        self.delivery_status = delivery_status

    def __str__(self):
        """
        Creates a string representation of a package object with format below.
        :return: The string representation of the package object
        """
        return "ID: %s, Address: %s, City: %s, State: %s, Zip Code: %s, Delivery Deadline: %s, Weight: %s, " \
               "Special Notes: %s, Delivery Status: %s" % (
                   self.package_id, self.address, self.city, self.state, self.package_zip, self.delivery_deadline,
                   self.weight,
                   self.special_notes, self.delivery_status)

    def get_package_id(self):
        """
        Gets the package id.
        :return: The package id
        """
        return self.package_id

    def get_address(self):
        """
        Gets the package address.
        :return: The package address
        """
        return self.address

    def get_city(self):
        """
        Gets the package city.
        :return: The package city
        """
        return self.city

    def get_state(self):
        """
        Gets the package state.
        :return: The package state
        """
        return self.state

    def get_package_zip(self):
        """
        Gets the package zip code.
        :return: The package zip code
        """
        return self.package_zip

    def get_delivery_deadline(self):
        """
        Gets the package's delivery deadline.
        :return: The package's delivery deadline
        """
        return self.delivery_deadline

    def get_weight(self):
        """
        Gets the package weight.
        :return: The package weight
        """
        return self.weight

    def get_special_notes(self):
        """
        Gets the package's special notes.
        :return: The package's special notes
        """
        return self.special_notes

    def get_delivery_status(self):
        """
        Gets the package's delivery status.
        :return: The package's delivery status
        """
        return self.delivery_status

    def set_package_id(self, package_id):
        """
        Sets the package ID.
        :param package_id: The new ID
        """
        self.package_id = package_id

    def set_address(self, address):
        """
        Sets the package address.
        :param address: The new address
        """
        self.address = address

    def set_city(self, city):
        """
        Sets the package city.
        :param city: The new city
        """
        self.city = city

    def set_state(self, state):
        """
        Sets the package state.
        :param state: The new state
        """
        self.state = state

    def set_package_zip(self, package_zip):
        """
        Sets the package zip code.
        :param package_zip: The new zip code
        """
        self.package_zip = package_zip

    def set_delivery_deadline(self, deliver_deadline):
        """
        Sets the package delivery deadline.
        :param deliver_deadline: The new deadline
        """
        self.delivery_deadline = deliver_deadline

    def set_weight(self, weight):
        """
        Sets the package weight.
        :param weight: The new weight
        """
        self.weight = weight

    def set_special_notes(self, special_notes):
        """
        Sets the package special notes.
        :param special_notes: The new special notes
        """
        self.special_notes = special_notes

    def set_delivery_status(self, deliver_status):
        """
        Sets the package delivery status.
        :param deliver_status: The new status
        """
        self.delivery_status = deliver_status

    def load_package_data(file_name, hash_table):
        """
        Reads packages.csv and adds each row to the hash table as a package object. After adding the package object,
        that package is then sorted into a truck packages list manually for specific packages or depending on 
        certain attributes such as delivery deadline or special notes.
        Space-time complexity of O(n).
        :param file_name: The name of the csv file to read
        :param hash_table: The hash table to fill with package objects
        """
        with open(file_name) as packages:
            package_data = csv.reader(packages, delimiter=',')

            # truck packages lists
            truck1_packages.clear()
            truck2_packages_trip1.clear()
            truck3_packages.clear()
            truck2_packages_trip2.clear()

            next(package_data)  # skip top line
            # cycle through each package in the package data as read by the csv reader
            for package in package_data:
                package_id = int(package[0])
                address = package[1]
                city = package[2]
                state = package[3]
                package_zip = package[4]
                if package_id == 9:
                    address = "410 S State St"
                    city = "Salt Lake City"
                    state = "UT"
                    package_zip = "84111"
                '''if "EOD" in package[5]:
                    deadline = datetime.now().replace(hour=17, minute=0, second=0).strftime("%H:%M:%S")
                elif "9:00" in package[5]:
                    deadline = datetime.now().replace(hour=9, minute=0, second=0).strftime("%H:%M:%S")
                elif "10:30" in package[5]:
                    deadline = datetime.now().replace(hour=10, minute=30, second=0).strftime("%H:%M:%S")
                else:'''
                deadline = package[5]
                mass = package[6]
                # if package has no special notes
                if len(package[7]) == 0:
                    notes = "N/A"
                else:
                    notes = package[7]
                if "Delayed" in package[7]:
                    status = "Delayed. Arriving at hub at " + \
                             str(datetime.now().replace(hour=9, minute=5, second=0).strftime("%H:%M:%S"))
                else:
                    status = "Arrived at hub at " + \
                             str(datetime.now().replace(hour=7, minute=30, second=0).strftime("%H:%M:%S"))

                p = Package(package_id, address, city, state, package_zip, deadline, mass, notes, status)

                # insert it into the hash table
                hash_table.insert(package_id, p)

                # manually add package 9 to truck 2 trip 2
                if package_id == 9:
                    truck2_packages_trip2.append(p)
                    # print("Truck 2 package 9: " + str(package_id))

                elif "truck 2" in notes:
                    truck2_packages_trip2.append(p)
                    # print("Truck 2 only truck 2: " + str(package_id))

                elif "Delayed" in status:
                    if "EOD" in deadline:
                        truck2_packages_trip2.append(p)
                    else:
                        truck2_packages_trip1.append(p)
                    # print("Truck 2 delayed: " + str(package_id))

                # manually add packages that must go together
                elif "Must be delivered with" in notes or package_id == 13 or package_id == 15 or package_id == 19:
                    truck1_packages.append(p)
                    # print("Truck 1 delivered with others: " + str(package_id))

                # add packages with deadlines
                elif "EOD" not in deadline and package not in truck1_packages and package not in truck2_packages_trip1 \
                        and package not in truck2_packages_trip2 and package not in truck3_packages:
                    if len(truck1_packages) < 16:
                        truck1_packages.append(p)
                        # print("Truck 1 eod not in deadline: " + str(package_id))
                    elif len(truck2_packages_trip1) < 16:
                        truck2_packages_trip1.append(p)
                        # print("Truck 2 eod not in deadline: " + str(package_id))

                # add all the other packages
                elif package not in truck1_packages and package not in truck2_packages_trip1 and \
                        package and package not in truck2_packages_trip2 not in truck3_packages:
                    if len(truck2_packages_trip2) < 10:
                        truck2_packages_trip2.append(p)
                        # print("Truck 2 not in other lists: " + str(package_id))
                    elif len(truck1_packages) < 10:
                        truck1_packages.append(p)
                    elif len(truck2_packages_trip1) < 16:
                        truck2_packages_trip1.append(p)
                    elif len(truck3_packages) < 16:
                        truck3_packages.append(p)
                        # print("Truck 3 not in other lists: " + str(package_id))

        print("Number of packages on each truck: ")
        print("Truck 1: ")
        print(len(truck1_packages))
        print("Truck 2 Trip 1: ")
        print(len(truck2_packages_trip1))
        print("Truck 2 Trip 2: ")
        print(len(truck2_packages_trip2))
        print("truck 3: ")
        print(len(truck3_packages))


def get_all_packages():
    package_list = []
    for i in range(len(my_hash_table.table) + 1):
        package = my_hash_table.search(i + 1)
        package_list.append(package)
    return package_list


def create_package_lists():
    """
    Calls the load package data method to create the hash table of packages.
    """
    # my_hash_table = HashTable()
    Package.load_package_data("packages.csv", my_hash_table)

    '''print("Packages from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(my_hash_table.table) + 1):
        print("Package: {}".format(my_hash_table.search(i + 1)))
'''
