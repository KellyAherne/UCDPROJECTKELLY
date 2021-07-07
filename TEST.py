import requests

apidata=requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=TEO&apikey=TGFBMIZEC0YHTT5W")

parsed_apidata=apidata.json()

print(type(parsed_apidata))
print(parsed_apidata)

