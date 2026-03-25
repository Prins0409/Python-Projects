import csv
from html.parser import HTMLParser
from itertools import count
from tkinter import N
from bs4 import BeautifulSoup
from numpy import empty
import requests
import json
import urllib.request
import os
def write_output(data):
	with open('adfixtrade_all.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","sku","category","image_url","page_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    for i in range(0,47):
        url = "https://www.adfixtrade.co.uk/product-category/architectural-ironmongery/furniture-fittings-architectural-ironmongery//page/"+str(i)
        headers = {
            'accept-ranges': 'bytes',
            'content-type': 'text/html; charset=UTF-8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
        }
        response = requests.request("GET", url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        for link1 in soup.find_all("li",{"class":"card", "class":"h-100","class":"product"}):
            link = link1.find("a")['href']

            headers1 = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image_url/avif,image_url/webp,image_url/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "en-US,en;q=0.9",
            "cookie": "_ga=GA1.3.48556236.1655277132; _gid=GA1.3.554589987.1655277132; Branda_Cookie_Notice_1=1657872789.434; __stripe_mid=1240eca6-459b-4dc5-9e4f-b643b18fdc5bc0d199; __atuvc=7%7C24",
            "referer": "https://www.adfixtrade.co.uk/product-category/architectural-ironmongery/furniture-fittings-architectural-ironmongery/bed-brackets/",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
            }
            url2 = link
            response2 = requests.request("GET", url2, headers=headers1)
            soup2 = BeautifulSoup(response2.text, 'html.parser')
            name = soup2.find('h1',{"class":"product_title entry-title"}).text
            sku = soup2.find('span',{"class":"sku"}).text
            category = soup2.find('span',{"class":"posted_in"}).text.replace('Categories: ', "")
            page_url = soup2.find("link",{"rel":"canonical"})["href"]
            image_url = ''
            if soup2.find("div",{"class":"woocommerce-product-gallery__image"}) != None:
                image_url = soup2.find("div",{"class":"woocommerce-product-gallery__image"}).find("a")['href']
                try: 
                    folder = name.replace(':'," ").replace('″'," ").strip().replace("/",'').replace(">","").strip().replace("..","")
                    os.mkdir(folder)
                except:
                    pass
                if image_url != '':
                    response = requests.get(image_url,headers=headers1)
                    if response.status_code == 200:
                        print(response.status_code)
                        with open(folder+"//"+folder+'.jpg', 'wb') as file:
                            file.write(response.content)
            store =[name,sku,category,image_url,page_url]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()