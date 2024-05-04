# Programming and Scripting
# Task - Project
# This program is based on the well-known Fisher’s Iris data set.
# This program should:
# 1. Output a summary of each variable to a single text file,
# 2. Save a histogram of each variable to png files, and
# 3. Output a scatter plot of each pair of variables.
# 4. Perform any other analysis you think is appropriate.

# First I'm importing all libraries that I can use to work/manipulate data files
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from skimpy import skim, generate_test_data
from analysisfFunctions import create_empty_file


# Creating a text file to write the data from running the program
# Using 'w' parameter we make sure that if the file doesn't exist it is created. 
# It will also empty the content of the file every time the program is run.

# calling the function create_empty_file to create the output file analysis.txt.
my_file = "analysis.txt"  
create_empty_file(my_file)
print(f"\n\nAnalyzing Iris DataSet.\nA file named '{my_file}' is created to store all your data.\n\n")


df = pd.read_csv("iris.csv", skip_blank_lines=True)
df_describe = df.describe()
df_types = df.dtypes
df_species = df["species"].value_counts()
df_setosa = df[df["species"] == "setosa"].describe()
df_versicolor = df[df["species"] == "versicolor"].describe()
df_virginica = df[df["species"] == "virginica"].describe()

with open(my_file, 'a') as file:
    file.write("\n\nColumn labels of the iris DataFrame are:\n")
    for i, label in enumerate(df.columns):
        file.write(f"{i+1}. {label}\n")
        
    file.write("\n\nSummary of the Iris dataset:\n")
    file.write(df_describe.to_string())
    file.write("\n\nData types in this Dataset:\n\n" + df_types.to_string())
    file.write("Main species in the dataset:\n\n" + df_species.to_string())
    file.write("\n\nSummary of Iris Setosa:\n\n" + df_setosa.to_string())
    file.write("\n\nSummary of Iris Versicolor:\n\n" +df_versicolor.to_string())
    file.write("\n\nSummary of Iris Virginica:\n\n" + df_virginica.to_string())
    
    




'''
basic exercise code: 

my_file = open("analysis.txt", "w")
my_file.write("This file contains my analysis of the Iris.\n\n")

# Loading the data to the dataframe pd and skip any lines with NAN (empty) values.
df = pd.read_csv("iris.csv", skip_blank_lines=True)

# checking if we can write info to our text file.
# write the first 5 lines of the iris.csv to text file
my_file.write(df.head().to_string())
my_file.write("\n\n")
# Write to file last 5 rows.
my_file.write(df.tail().to_string())

# Information about dataset.
# my_file.write("\n\nInformation about the DataSet\n\n" + df.info(buf=f))

# Write data type 
my_file.write("\n\nData Types in the DataSet\n\n" + df.dtypes)

# Summary of DataSet.
my_file.write("\n\nA Concise Summary of DataSet\n\n" + df.describe().to_string())

# print that all went well.
print("writing in the file was successful! ")

'''

# references:

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# https://realpython.com/python-csv/
# https://python-course.eu/numerical-programming/reading-and-writing-data-in-pandas.php