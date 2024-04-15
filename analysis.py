import pandas as pd
import matplotlib.pyplot as plt

# Load the iris dataset
iris = pd.read_csv('data/iris.data')

# Rename the columns
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

#Group the data by species
grouped_data = iris.groupby('species')

#Outputs a summary of each variable to a single text file
print(grouped_data.describe().to_string(), file=open('iris.summary.txt', 'w'))

#Saves a histogram of each variable to png files
for species, species_data in grouped_data:
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    fig.suptitle(f'{species} Histograms')
    for i, column in enumerate(iris.columns[:4]):
        ax = axs[i // 2, i % 2]
        ax.hist(species_data[column])
        ax.set_title(column)
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')
    plt.savefig(f'{species}_histograms.png')
    plt.close()

#Performs any other analysis you think is appropriate
    #Box and Whisker Plots
iris.boxplot(by='species', figsize=(10, 10))
plt.savefig('iris_boxplot.png')