import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea   

df = pd.read_csv("Zomato-data.csv")
# print(df.head())
df['votes'] = pd.to_numeric(df['votes'], errors='coerce')

def handleRate(value):
    value=str(value).split('/')
    value=value[0]
    return float(value)

df['rate']=df['rate'].apply(handleRate)
# print(df.head())

# df.info()
# print(df.isnull().sum())

sea.countplot(x=df['listed_in(type)'])
plt.xlabel('Type of Restaurent')
plt.show()

grouped_data = df.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes':grouped_data})
plt.plot(result,c='red',marker='o')
plt.xlabel('Type of restaurant')
plt.ylabel('No of User Votes')
plt.show()

max_votes=df['votes'].max()
res_mv_name = df.loc[df['votes']==max_votes,'name']
print('Restaurant(s) with maximum votes:')
print(res_mv_name.values[0], max_votes)

sea.countplot(x=df['online_order'])
plt.xlabel('Does restaurant allow online orders')
plt.show()

plt.hist(df['rate'],bins=5)
plt.title('Ratings distribution')
plt.xlabel('Rating Value')
plt.ylabel('Frequency of Rating')
plt.show()

sea.countplot(x=df['approx_cost(for two people)'])
plt.ylabel('Frequency')
plt.show()

tb = df.pivot_table(index='listed_in(type)',columns='online_order',aggfunc='size',fill_value=0)
sea.heatmap(tb,annot=True,cmap='YlGnBu', fmt='d')
plt.title('Heatmap')
plt.xlabel('Online orders accepted')
plt.ylabel('Type of Restaurant')
plt.show()