# Take input from user for the value of k
k = int(input("Enter the value of k: "))

# Take input from user for the list of tuples
tuples_list = eval(input("Enter a list of tuples: "))

# Remove tuples that have a length of k
new_list = [t for t in tuples_list if len(t) != k]

# Display the new list without tuples of length k
print("New list without tuples of length", k, ":", new_list)
