#import modules
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as ply
import seaborn as sns


#import API Telco stock info:
apidata=requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=TEO&apikey=TGFBMIZEC0YHTT5W")

#API str to dict using json
parsed_apidata=apidata.json()
print(type(parsed_apidata))
print(parsed_apidata)

#import dataset and view info
telcodata = pd.read_csv("Telco_customer_churn_project.csv")
print(telcodata.head())
print(telcodata.info())
print(telcodata.shape)
print(telcodata.describe(include="all"))

#check for missing values/duplicates
telcomissing = telcodata.isna().any()
print(telcomissing)

#update Total Charges column to numeric
telcodata["TotalCharges"] = pd.to_numeric(telcodata.TotalCharges, errors="coerce")
print(telcodata.TotalCharges.isnull().sum())

#print null values to check for pattern
print(telcodata[np.isnan(telcodata["TotalCharges"])])

#tenure = 0,
print(telcodata[telcodata['tenure'] == 0][['tenure','TotalCharges']])

#update missing TotalCharges to be 0
print(telcodata.fillna(0, inplace=True))
print(telcodata.shape)

telcoduplicate = telcodata.duplicated(subset=None, keep="first")
print(telcoduplicate)

#seperate male and female customers into 2 datasets with specific columns sorted by total charges
malecustomers = telcodata[telcodata["gender"]== "Male"]
femalecustomers = telcodata[telcodata["gender"]== "Female"]

malecustomers1 = malecustomers[["customerID", "gender", "tenure", "DeviceProtection", "Contract", "PaperlessBilling", "MonthlyCharges", "TotalCharges"]]
femalecustomers1 = femalecustomers[["customerID", "gender", "tenure", "DeviceProtection", "Contract", "PaperlessBilling", "MonthlyCharges", "TotalCharges"]]

malemonthlychgs = malecustomers1.sort_values("MonthlyCharges", ascending=False)
femalemonthlychgs = femalecustomers1.sort_values("MonthlyCharges", ascending=False)

print(malemonthlychgs)
print(femalemonthlychgs)

#use iterrows to show all headings before MonthlyCharges on teh malecustomers1 list
for x in malecustomers1:
    print (x)
    if x == "MonthlyCharges":
        break

#split into monthly charges categories by amount
malemonthlychgscategorized = pd.cut(malemonthlychgs["MonthlyCharges"], bins=[0, 25, 50, 75, 100, 125], include_lowest=True, labels=["low", "quite low", "mid", "quite high", "high"])
print(malemonthlychgscategorized)

femalemonthlychgscategorized = pd.cut(femalemonthlychgs["MonthlyCharges"], bins=[0, 25, 50, 75, 100, 125], include_lowest=True, labels=["low", "quite low", "mid", "quite high", "high"])
print(femalemonthlychgscategorized)

MaleCategories = []

for i in malemonthlychgs["MonthlyCharges"]:

    if (i < 25):
        MaleCategories.append("Low")

    elif (i > 25) & (i < 50):
        MaleCategories.append("Quite Low")

    elif (i > 50 ) & (i < 75):
        MaleCategories.append("Mid")

    elif (i > 75 ) & (i < 100):
        MaleCategories.append("Quite High")

    elif (i > 100 ) & (i < 125):
        MaleCategories.append("High")

print(MaleCategories)

MaleCategories2 = pd.DataFrame(MaleCategories, columns=["MonthlyCharges"])
print(MaleCategories2)

FemaleCategories = []

for i in femalemonthlychgs["MonthlyCharges"]:

    if (i < 25):
        FemaleCategories.append("Low")

    elif (i > 25) & (i < 50):
        FemaleCategories.append("Quite Low")

    elif (i > 50 ) & (i < 75):
        FemaleCategories.append("Mid")

    elif (i > 75 ) & (i < 100):
        FemaleCategories.append("Quite High")

    elif (i > 100 ) & (i < 125):
        FemaleCategories.append("High")

print(FemaleCategories)

FemaleCategories2 = pd.DataFrame(FemaleCategories, columns=["MonthlyCharges"])
print(FemaleCategories2)

#graph no of customers in each category