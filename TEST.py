import pandas as pd

data=pd.read_csv("netflix_titles.csv")

new_Data=data.fillna(data.mean)
print(new_Data.isnull().sum())
print(data.shape, new_Data.shape)