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

# where tenure = 0, total charges also = 0.
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
for x in malemonthlychgs:
    print (x)
    if x == "MonthlyCharges":
        break

#split into monthly charges categories by amount
malemonthlychgscategorized = pd.cut(malemonthlychgs["MonthlyCharges"], bins=[0, 25, 50, 75, 100, 125], include_lowest=True, labels=["1-low-M", "2-quite low-M", "3-mid-M", "4-quite high-M", "5-high-M"])
print(malemonthlychgscategorized)

femalemonthlychgscategorized = pd.cut(femalemonthlychgs["MonthlyCharges"], bins=[0, 25, 50, 75, 100, 125], include_lowest=True, labels=["1-low-F", "2-quite low-F", "3-mid-F", "4-quite high-F", "5-high-F"])
print(femalemonthlychgscategorized)

# define male categories using elif
MaleCategories = []
for i in malemonthlychgs["MonthlyCharges"]:

    if (i < 25):
        MaleCategories.append("1-Low-M")

    elif (i >= 25) & (i < 50):
        MaleCategories.append("2-Quite Low-M")

    elif (i >= 50 ) & (i < 75):
        MaleCategories.append("3-Mid-M")

    elif (i >= 75 ) & (i < 100):
        MaleCategories.append("4-Quite High-M")

    elif (i >= 100 ) & (i <= 125):
        MaleCategories.append("5-High-M")

print(MaleCategories)

MaleCategories2 = pd.DataFrame(MaleCategories, columns=["MonthlyChargesGroup"])
print(MaleCategories2)

# define female categories using elif
FemaleCategories = []

for i in femalemonthlychgs["MonthlyCharges"]:

    if (i < 25):
        FemaleCategories.append("1-Low-F")

    elif (i >= 25) & (i < 50):
        FemaleCategories.append("2-Quite Low-F")

    elif (i >= 50 ) & (i < 75):
        FemaleCategories.append("3-Mid-F")

    elif (i >= 75 ) & (i < 100):
        FemaleCategories.append("4-Quite High-F")

    elif (i >= 100 ) & (i < 125):
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
print(female.head)
malefemale = pd.concat([male, female])
print(malefemale.shape)

# creating the dataset
data = {'1-Low-M': 714, '2-Quite Low-M': 471, '3-Mid-M': 817,
        '4-Quite High-M': 1109, '5-High-M' : 444}
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
data = {'1-Low-M': 675, '2-Quite Low-M': 434, '3-Mid-M': 804,
        '4-Quite High-M': 1111, '5-High-M' : 464}
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

#Comparison of Male v Female
# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize=(12, 8))

# set height of bar
Male = [714, 471, 817, 1109, 444]
Female = [675, 434, 804, 1111, 464]

# Set position of bar on X axis
br1 = np.arange(len(Male))
br2 = [x + barWidth for x in br1]

# Make the plot
plt.bar(br1, Male, color='r', width=barWidth,
        edgecolor='grey', label='Male')
plt.bar(br2, Female, color='g', width=barWidth,
        edgecolor='grey', label='Female')

# Adding Xticks
plt.xlabel('Categories', fontweight='bold', fontsize=15)
plt.ylabel('No. of Customers', fontweight='bold', fontsize=15)
plt.xticks([r + barWidth for r in range(len(Male))],
           ['Low', 'Quite Low', 'Mid', 'Quite High', 'High'])
plt.legend()
plt.show()

# Sort merged dataframe
malefemale = malefemale.sort_values(["gender", "MonthlyCharges_y"])
print(malefemale)
fig, ax = plt.subplots(1,1)

# Load Data
g = sns.countplot(x='MonthlyCharges_y', data=malefemale, hue='gender')
g.set_title("Male Female Comparison")
plt.show()

print(malefemale.columns)

# Check average monthly spend
print(malefemale["MonthlyCharges_x"].mean())
print(malefemale["MonthlyCharges_x"].sum())
print(malefemale["MonthlyCharges_x"].count())

#Remove customer IDs from the data set
churncomp = telcodata.iloc[:,1:]
#Convert the variables
churncomp['Churn'].replace(to_replace='Yes', value=1, inplace=True)
churncomp['Churn'].replace(to_replace='No',  value=0, inplace=True)

#Convert all the categorical variables into dummy variables
df_dummies = pd.get_dummies(churncomp)
print(df_dummies.head())
print(df_dummies.info())

#Get Correlation of "Churn" with other variables:
plt.figure(figsize=(15,8))
df_dummies.corr()['Churn'].sort_values(ascending = False).plot(kind='bar')

fig, ax = plt.subplots(1,1)

#Show total customers by contract type
ax = telcodata['Contract'].value_counts().plot(kind = 'bar',rot = 0, width = 0.3)
ax.set_ylabel('# of Customers')
ax.set_title('# of Customers by Contract Type')
plt.show()

print(telcodata[['MonthlyCharges', 'TotalCharges']].plot.scatter(x = 'MonthlyCharges',
                                                              y='TotalCharges'))
#Insights
#1 Monthly spend is not affected by gender
#2 "Quite High" range is the highest in both male and female. It accounts for 2212 customers out of 7043 = 31.4%
#3 Average monthly spend is $64.76.
#4 Month to month contracts, absence of online security and tech support seem to be positively correlated with churn. While, tenure, two year contracts seem to be negatively correlated with churn. Online security, streaming TV, online backup, tech support, etc. without internet connection seem to be negatively related to churn.
#5 Most customers are in the month to month contract. While there are almost equal number of customers in the 1 year and 2 year contracts.
#6 Total charges increase as the monthly bill for a customer increases#6 Total charges increase as the monthly bill for a customer increases.