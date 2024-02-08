import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

house_data = pd.read_csv('housing.csv')


print("Sample of the House Dataset:")
print(house_data.head())

stats=house_data.describe()
print("\nSummary Stats")
print(stats)

plt.figure(figsize=(10, 6))
plt.hist(house_data['median_house_value'], bins=20, color='skyblue', edgecolor='black')
plt.title('Median House Value Distribution')
plt.xlabel('Median House Value')
plt.ylabel('Frequency')
plt.show()

plt.scatter(house_data['longitude'], house_data['latitude'], alpha=0.4, s=house_data['population']/100, c=house_data['median_house_value'], cmap=plt.get_cmap('jet'))
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Geospatial Distribution of Housing Prices')
plt.colorbar(label='Median House Value')
plt.show()


plt.scatter(house_data['median_income'], house_data['median_house_value'], alpha=0.5)
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.title('Relationship between Median Income and Median House Value')
plt.show()

plt.figure(figsize=(12, 8))
sns.boxplot(x='ocean_proximity', y='median_house_value', data=house_data)
plt.title('Box Plot of Median House Value by Ocean Proximity')
plt.show()
