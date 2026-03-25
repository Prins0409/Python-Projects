import csv
from html.parser import HTMLParser
from itertools import count
from tkinter import N
from bs4 import BeautifulSoup
import requests
import json

def write_output(data):
	with open('Blumen_Deko.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","category","streetNumber_streetName","postalCode","city","country","phone","web_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    for i in range(1,92):
        headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "origin": "https://www.hochzeitsportal24.de",
        "referer": "https://www.hochzeitsportal24.de/",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
        }
        url = "https://api.hochzeitsportal24.de/vendors/search?categoryId=12&page="+str(i)+"&distance=10&limit=12"
        data = requests.get(url, headers=headers)
        json_data = json.loads(data.text)
        for item in json_data['items']:
            name = item['name']
            category = "Hochzeitstorte"
            # category--"Hochzeitstorte" --- Direct add in csv
            streetNumber_streetName = item['location']['streetNumber'] + item['location']['streetName']
            postalCode = item['location']['postalCode']
            city = item['location']['city']
            country = item['location']['country']
            phone = item['contactInfo']['phone']
            web_url = "https://www.hochzeitsportal24.de/branchenbuch/hochzeitstorte/"+ item['slug']
            store =[name,category,streetNumber_streetName,postalCode,city,country,phone,web_url]
            yield store

def scrape():
    data = fetch_data()
    write_output(data)
scrape()