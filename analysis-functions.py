# This file contains functions for main file analysis.txt

# Clean text function
# def clean_text(text):
    

def clean_text_data(data):
    # Clean the data (example: removing leading/trailing whitespaces)
    cleaned_data = [line.strip() for line in data]
    return cleaned_data

def clean_text_file(input_file):
    try:
        # Read data from the text file
        with open(input_file, 'r') as file:
            data = file.readlines()

        # Clean the data
        cleaned_data = clean_text_data(data)
        
        print("Data cleaned.")
        return cleaned_data
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

# Define the input text file
input_file = 'data.txt'

# Clean the text file every time the program runs
cleaned_data = clean_text_file(input_file)

# Now you can use the cleaned_data variable in memory without writing it back to the file

