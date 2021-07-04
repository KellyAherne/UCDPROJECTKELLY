import pandas as pd

data = pd.read_csv("Telco_customer_churn_project.csv")

new_Data=data.fillna(data.mean)

