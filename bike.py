
import pandas
#import numpy 
import matplotlib.pyplot as plt
import seaborn as sns

# Loading data
dataset = pd.read_csv('day.csv')
print(dataset.head())

# Information about the data

print(dataset.info)