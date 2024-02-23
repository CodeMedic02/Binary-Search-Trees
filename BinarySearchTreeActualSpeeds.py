# Trent Adams
# Date: 2024-11-02

from BinarySearchTree import BinarySearchTree
from Client import Client
from datetime import date
import time     # Used for code execution timing.
import random   # Used for generating random numbers.
import sys

# display author's name and the date in the output.
print("Name: <NAME>")
print("Date: " + str(date.today()))
print()

# Create an empty list.
clients = []

# read the records into the list.
input_file_name = "ClientData.csv"
with open(input_file_name, "r") as infile:
    for line in infile:
        # Split the line into a list of strings based on commas.
        s = line.split(",")
        client_id = int(s[0])  # Convert the default string to an integer.
        first_name = s[1]
        last_name = s[2]
        phone = s[3]
        email = s[4]
        # Create a new Client object and add it to the list.
        clt = Client(client_id, first_name, last_name, phone, email)
        clients.append(clt)

# How many clients are in the list?
print("There are " + str(len(clients)) + " clients in the list.")

# Create the binary search tree to test real-world performance.
bst = BinarySearchTree()

# Scenario 1: Printer Ques or Call Que or Service Que
section_title = "Scenario 1: Printer Ques or Call Que or Service Que"
print(section_title)
print("-" * len(section_title))

# How long does it take to insert all the clients into the tree?
start_time = time.time()

for i in range(len(clients)):
    bst.insert(clients[i])

end_time = time.time()
total_time = end_time - start_time
print("Seconds to insert all the clients into the tree: {:6f}".format(total_time))

# How long does it take to remove records from the tree?
for i in range(len(clients)):
    bst.remove_minimum()

end_time = time.time()
total_time = end_time - start_time
print("Seconds to remove records from the tree: {:6f}".format(total_time))

# Scenario 2: Random Ques
answer = input("Do you want to run scenario 2? (y/n) ")
if answer.lower() != "y":
    sys.exit()


section_title = "Scenario 2: Random Ques"
print(section_title)
print("-" * len(section_title))

# Add clients to the binary search tree.
for i in range(len(clients)):
    bst.insert(clients[i])

# How long does it take to search 1000 random clients?
start_time = time.time()

for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + len(clients) - 1
    random_num = random.randint(smallest_id, largest_id)
    print(bst.search(Client(random_num)))

end_time = time.time()
total_time = end_time - start_time
print("Seconds to display 1000 random clients: {:6f}".format(total_time))

answer = input("Do you want to run scenario 3? (y/n) ")
if answer.lower() != "y":
    sys.exit()

# Scenario 3: Call Center
section_title = "Scenario 3: Call Center"
print(section_title)
print("-" * len(section_title))

# Add more clients to the binary search tree.
for i in range(len(clients)):
    bst.insert(clients[i])

# How long does it take to add more client records,
# Randomly display 1000 records, and randomly,
# remove records from the tree?
start_time = time.time()

# Add Records
current_id = 100001 + len(clients) + 1
for i in range(1000):
    bst.insert(Client(current_id))
    current_id += 1

# Display Records.
for i in range(100):
    smallest_id = 100001
    largest_id = smallest_id + len(clients) - 1
    random_num = random.randint(smallest_id, largest_id)
    print(bst.search(Client(random_num)))

# Remove 1000 random records from the tree.
for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + len(clients)
    random_num = random.randint(smallest_id, largest_id)
    bst.remove(Client(random_num))

end_time = time.time()
total_time = end_time - start_time
print("Seconds add records: {:6f}".format(total_time))
