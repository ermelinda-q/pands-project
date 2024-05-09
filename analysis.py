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
from skimpy import skim, generate_test_data
from analysisFunctions import *
import warnings
warnings.filterwarnings("ignore", message="The figure layout has changed to tight")

#########################################################################
###############        Working with the text file         ###############
#########################################################################
# Creating a text file to write the data from running the program
# Using 'w' parameter we make sure that if the file doesn't exist it is created. 
# It will also empty the content of the file every time the program is run.

# calling the function create_empty_file to create the output file analysis.txt.
my_file = "analysis.txt"  
create_empty_file(my_file)
print(f"\nAnalyzing Iris DataSet.\nA file named '{my_file}' is created to store all analysis data.\n")


df = pd.read_csv("iris.csv", skip_blank_lines=True)
df_describe = df.describe(include="all")
df_types = df.dtypes
df_species = df["species"].value_counts()
df_setosa = df[df["species"] == "setosa"]
df_versicolor = df[df["species"] == "versicolor"]
df_virginica = df[df["species"] == "virginica"]


# Generating info from the dataset and writing in our file: analysis.txt
with open(my_file, 'a') as file:
    file.write("\n\nColumn labels of the iris DataFrame are:\n")
    for i, label in enumerate(df.columns):
        file.write(f"{i+1}. {label}\n")
    
    file.write("\n\nData types in this Dataset:\n\n" + df_types.to_string()) 
    file.write("\n\nMain species in the dataset:\n\n" + df_species.to_string())  
    file.write("\n\nSummary of the Iris dataset:\n\n")
    file.write(df_describe.to_string())
    
    file.write("\n\nThe next section shows the mean values of each variable in the dataset for each species.\n")
    file.write((df.groupby("species").mean()).to_string())
    
    
    file.write("\n\nSummary of Iris Setosa:\n\n" + df_setosa.describe(include="all").to_string())
    file.write("\n\nSummary of Iris Versicolor:\n\n" +df_versicolor.describe(include="all").to_string())
    file.write("\n\nSummary of Iris Virginica:\n\n" + df_virginica.describe(include="all").to_string())
    


########################################################
###############        Histograms        ###############
######################################################## 

# Histogram of all 4 variables comparing by species

fig, axes = plt.subplots(2, 2)
sns.histplot(data=df, x="sepal_length", hue="species", ax=axes[0,0]).set_title("Sepal Length")
sns.histplot(data=df, x="sepal_width", hue="species", ax=axes[0,1]).set_title("Sepal Width")
sns.histplot(data=df, x="petal_length", hue="species", ax=axes[1,0]).set_title("Petal Length")
sns.histplot(data=df, x="petal_width", hue="species", ax=axes[1,1]).set_title("Petal Width")

plt.savefig("./IrisGraphs/VariablesHistogram.png")


##############################################################
##############      Pairplot      ############################
##############################################################

# Relationship of our variables on the dataset.
sns.pairplot(df, hue='species', height=1.5)
plt.suptitle("Relationship between Iris dataset variables", fontsize=10)
plt.savefig("./IrisGraphs/DatasetVariables.png")
plt.close()

# Calling species_pairplot_to_file function from analysisFunctions file
species_pairplot_to_file(df_setosa, "Setosa")               # Relationship of variables in Iris Setosa.
species_pairplot_to_file(df_versicolor, "Versicolor")       # Relationship of variables in Iris Versicolor.
species_pairplot_to_file(df_virginica, "Virginica")         # Relationship of variables in Iris Virginica.


# Relationship of petal_length and petal_width, all three species.

fig, ax = plt.subplots()
fig.set_size_inches(10, 5) # adjusting the length and width of plot

# lables and scatter points
ax.scatter(df_setosa['petal_length'], df_setosa['petal_width'], label="Setosa", facecolor="blue")
ax.scatter(df_versicolor['petal_length'], df_versicolor['petal_width'], label="Versicolor", facecolor="green")
ax.scatter(df_virginica['petal_length'], df_virginica['petal_width'], label="Virginica", facecolor="red")


ax.set_xlabel("petal length")
ax.set_ylabel("petal width")
ax.grid()
ax.set_title("Iris petals")
ax.legend()
plt.savefig("./IrisGraphs/IrisPetals.png")
plt.close()

# Relationship between sepal_length and sepal_width of three species.

fig, ax = plt.subplots()
fig.set_size_inches(10, 5) # adjusting the length and width of plot

# lables and scatter points
ax.scatter(df_setosa['sepal_length'], df_setosa['sepal_width'], label="Setosa", facecolor="blue")
ax.scatter(df_versicolor['sepal_length'], df_versicolor['sepal_width'], label="Versicolor", facecolor="green")
ax.scatter(df_virginica['sepal_length'], df_virginica['sepal_width'], label="Virginica", facecolor="red")


ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.grid()
ax.set_title("Iris Sepals")
ax.legend()
plt.savefig("./IrisGraphs/Iris Sepals")
plt.close()


# references:

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# https://realpython.com/python-csv/
# https://python-course.eu/numerical-programming/reading-and-writing-data-in-pandas.php
# https://geo-python.github.io/site/notebooks/L5/exploring-data-using-pandas.html
# https://www.pluralsight.com/resources/blog/guides/scikit-machine-learning

# variables to use for graphs by species maybe later?????
'''
set_sepal_length_mean = round(df_setosa["sepal_length"].mean(), 3)
set_sepal_width_mean = round(df_setosa["sepal_width"].mean(), 3)
set_petal_length_mean = round(df_setosa["petal_length"].mean(), 3)
set_petal_width_mean = round(df_setosa["petal_width"].mean(), 3)

ver_sepal_length_mean = round(df_versicolor["sepal_length"].mean(), 3)
ver_sepal_width_mean = round(df_versicolor["sepal_width"].mean(), 3)
ver_petal_length_mean = round(df_versicolor["petal_length"].mean(), 3)
ver_petal_width_mean = round(df_versicolor["petal_width"])

virg_sepal_length_mean = round(df_virginica["sepal_length"].mean(), 3)
virg_sepal_width_mean = round(df_virginica["sepal_width"].mean(), 3)
virg_petal_length_mean = round(df_virginica["petal_length"].mean(), 3)
virg_petal_width_mean = round(df_virginica["petal_width"].mean(), 3)
'''