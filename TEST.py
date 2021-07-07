import pandas as pd
import numpy as np

#import dataset
telcodata = pd.read_csv("Telco_customer_churn_project.csv")
femalecustomers = telcodata[telcodata["gender"]== "Female"]
femalecustomers1 = femalecustomers[["customerID", "gender", "tenure", "DeviceProtection", "Contract", "PaperlessBilling", "MonthlyCharges", "TotalCharges"]]

print(femalecustomers1)

