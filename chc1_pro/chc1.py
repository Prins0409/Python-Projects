import csv
from html.parser import HTMLParser
from itertools import count
from tkinter import N
from bs4 import BeautifulSoup
from numpy import number
import requests
import json

def write_output(data):
	with open('chc1.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["link","name","addr","num","time"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "cookie": "DISPLAY_NEWSLETTER=1; _gcl_au=1.1.541168490.1654074756; _gid=GA1.2.869459300.1654074756; _ga_KH71LCVTGE=GS1.1.1654074756.1.1.1654074760.56; _ga=GA1.2.1364389241.1654074756",
        "referer": "https://www.chc1.com/locations/",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
    }
    url = "https://www.chc1.com/locations/"
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    for link1 in soup.find_all("div",{"class":"col-6 col-md-3 mb-5"}):
        link = link1.find("a")['href']
        headers2 = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "en-US,en;q=0.9",
            "cookie": "DISPLAY_NEWSLETTER=1; _gcl_au=1.1.541168490.1654074756; _gid=GA1.2.869459300.1654074756; _ga_KH71LCVTGE=GS1.1.1654074756.1.1.1654077307.59; _ga=GA1.2.1364389241.1654074756",
            "referer": "https://www.chc1.com/locations/",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
        }
        url2 = requests.get(link, headers=headers2)
        soup2 = BeautifulSoup(url2.text, 'html.parser')
        name = soup2.find("strong",{"class":"mt-3"}).text
        addr = soup2.find("div",{"class","col-12 col-sm-5"}).find("p").text
        num = soup2.find("div",{"class":"col-12 col-sm-5"}).find_all("p")[1].text        
        time = []
        table = soup2.find("table", {"class":"table table-striped"}).text.strip().replace('\n'," ").replace('\r'," ").encode('ascii', 'ignore').decode('ascii').strip()
        time.append(table)
        store =[link,name,addr,num,time]
        yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()