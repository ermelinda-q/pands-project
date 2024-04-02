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