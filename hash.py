class HashTable:

    def __init__(self, capacity=40):
        """
        Initializes hash table with a capacity of 40 for the 40 packages.
        Space-time complexity of O(1).
        :param capacity: The amount of packages needing delivered
        """
        self.table = []
        for i in range(capacity):
            self.table.append([])

    def insert(self, key, item):
        """
        Inserts a package into the hash table.
        Space-time complexity of O(1).
        :param key: The package ID
        :param item: The package itself
        :return: True for package added
        """
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def update(self, key, item):
        """
        Update a package in the hash table.
        Space-time complexity of O(n).
        :param key: The package ID
        :param item: The updated package
        :return: True if package is updated
        """
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            # print (key_value)
            if key_value[0] == key:
                key_value[1] = item
                return True
            else:
                print(key + " could not be updated. Please try again.")

    def search(self, key):
        """
        Searches the hash table for a value using the provided key.
        Space-time complexity of O(n).
        :param key: The key to search for
        :return: The value that matches the key param
        """
        bucket = hash(key) % len(self.table)
        # print("bucket: ")
        # print(bucket)
        bucket_list = self.table[bucket]
        # print("bucket list: ")
        # print(bucket_list)
        # print(bucket_list)
        # print("bucket_list: " + str(bucket_list))
        for key_value in bucket_list:
            # print("key_value: " + str(key_value))
            if key_value[0] == key:
                return key_value[1]
        return None

    def remove(self, key):
        """
        Searches for a key value pair then removes it.
        Space-time complexity of O(n).
        :param key: The key to search for
        :return: True if key value pair is removed
        """
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for key_value in bucket_list:
            # print(key_value)
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])
                return True

    def clear(self):
        """
        Clears the hash table for each run through of deliveries from user menu. Ensures no duplicates.
        """
        del self
