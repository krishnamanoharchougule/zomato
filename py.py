import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea   

df = pd.read_csv("Zomato-data.csv")
# print(df.head())

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
plt.ylabel('votes')
plt.show()

max_votes=df['votes'].max()
res_mv_name = df.loc[df['votes']==max_votes,'name']
print('Restaurant(s) with maximum votes:')
print(res_mv_name.iloc[0])

sea.countplot(x=df['book_table'])
plt.show()

plt.hist(df['rate'],bins=5)
plt.title('Ratings distribution')
plt.show()

sea.countplot(x=df['approx_cost(for two people)'])
plt.show()

tb = df.pivot_table(index='listed_in(type)',columns='online_order',aggfunc='size',fill_value=0)
sea.heatmap(tb,annot=True,cmap='YlGnBu', fmt='d')
plt.title('Heatmap')
plt.xlabel('Online order')
plt.ylabel('Listed_in(type)')
plt.show()