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
import sys
import os

# Creating a text file to write the data from running the program
# Using 'w' parameter we make sure that if the file doesn't exist it is created. 
# It will also empty the content of the file every time the program is run.
my_file = open("analysis.txt", "w")
my_file.write("This file contains my analysis of the Iris dataset.\n\n")
# my_file.close

# Loading the data to the dataframe pd.
df = pd.read_csv('iris.csv')


# checking if we can write info to our text file.
my_file.write(df.head().to_string())
my_file.write("\n\n")
my_file.write(df.tail().to_string())

# print that all went well.
print("writing in the file was successful! ")

# append if in the text file.







# references:

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html