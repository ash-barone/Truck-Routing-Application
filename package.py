import csv
from datetime import datetime

from hash import HashTable

truck1_packages = []
truck2_packages_trip1 = []
truck2_packages_trip2 = []
truck3_packages = []


class Package:
    def __init__(self, package_id, address, city, state, package_zip, delivery_deadline, weight, special_notes,
                 delivery_status):
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
        return "ID: %s, Address: %s, City: %s, State: %s, Zip Code: %s, Delivery Deadline: %s, Weight: %s, " \
               "Special Notes: %s, Delivery Status: %s" % (
                   self.package_id, self.address, self.city, self.state, self.package_zip, self.delivery_deadline,
                   self.weight,
                   self.special_notes, self.delivery_status)

    def get_package_id(self):
        return self.package_id

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_package_zip(self):
        return self.package_zip

    def get_delivery_deadline(self):
        return self.delivery_deadline

    def get_weight(self):
        return self.weight

    def get_special_notes(self):
        return self.special_notes

    def get_delivery_status(self):
        return self.delivery_status

    def set_package_id(self, package_id):
        self.package_id = package_id

    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_package_zip(self, package_zip):
        self.package_zip = package_zip

    def set_delivery_deadline(self, deliver_deadline):
        self.delivery_deadline = deliver_deadline

    def set_weight(self, weight):
        self.weight = weight

    def set_special_notes(self, special_notes):
        self.special_notes = special_notes

    def set_delivery_status(self, deliver_status):
        self.delivery_status = deliver_status

    def load_package_data(file_name, hash_table):
        with open(file_name) as packages:
            package_data = csv.reader(packages, delimiter=',')

            # truck packages lists

            next(package_data)  # skip header
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
                if len(package[7]) == 0:
                    notes = "N/A"
                else:
                    notes = package[7]
                if "Delayed" in package[7]:
                    status = "Delayed. Hub arrival at: " + \
                             str(datetime.now().replace(hour=9, minute=5, second=0).strftime("%H:%M:%S"))
                else:
                    status = "At hub. Arrived at hub: " + \
                             str(datetime.now().replace(hour=7, minute=30, second=0).strftime("%H:%M:%S"))

                p = Package(package_id, address, city, state, package_zip, deadline, mass, notes, status)

                # insert it into the hash table
                hash_table.insert(package_id, p)

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

                elif "Must be delivered with" in notes or package_id == 13 or package_id == 15 or package_id == 19:
                    truck1_packages.append(p)
                    # print("Truck 1 delivered with others: " + str(package_id))

                elif "EOD" not in deadline and package not in truck1_packages and package not in truck2_packages_trip1 \
                        and package not in truck2_packages_trip2 and package not in truck3_packages:
                    if len(truck1_packages) < 16:
                        truck1_packages.append(p)
                        # print("Truck 1 eod not in deadline: " + str(package_id))
                    elif len(truck2_packages_trip1) < 16:
                        truck2_packages_trip1.append(p)
                        # print("Truck 2 eod not in deadline: " + str(package_id))

                elif package not in truck1_packages and package not in truck2_packages_trip1 and \
                        package and package not in truck2_packages_trip2 not in truck3_packages:
                    if len(truck1_packages) < 7:
                        truck1_packages.append(p)
                        # print("Truck 1 not in other lists: " + str(package_id))
                    elif len(truck2_packages_trip2) < 8:
                        truck2_packages_trip2.append(p)
                        # print("Truck 2 not in other lists: " + str(package_id))
                    elif len(truck3_packages) < 16:
                        truck3_packages.append(p)
                        # print("Truck 3 not in other lists: " + str(package_id))
                    elif len(truck2_packages_trip1) < 8:
                        truck2_packages_trip2.append(p)
        print("Number of packages in list: ")
        print("truck 1: ")
        print(len(truck1_packages))
        print("truck 2 trip 1: ")
        print(len(truck2_packages_trip1))
        print("truck 2 trip 2: ")
        print(len(truck2_packages_trip2))
        print("truck 3: ")
        print(len(truck3_packages))


def create_package_lists():
    my_hash_table = HashTable()
    Package.load_package_data("packages.csv", my_hash_table)

    '''print("Packages from Hashtable:")
    # Fetch data from Hash Table
    for i in range(len(my_hash_table.table) + 1):
        print("Package: {}".format(my_hash_table.search(i + 1)))
'''
