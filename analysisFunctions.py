# This file contains functions for main file analysis.txt
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 
import os

def create_empty_file(my_file):
    # Open the file in 'write' mode ('w'). If the file doesn't exist, it will be created.
    # If the file already exists, its contents will be overwritten.
    try:
        with open(my_file, 'w') as file:
        # Write a message as the First line of the text file.
            file.write("This is my analysis of Iris DataSet.\n\nIris data set is a collection of measurements taken from three species of Iris flowers: "
                   "\na. Iris Setoza.\nb. Iris Versicolor.\nc. Iris Virginica.\n"
                   "\nThe dataset is widely used in the field of data science, making it an excellent resource for teaching and learning."
                   "\nEach species studied in the dataset has 50 samples, and four measurements:\na. sepal length.\nb. sepal width.\nc. petal length.\nd. petal width.\n"
                   "\nThe aim of this program is to show what information we can get from the dataset using Python programming language and its libraries."
                   "\n************************************************************************************************************************************\n") 
        print(f"File '{my_file}' successfully created.")
    except Exception as e:
        print("Error saving information to file:", str(e))

# Function to generate and save pairplot for a given species.
# df = DataFrame, species = name of species as string, save_dir = Directory to save the plots.
def species_pairplot_to_folder(df, species_name, save_dir="./IrisGraphs/"):
    try:
        sns.pairplot(df, height=1.5)                         # Create pairplot for the given species.
        plt.suptitle(f"Iris {species_name} variables")       # Set title for the pairplot.
        save_path = f"{save_dir}/Iris{species_name}Variables.png"     # Create path and file name of pairplot.
        plt.savefig(save_path)                                        # Save the plot.
        plt.close()                                          # Close the plot to free up memory
        print(f"Iris {species_name} pairplot successfully saved in {save_dir} directory.")
    except Exception as e:
        print("Error generating pairplot:", str(e))
        
        

####
####

def create_iris_histograms(df):
    try:
        # Create a 2x2 grid of subplots
        fig1, axes = plt.subplots(2, 2, figsize=(12, 12))

        # Plot histograms for each feature with hue based on species
        sns.histplot(data=df, x="sepal_length", hue="species", ax=axes[0, 0]).set_title("Sepal Length")
        sns.histplot(data=df, x="sepal_width", hue="species", ax=axes[0, 1]).set_title("Sepal Width")
        sns.histplot(data=df, x="petal_length", hue="species", ax=axes[1, 0]).set_title("Petal Length")
        sns.histplot(data=df, x="petal_width", hue="species", ax=axes[1, 1]).set_title("Petal Width")

        # Set the main title for the figure
        plt.suptitle("Histogram of Iris flowers")

        # Save the figure to a file
        plt.savefig("./IrisGraphs/VariablesHistogram.png")
        print("Histogram of Iris DataSet successfully saved as VariablesHistogram in ./IrisGraphs/ directory.")
    except Exception as e:
        print("Error generating histogram:", str(e))
        


def save_iris_pairplot(df, save_dir="./IrisGraphs/", filename="PairPlotOfVariables.png"):
    # Ensure the save directory exists
    os.makedirs(save_dir, exist_ok=True)
    try:
        # Create the pairplot
        sns.pairplot(df, hue='species', height=1.5)
        
        # Add a title
        plt.suptitle("Relationship between Iris dataset variables", fontsize=10)
        
        # Save the plot to the specified directory
        filepath = os.path.join(save_dir, filename)
        plt.savefig(filepath)
        
        # Close the plot to free up memory
        plt.close()
        
        print(f"Pairplot of Iris DataSet variables successfully saved as {filename} in {save_dir} directory.")
    except Exception as e:
        print(f"An error occurred while creating or saving the pairplot: {e}")






