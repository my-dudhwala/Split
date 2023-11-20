import os
import shutil

def split_txt_file(filename):
    directory_name = filename[:-4]  # Get the filename without the extension

    # Create a new directory if it doesn't exist
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    with open(filename, 'r') as input_file:
        file_content = input_file.read()

    file_size = 0
    file_num = 1
    output_file = open(os.path.join(directory_name, f"{file_num}.txt"), 'w')

    for line in file_content:
        file_size += len(line)

        # If the file size reaches 63KB, close the current file and open a new one
        if file_size > 63000:
            output_file.close()
            file_size = 0
            file_num += 1
            output_file = open(os.path.join(directory_name, f"{file_num}.txt"), 'w')

        # Write the line to the current output file
        output_file.write(line)

    # Close the last output file
    output_file.close()

    # Remove the original txt file
    os.remove(filename)

# Check if a txt file was uploaded
if os.path.exists('uploaded_file.txt'):
    split_txt_file('uploaded_file.txt')