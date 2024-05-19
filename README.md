# Python and the Iris Dataset.

## Programming and Scripting - Project

#### by Ermelinda Qejvani

***
![Iris Setosa](/images/Iris_setosa.jpg)  ![Iris Versicolor](/images/Iris_versicolor.jpg)   ![Iris Virginica](/images/Iris_virginica.jpg)

[Photo Source: Wikipedia](https://commons.wikimedia.org/wiki/File:Kosaciec_szczecinkowaty_Iris_setosa.jpg)

This README has been written with [GitHub's documentation on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind.
You should refer to that documentation for more information on writing an appropriate README for visitors to your repository.
You can find out more about [writing in MarkDown in GitHub's documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

***
## About this repository

This git repository (pands-project) holds all the files of Programming and Scripting module project, as part of my [Hdip in Computer Science in Data Analytics](https://www.gmit.ie/higher-diploma-in-science-in-computing-in-data-analytics#:~:text=You%20are%20a%20Level%208,topics%20in%20your%20original%20degree.) in [ATU](https://www.gmit.ie/).

_Files and Folders in this repository:_

_Files:_

- `analysis.py` - main file to run the program.
- `analysisFunctions.py` - storing the following functions:
    - `create_empty_file`: creates analysis.txt file.
    - `create_iris_histograms`: generates VariablesHistogram.png to folder IrisGraphs.
    - `species_pairplot_to_folder`: generates pairplot graph of relations between variables in a given iris flower, e.g. IrisSetosaVariables.png
    - `save_iris_pairplot`: generates a pairplot graph of all variables in the DataFrame.
    - `plot_iris_petal_or_sepal`: generates a pairplot graph of variables for just petals or sepals.
- `bestFitLineMenu.py`:
    - creates a submenu to get users input of which variables to calculate/display graph of Best Fit Line.
    - function `best_fit_line` that plots the graph of input variables and adds the best fit line.
- `correlation.py` - holds two functions:
    - `calculate_correlation`: calculates the correlation between the variable values of the dataset.
    - `write_correlation_to_file`: creates and stores a list of tuples, output from calculate_correlation, sorts it, and writes the output in `correlation_results.txt`.
- `analysis.txt` - a text file created when the program starts.
- `correlation_results.txt` - generated by correlation.py file.
- `iris.scv` - downloaded from [Michael Waskom on GitHub](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv).
- a `.gitignore` file.
- This `README` file.

_Folders:_

- `IrisGraphs` - holds 7 .png file generated from the program (when all options of program are run).
    - `BestFitLine` - a subfolder where 6 .png files of graphs of plots with a best fit line are stored.
- `images` - holds three .jpg files of iris species analyzed in this project.

***
## About this project

This project is a study about Iris flower data set, or Fisher's Iris data set - a collection of measurements taken from three species of Iris flowers. Ronald Fisher, a British statistician and biologist, introduced this data set in 1936 to demonstrate linear discriminant analysis. Edgar Anderson collected the data to study the morphological differences among three Iris species: Iris Setosa, Iris Versicolor and Iris Virginica. Each species has 50 samples, and four measurements—sepal length, sepal width, petal length, and petal width—were recorded for each sample. Fisher used these measurements to create a model that can distinguish between the different Iris species. His work was published in the _Annals of Eugenics_, now known as the _Annals of Human Genetics_. [Source: Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set)

***
## Use of this project

The aim of this project is to develop a Python program that demonstrates various techniques for exploring, modifying, and analyzing data from the Iris dataset.

***
## Get Started

To run the files stored in this repository you will need to download and install in your computer the following apps:

- [Anaconda](https://www.anaconda.com/) - open-source platform that allows you to write and execute code in Python. A guide how to install Anaconda in your computer can be found [here](https://docs.anaconda.com/free/anaconda/install/index.html).
- [Visual Studio Code](https://code.visualstudio.com/) - source code editor for developers. With Visual Studio Code you can open and run all python files(ending with .py). A guide how to install and setup Visual Studio Code in your computer can be found [here](https://code.visualstudio.com/learn/get-started/basics).
- [Git](https://git-scm.com/downloads) - will help you to download a copy of this repository in your local machine. Installation guide can be found [here](https://github.com/git-guides/install-git).

To make a copy of this repository in your computer/local machine run the following command:

```
git clone https://github.com/ermelinda-q/pands-project.git
```
***
## Python program description

I created this program to show fifth-year computer science class at our school how Python can analyze data from .csv files. To make it easier to understand, I added a menu so users can easily navigate and learn how everything works.
![Main Menu](./images/main-menu.png)





List of possible extra commands I can use for variable's summary (analysis.txt):
1. Adding a menu.

2. Sorting the array of each variable????
    - numpy:
    def bogosort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x
    x = np.array([2, 1, 4, 3, 5])
    bogosort(x)
    - or np.sort()
    - https://jakevdp.github.io/PythonDataScienceHandbook/02.08-sorting.html

List of possible commands for plotting (pyplot):

1. K-nearest neighbors:
     - https://jakevdp.github.io/PythonDataScienceHandbook/02.08-sorting.html
2. Plotting with matplot library:
    - https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html
    - Saving figures to file:
    fig.savefig('my_figure.png')
    - To confirm that it contains what we think it contains, let's use the IPython Image object to display the contents of this file:
    ' from IPython.display import Image
    ' Image('my_figure.png')
    https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html
    - scatter plots:
    https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html
    - Histograms:
    https://jakevdp.github.io/PythonDataScienceHandbook/04.05-histograms-and-binnings.html
    - Seaborn:
    https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html
    - Machine Learning:
    https://jakevdp.github.io/PythonDataScienceHandbook/05.01-what-is-machine-learning.html
    https://jakevdp.github.io/PythonDataScienceHandbook/05.03-hyperparameters-and-model-validation.html
    https://jakevdp.github.io/PythonDataScienceHandbook/05.06-linear-regression.html
3. Save all .png files to a .pdf file????

## Get Help



## Contribute



## Author


Iris data set file iris.csv uploaded from:
https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

