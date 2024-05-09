# This file contains functions for main file analysis.txt
import seaborn as sns 
import matplotlib.pyplot as plt 

def create_empty_file(my_file):
    # Open the file in 'write' mode ('w'). If the file doesn't exist, it will be created.
    # If the file already exists, its contents will be overwritten.
    with open(my_file, 'w') as file:
        # Write a message as the First line of the text file.
        file.write("This is my analysis of Iris DataSet.\n\nIris data set is a collection of measurements taken from three species of Iris flowers: "
                   "\na. Iris Setoza.\nb. Iris Versicolor.\nc. Iris Virginica.\n"
                   "\nThe dataset is widely used in the field of data science, making it an excellent resource for teaching and learning."
                   "\nEach species studied in the dataset has 50 samples, and four measurements:\na. sepal length.\nb. sepal width.\nc. petal length.\nd. petal width.\n"
                   "\nThe aim of this program is to show what information we can get from the dataset using Python programming language and its libraries.\n\n") 


# Function to generate and save pairplot for a given species.
# df = DataFrame, species = name of species as string, save_dir = Directory to save the plots.
def species_pairplot_to_file(df, species_name, save_dir="./IrisGraphs/"):
   
    sns.pairplot(df, height=1.5)                         # Create pairplot for the given species.
    plt.suptitle(f"Iris {species_name} variables")       # Set title for the pairplot.
    save_path = f"{save_dir}/Iris{species_name}Variables.png"     # Create path and file name of pairplot.
    plt.savefig(save_path)                                        # Save the plot.
    plt.close()                                          # Close the plot to free up memory
    






