#import modules
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import seaborn as sns


#import API Telco stock info:
apidata=requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=TEO&apikey=TGFBMIZEC0YHTT5W")

#API str to dict using json
parsed_apidata=apidata.json()
print(type(parsed_apidata))
print(parsed_apidata)

#import dataset and view info
telcodata = pd.read_csv("Telco_customer_churn_project.csv")
print(telcodata.head(5))
print(telcodata.info())
print(telcodata.shape)
print(telcodata.describe(include="all"))

#check for missing values
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

#check for missing duplicates
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

#use iterrows to show all headings before MonthlyCharges on the malecustomers1 list
for x in malecustomers1:
    print (x)
    if x == "MonthlyCharges":
        break

#split into monthly charges categories by amount
malemonthlychgscategorized = pd.cut(malemonthlychgs["MonthlyCharges"], bins=[0, 25, 50, 75, 100, 125], include_lowest=True, labels=["1-low-M", "2-quite low-M", "3-mid-M", "4-quite high-M", "5-high-M"])
print(malemonthlychgscategorized)

femalemonthlychgscategorized = pd.cut(femalemonthlychgs["MonthlyCharges"], bins=[0, 25, 50, 75, 100, 125], include_lowest=True, labels=["1-low-F", "2-quite low-F", "3-mid-F", "4-quite high-F", "5-high-F"])
print(femalemonthlychgscategorized)

MaleCategories = []

for i in malemonthlychgs["MonthlyCharges"]:

    if (i < 25):
        MaleCategories.append("1-Low-M")

    elif (i > 25) & (i < 50):
        MaleCategories.append("2-Quite Low-M")

    elif (i > 50 ) & (i < 75):
        MaleCategories.append("3-Mid-M")

    elif (i > 75 ) & (i < 100):
        MaleCategories.append("4-Quite High-M")

    elif (i > 100 ) & (i < 125):
        MaleCategories.append("5-High-M")

print(MaleCategories)

MaleCategories2 = pd.DataFrame(MaleCategories, columns=["MonthlyChargesGroup"])
print(MaleCategories2)

FemaleCategories = []

for i in femalemonthlychgs["MonthlyCharges"]:

    if (i < 25):
        FemaleCategories.append("1-Low-F")

    elif (i > 25) & (i < 50):
        FemaleCategories.append("2-Quite Low-F")

    elif (i > 50 ) & (i < 75):
        FemaleCategories.append("3-Mid-F")

    elif (i > 75 ) & (i < 100):
        FemaleCategories.append("4-Quite High-F")

    elif (i > 100 ) & (i < 125):
        FemaleCategories.append("5-High-F")

print(FemaleCategories)

FemaleCategories2 = pd.DataFrame(FemaleCategories, columns=["MonthlyChargesGroup"])
print(FemaleCategories2)

# Calculate the number of male and female customers
def somecalculation(x):
    return (telcodata['gender'] == x).sum()

print(somecalculation('Male'))
print(somecalculation('Female'))


#Totals of male and female by category

Maletotals = MaleCategories2.groupby("MonthlyChargesGroup")["MonthlyChargesGroup"].count()
print(Maletotals)

Femaletotals = FemaleCategories2.groupby("MonthlyChargesGroup")["MonthlyChargesGroup"].count()
print(Femaletotals)

# Merge dataframes
male = malecustomers1.merge(malemonthlychgscategorized, how="inner", left_index=True, right_index=True)
female = femalecustomers1.merge(femalemonthlychgscategorized, how="inner", left_index=True, right_index=True)

# Check row and column amounts to ensure no data is lost
print(male.shape)
print(male.head)
print(female.shape)
malefemale = pd.concat([male, female])
print(malefemale.shape)


# creating the dataset
data = {'1-Low-M': 714, '2-Quite Low-M': 461, '3-Mid-M': 813,
        '4-Quite High-M': 1104, '5-High-M' : 441}
category = list(data.keys())
amount = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(category, amount, color='maroon',
        width=0.4)

plt.xlabel("Category")
plt.ylabel("No. customers in category")
plt.title("Male customers monthly spend")
plt.show()

# creating the dataset
data = {'1-Low-M': 675, '2-Quite Low-M': 427, '3-Mid-M': 803,
        '4-Quite High-M': 1108, '5-High-M' : 461}
category = list(data.keys())
amount = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(category, amount, color='blue',
        width=0.4)

plt.xlabel("Category")
plt.ylabel("No. customers in category")
plt.title("Female customers monthly spend")
plt.show()


