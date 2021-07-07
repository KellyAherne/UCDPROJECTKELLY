#import modules
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as ply
import seaborn as sns

#import dataset
telcodata = pd.read_csv("Telco_customer_churn_project.csv")
print(telcodata)

#import API:
apidata=requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=TEO&apikey=TGFBMIZEC0YHTT5W")


#str to dict using json
parsed_apidata=apidata.json()
print(type(parsed_apidata))
print(parsed_apidata)

print(telcodata.head())
print(telcodata.info())
print(telcodata.shape)
print(telcodata.describe())
print(telcodata.values)
print(telcodata.columns)
print(telcodata.index)
print(telcodata.sort_values(["TotalCharges", "gender"], ascending=[False, True]))