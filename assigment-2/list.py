# Create empty list
my_list = []

# Appending 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Inserting 15 at index 1
my_list.insert(1, 15)
print(my_list)

# Extending
my_list.extend([50, 60, 70])
print(my_list)

# Removing the last element
my_list.pop()
print(my_list)

# Sorting list in ascending order
my_list.sort()
print(my_list)

# Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)


