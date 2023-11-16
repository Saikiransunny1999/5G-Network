import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv(r"D:\project\flask\5g_coverage_worldwide.csv")

data.head(10)

data.shape

data.info()

data.isna().sum()

for f in data.columns:
    print(f, data[f].nunique())

duplicated=data.duplicated().sum()
print('Total duplicates:', duplicated)

duplicates=data[data.duplicated(keep=False)]
duplicates.head(10)

data['deployment_type'].value_counts

data['deployment_type'] = data['deployment_type'].replace({'5GNR': '5G NR', '5g NR': '5G NR', '5G': '5G NR', '5N NR': '5G NR'})

status_counts = data['status'].value_counts()
status_counts

top_10_operators = data['operator'].value_counts().head(10)

plt.figure(figsize=(10, 8))
sns.barplot(x=top_10_operators.index, y=top_10_operators.values)
plt.xticks(rotation=45)  


plt.title('Top 10 Operators with the Most Active 5G Networks')
plt.xlabel('Operator')
plt.ylabel('Number of Active 5G Networks')

plt.show()

top_10_city = data['city_name'].value_counts().head(10)

plt.figure(figsize=(10, 8))
sns.barplot(x=top_10_city.index, y=top_10_city.values)
plt.xticks(rotation=45)  


plt.title('Top 10 Cities with the Most Active 5G Networks')
plt.xlabel('City')
plt.ylabel('Number of Active 5G Networks')


plt.show()


plt.figure(figsize=(10, 8))
plt.scatter(data['longitude'], data['latitude'], s=20, c='blue', marker='o', alpha=0.5)

plt.title('5G Network Map')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)


plt.show()


status_value = data['status'].value_counts()

plt.figure(figsize=(10, 6))
ax = status_value.plot(kind='bar')

total = status_value.sum()
for i, v in enumerate(status_value):
    porcentaje = (v / total) * 100
    ax.text(i, v + 2000, f'{porcentaje:.2f}%', ha='center')


plt.title('Status Distribution Count')
plt.xlabel('Status')
plt.ylabel('Count')
plt.xticks(rotation=0)  

plt.show()


data_top_10 = data[data['operator'].isin(top_10_operators.index)]

plt.figure(figsize=(10, 8))


plt.scatter(data['longitude'], data['latitude'], s=20, c='blue', marker='o', alpha=0.5, label='Other Operators')


plt.scatter(data_top_10['longitude'], data_top_10['latitude'], s=20, c='yellow', marker='o', alpha=0.5, label='Top 10 Operators')

plt.title('5G Network Map with Top 10 Operators Highlighted')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.legend()

# Muestra el gráfico
plt.show()













