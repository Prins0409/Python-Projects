import csv
import requests
import json
from bs4 import BeautifulSoup

def write_output(data):
	with open('latitude.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["latitude"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    for data1 in open("yelp_target_zip_codes.csv",'r',encoding='utf-8'):
        print(data1.strip())
        url = "https://www.rheem.com/media/getData.php?service=getDealersJSONString&PostalCode="+str(data1.strip())+"&Distance=1&brand=bRheem&HeatingAndCooling=1&ResidentialWaterHeaters=1&CommercialHVAC=1&CommercialWaterHeaters=1&TanklessWaterHeaters=1&SolarWaterHeaters=1&HybridWaterHeaters=1&PoolAndSpaWaterHeaters=1&Distributor="
        headers = {
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Cookie": "tuuid=316e29f8-0929-4353-b3d1-2b0605e1dc51; c=1652811531; tuuid_lu=1670304721",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response = requests.request("GET", url, headers=headers)
        json_data = json.loads(response.text)
        for data in json_data:
            latitude = data['Latitude']
            print(latitude)
            store =[latitude]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()