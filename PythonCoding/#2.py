import os

# Specify the directory containing the text files
directory = r"C:\Users\ayush\Downloads"

# List all files in the directory
files = os.listdir(directory)

# Iterate over each file in the directory
for file_name in files:
    # Check if it's a text file (you can adjust the condition as per your file naming convention)
    if file_name.endswith('TEXT FILE.txt'):
        # Construct the full file path
        file_path = os.path.join(directory, file_name)

        # Open the file for reading
        with open(file_path, 'r') as file:
            # Read the contents of the file
            file_contents = file.read()

            # Do something with the file contents
            print(f"Contents of {file_name}:")
            print(file_contents)
