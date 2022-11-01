import requests
import pandas as pd

url = "https://api.storelocator.hmgroup.tech/v2/brand/hm/stores/locale/es_es/country/ES?_type=json&campaigns=true&departments=true&openinghours=true&maxnumberofstores=100"

payload = {}
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Origin": "https://www2.hm.com",
    "Referer": "https://www2.hm.com/",
    "Cookie": "ARRAffinity=ab378bc277b4a32d20c57fceb79fd08f1fb44a1e1e227b7dd5fc3185d30f26f4; ARRAffinitySameSite=ab378bc277b4a32d20c57fceb79fd08f1fb44a1e1e227b7dd5fc3185d30f26f4",
}

# response = requests.request("GET", url, headers=headers, data=payload)

response = requests.post(url, headers=headers, data=payload, timeout=10)

# print(response.text)
# print(response.json())
store_df = pd.json_normalize(response.json(), record_path=["stores"])

opening_hours = pd.json_normalize(
    response.json()["stores"],
    record_path=["openingHours"],
)

pd.json_normalize(store_df.openingHours, record_path=["openingHours"])
print(store_df.columns)
store_df.to_csv("../dataset/output.csv")
print(opening_hours.T)
