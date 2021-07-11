import pandas as pd
import numpy as np

#import dataset
telcodata = pd.read_csv("Telco_customer_churn_project.csv")

telcodata["TotalCharges"] = pd.to_numeric(telcodata.TotalCharges, errors="coerce")
print(telcodata.TotalCharges.isnull().sum())

print(telcodata[np.isnan(telcodata["TotalCharges"])])

print(telcodata[telcodata['tenure'] == 0][['tenure','TotalCharges']])

print(telcodata.fillna(0, inplace=True))
print(telcodata.shape)

for No in PhoneService:
    print()