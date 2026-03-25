import csv
from html.parser import HTMLParser
from itertools import count
from tkinter import N
from bs4 import BeautifulSoup
import requests
import json

def write_output(data):
	with open('car_max1.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)	
		writer.writerow(["name","miles","price","store_id","store_geocity","stateName","stockNumber","year","company_name","model","trim","page_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }
    # url = "https://www.carmax.com/stores/api/recommendations/4wd_awd/8/6049/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    # url = "https://www.carmax.com/stores/api/recommendations/4wd_awd/8/6059/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    # url = "https://www.carmax.com/stores/api/recommendations/4wd_awd/8/6102/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    # url = "https://www.carmax.com/stores/api/recommendations/4wd_awd/8/6043/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    # url = "https://www.carmax.com/stores/api/recommendations/thirdrowseat/8/6098/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    # url = "https://www.carmax.com/stores/api/recommendations/comfort/8/6011/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    # url = "https://www.carmax.com/stores/api/recommendations/4wd_awd/8/7234/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    # url = "https://www.carmax.com/stores/api/recommendations/4wd_awd/8/6087/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    # url = "https://www.carmax.com/stores/api/recommendations/4wd_awd/8/6075/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    # url = "https://www.carmax.com/stores/api/recommendations/4wd_awd/8/7271/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    # url = "https://www.carmax.com/stores/api/recommendations/thirdrowseat/8/7233/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    # url = "https://www.carmax.com/stores/api/recommendations/4wd_awd/8/7100/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    # url = "https://www.carmax.com/stores/api/recommendations/thirdrowseat/8/6013/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    # url = "https://www.carmax.com/stores/api/recommendations/4wd_awd/8/7662/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    # url = "https://www.carmax.com/stores/api/recommendations/4wd_awd/8/7274/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    # url = "https://www.carmax.com/stores/api/recommendations/4wd_awd/8/6161/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    # url = "https://www.carmax.com/stores/api/recommendations/thirdrowseat/8/7249/6ef33d96-d116-4bcf-95af-1636d1e42f9f"
    url = "https://www.carmax.com/stores/api/recommendations/4wd_awd/8/6170/6ef33d96-d116-4bcf-95af-1636d1e42f9f"

    data = requests.get(url, headers=headers)
    json_data = json.loads(data.text)
    for item in json_data['recommendations']:
        for all_data in item['vehicles']:
            name = all_data['description']
            miles = all_data['miles']
            price = all_data['price']
            store_detail = all_data['store']
            store_id = store_detail['id']
            store_geocity = store_detail['geoCity']
            stateName = store_detail['stateName']
            stockNumber = all_data['stockNumber']
            year = all_data['year']
            company_name = all_data['make']
            model = all_data['model']
            trim = all_data['trim']
            page_url = "https://www.carmax.com/car/" + str(all_data['stockNumber'])
            store =[name,miles,price,store_id,store_geocity,stateName,stockNumber,year,company_name,model,trim,page_url]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()