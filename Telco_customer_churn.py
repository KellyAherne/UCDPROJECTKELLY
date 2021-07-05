import pandas as pd

telcodata = pd.read_csv("Telco_customer_churn_project.csv")

print(telcodata)

print(telcodata.head())
print(telcodata.info())
print(telcodata.shape)
print(telcodata.describe())
print(telcodata.values)
print(telcodata.columns)
print(telcodata.index)
print(telcodata.sort_values(["TotalCharges", "gender"], ascending=[False, True]))