file_path = '/Users/namansahai/naman.txt'
num_lines = 1

# Open the file in read mode
with open(file_path, 'r') as file:

    # Read the first n lines of the file
    first_lines = []
    for i in range(num_lines):
        line = file.readline().strip()
        first_lines.append(line)

    # Read the last n lines of the file
    last_lines = []
    file.seek(0)  # Return to the beginning of the file
    lines = file.readlines()
    for line in lines[-num_lines:]:
        last_lines.append(line.strip())

# Print the results
print(f"First {num_lines} lines: {first_lines}")
print(f"Last {num_lines} lines: {last_lines}")
