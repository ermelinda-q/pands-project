# This file contains functions for main file analysis.txt

def create_empty_file(my_file):
    # Open the file in 'write' mode ('w'). If the file doesn't exist, it will be created.
    # If the file already exists, its contents will be overwritten.
    with open(my_file, 'w') as file:
        # Write a message as the First line of the text file.
        file.write("This is my analysis of Iris DataSet.") 




