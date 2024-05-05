
## Programming and Scripting - Project

Author: Ermelinda Qejvani

***
![Iris Setosa](/images/Iris_setosa.jpg)  ![Iris Versicolor](/images/Iris_versicolor.jpg)   ![Iris Virginica](/images/Iris_virginica.jpg)

[Photo Source: Wikipedia](https://commons.wikimedia.org/wiki/File:Kosaciec_szczecinkowaty_Iris_setosa.jpg)

This README has been written with [GitHub's documentation on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) in mind.
You should refer to that documentation for more information on writing an appropriate README for visitors to your repository.
You can find out more about [writing in MarkDown in GitHub's documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

***
## About this project

This project is a study about Iris flower data set, or Fisher's Iris data set - a collection of measurements taken from three species of Iris flowers. Ronald Fisher, a British statistician and biologist, introduced this data set in 1936 to demonstrate linear discriminant analysis. Edgar Anderson collected the data to study the morphological differences among the Iris species. Each species has 50 samples, and four measurements—sepal length, sepal width, petal length, and petal width—were recorded for each sample. Fisher used these measurements to create a model that can distinguish between the different Iris species. His work was published in the _Annals of Eugenics_, now known as the _Annals of Human Genetics_. [Source: Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set)




## Use of this project



## Get Started

List of possible extra commands I can use for variable's summary (analysis.txt):

1. getting min, max and sum of the variables:
    - numpy: print(big_array.min(), big_array.max(), big_array.sum()) 
    - https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html
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
3. 

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


## Get Help



## Contribute



## Author


Iris data set file iris.csv uploaded from:
https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

