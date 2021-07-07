#import modules
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as ply
import seaborn as sns


#import API:
apidata=requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=TEO&apikey=TGFBMIZEC0YHTT5W")

#API str to dict using json
parsed_apidata=apidata.json()
print(type(parsed_apidata))
print(parsed_apidata)


#import dataset
telcodata = pd.read_csv("Telco_customer_churn_project.csv")
print(telcodata)
print(telcodata.head())
print(telcodata.info())
print(telcodata.shape)

#check for missing values/duplicates
telcomissing = telcodata.isna().any()
print(telcomissing)

telcoduplicate = telcodata.duplicated(subset=None, keep="first")
print(telcoduplicate)

#seperate male and female customers into 2 datasets with specific columns sorted by total charges
malecustomers = telcodata[telcodata["gender"]== "Male"]
femalecustomers = telcodata[telcodata["gender"]== "Female"]

malecustomers1 = malecustomers[["customerID", "gender", "tenure", "DeviceProtection", "Contract", "PaperlessBilling", "MonthlyCharges", "TotalCharges"]]
femalecustomers1 = femalecustomers[["customerID", "gender", "tenure", "DeviceProtection", "Contract", "PaperlessBilling", "MonthlyCharges", "TotalCharges"]]

maletotalchgs = malecustomers1.sort_values("TotalCharges", ascending=False)
femaletotalchgs = femalecustomers1.sort_values("TotalCharges", ascending=False)

print(maletotalchgs)
print(femaletotalchgs)








