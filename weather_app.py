import requests
import json
import pandas as pd

City_Name = input("Enter the city name : ")

url = f"https://api.weatherapi.com/v1/current.json?key=d466e109017347a198341609230310&q={City_Name}"

Weather_data = requests.get(url)

print(f"{Weather_data.text}\n")

Weather_dic = json.loads(Weather_data.text)
print(f"{Weather_dic}\n")

df=pd.DataFrame(Weather_dic)
print(df)
print(df["current"]["temp_c"])

temp=Weather_dic["current"]["temp_c"]
print(f"Tempreature of city is {temp}")
