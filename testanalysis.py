# Programming and Scripting
# Task - Project
# This program is based on the well-known Fisher’s Iris data set.
# This program should:
# 1. Output a summary of each variable to a single text file,
# 2. Save a histogram of each variable to png files, and
# 3. Output a scatter plot of each pair of variables.
# 4. Perform any other analysis you think is appropriate.

# Author: Ermelinda Qejvani

# First I'm importing all libraries that I can use to work/manipulate data files
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
# Pearson's correlation coefficient.
from scipy.stats import pearsonr
from analysisFunctions import *
import warnings
warnings.filterwarnings("ignore", message="The figure layout has changed to tight")

################################################################################
####################        Working with the text file      ####################
################################################################################

# Creating a text file to write the data from running the program
# Using 'w' parameter we make sure that if the file doesn't exist it is created. 
# It will also empty the content of the file every time the program is run.

# calling the function create_empty_file to create the output file analysis.txt.
my_file = "analysis.txt"  
create_empty_file(my_file)
print(f"File '{my_file}' contains information about Iris DataSet and its variables.")

# Storing dataset into DataFrame (df). Defining variables to use in the program.
df = pd.read_csv("iris.csv", skip_blank_lines=True)
df_describe = df.describe(include="all")
df_types = df.dtypes
df_species = df["species"].value_counts()

# Creating subset for each dataset by species.
df_setosa = df[df["species"] == "setosa"]           
df_versicolor = df[df["species"] == "versicolor"]
df_virginica = df[df["species"] == "virginica"]


# Generating info from the dataset and writing in our file: analysis.txt
with open(my_file, 'a') as file:
    file.write("\nUsing command 'df.columns' we can get the Column labels of the DataSet which are:\n"
               "---------------------------------------------------------------------------------\n")
    for i, label in enumerate(df.columns):
        file.write(f"{i+1}. {label}\n")
    
    file.write("\n\nFinding out data types in the Dataset using 'df.dtypes' command:\n"
               "----------------------------------------------------------------\n" + df_types.to_string()) 
    file.write("\n\nMain species in the dataset using 'df['species'].value_count' command:\n"
               "----------------------------------------------------------------------\n"+ df_species.to_string())  
    file.write("\n\nSummary of the Iris dataset using 'df.describe()' command:\n"
               "----------------------------------------------------------\n")
    file.write(df_describe.to_string())
    file.write("\n\nPlease note that 'df.describe()' command gives us information about the whole dataset."
               "\nTo get a more accurate information about the different flower species I created subsets for each flower.\n") 
    file.write("\n\nThe next section shows the mean values of each variable in the dataset for each species.\n"
               "----------------------------------------------------------------------------------------"
               "\nI am using 'df.groupby('species')' command:\n"
               "-------------------------------------------\n")
    file.write((df.groupby("species").mean()).to_string())
    
    file.write("\n\nIn the next section I will use 'df_specie.describe()' command to get information about each of species.\n"
               "*******************************************************************************************************\n")
    file.write("\nSummary of Iris Setosa:\n-----------------------\n" + df_setosa.describe(include="all").to_string())
    file.write("\n\nSummary of Iris Versicolor:\n---------------------------\n" +df_versicolor.describe(include="all").to_string())
    file.write("\n\nSummary of Iris Virginica:\n--------------------------\n" + df_virginica.describe(include="all").to_string())
    


################################################################################
####################               Histogram                ####################
################################################################################

# Histogram of all 4 variables comparing by species

create_iris_histograms(df)

save_iris_pairplot(df)

species_pairplot_to_folder(df_setosa, "Setosa")               # Relationship of variables in Iris Setosa.
species_pairplot_to_folder(df_versicolor, "Versicolor")       # Relationship of variables in Iris Versicolor.
species_pairplot_to_folder(df_virginica, "Virginica")         # Relationship of variables in Iris Virginica.