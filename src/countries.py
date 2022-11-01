import requests
import json


url = (
    "https://api.storelocator.hmgroup.tech/v2/brand/hm/locations/locale/es_es/countries"
)

payload = {}
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Origin": "https://www2.hm.com",
    "Referer": "https://www2.hm.com/",
    "Cookie": "ARRAffinity=ab378bc277b4a32d20c57fceb79fd08f1fb44a1e1e227b7dd5fc3185d30f26f4; ARRAffinitySameSite=ab378bc277b4a32d20c57fceb79fd08f1fb44a1e1e227b7dd5fc3185d30f26f4",
}

response = requests.request("GET", url, headers=headers, data=payload, timeout=10)

# print(response.text)

country_data = json.loads(response.text)

country_codes = [i["countryId"] for i in country_data["storeCountries"]]

print(country_codes)
