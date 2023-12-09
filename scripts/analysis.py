import pandas as pd
import matplotlib.pyplot as plt

#Reading in the csv as a dataframe and adding in identifying columns to the dataframe
df = pd.read_csv(r'/Users/edward/is477-fall2023-final-project/data/car+evaluation/car.data')
df.columns = ['buying_price', 'maintenance', 'doors', 'persons', 'luggage_boot', 'safety', 'class_value']

#Describing summary stats for the car dataset
summary_stats = df.describe()
summary_stats.to_csv('results/summary_stats.csv')

#Calulcating the frequency of each car classification based on the maintenance cost value and their class value
#Then storing the different frequencies into a new dataframe
maintenance_class_value = pd.crosstab(df['maintenance'], df['class_value'])
maintenance_class_value.to_csv('results/maintenance_class_value_distribution.csv')

#Creating a stacked bar chart to illustrate the distribution of maintenance cost values compared to class values
maintenance_class_value.plot(kind='bar', stacked=True)
plt.title('Maintenance Cost vs Class Value')
plt.xlabel('Maintenance Cost')
plt.ylabel('Number of Cars')
plt.savefig('results/maintenance_cost_class_value_chart.png')