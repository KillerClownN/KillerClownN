file_path = input("Enter the path to the text file: ")

# Read the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Remove newline characters
lines = [line.rstrip('\n') for line in lines]

# Write the modified lines back to the file
with open(file_path, 'w') as file:
    file.writelines(lines)

print("Newline characters removed successfully.")
