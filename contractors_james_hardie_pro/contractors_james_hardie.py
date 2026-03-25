import csv
import requests
import json
from bs4 import BeautifulSoup

def write_output(data):
	with open('contractors_james_hardie.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","city","state","zipcode","phone","full_address","website","page_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    for data1 in open("yelp_target_zip_codes.csv",'r',encoding='utf-8'):
        print(data1.strip())
        url = "https://contractors.jameshardie.com/10001"
        headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "cache-control": "max-age=0",
        "cookie": "CMSPreferredCulture=en-US; ASP.NET_SessionId=fer4entiu35qntap1yitpvxo; __utmc=117766683; __utmz=117766683.1670590721.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); OptanonAlertBoxClosed=2022-12-09T12:58:45.571Z; __utma=117766683.1133543419.1670590721.1670907713.1670910873.7; __utmt=1; __utmb=117766683.5.10.1670910873; OptanonConsent=isIABGlobal=false&datestamp=Tue+Dec+13+2022+11%3A41%3A52+GMT%2B0530+(India+Standard+Time)&version=5.15.0&landingPath=NotLandingPage&groups=C0003%3A1%2CC0001%3A1%2CC0004%3A1%2CBG1%3A1&hosts=H47%3A1&legInt=&consentId=f30cc824-4120-48e5-b754-df52760929d6&interactionCount=1&geolocation=%3B&AwaitingReconsent=false",
        "referer": "https://contractors.jameshardie.com/",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response = requests.request("GET", url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        for urls in soup.find_all("div",{"class":"group profile-name-right"}):
            page_url = "https://contractors.jameshardie.com" + urls.find("div",{"class":"fr heading"}).find("a")["href"]
            headers1 = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "cookie": "CMSPreferredCulture=en-US; ASP.NET_SessionId=fer4entiu35qntap1yitpvxo; __utmc=117766683; __utmz=117766683.1670590721.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); OptanonAlertBoxClosed=2022-12-09T12:58:45.571Z; __utma=117766683.1133543419.1670590721.1670907713.1670910873.7; __utmt=1; __utmb=117766683.7.10.1670910873; OptanonConsent=isIABGlobal=false&datestamp=Tue+Dec+13+2022+12%3A02%3A45+GMT%2B0530+(India+Standard+Time)&version=5.15.0&landingPath=NotLandingPage&groups=C0003%3A1%2CC0001%3A1%2CC0004%3A1%2CBG1%3A1&hosts=H47%3A1&legInt=&consentId=f30cc824-4120-48e5-b754-df52760929d6&interactionCount=1&geolocation=%3B&AwaitingReconsent=false",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
            }
            response1 = requests.request("GET", page_url, headers=headers1)
            soup1 = BeautifulSoup(response1.text, 'html.parser')
            name = soup1.find("h4",{"class":"company-name"}).text.strip()
            phone = soup1.find("div",{"class":"company-info"}).text.strip().split("p:")[1].split("Email")[0].strip()
            try:
                datas = soup1.find("div",{"class":"company-info"}).find_all("a")[1].text
            except:
                datas = ''
            if datas == "Contractor Website":
                website = soup1.find("div",{"class":"company-info"}).find_all("a")[1]['href']
            elif soup1.find("div",{"class":"company-info"}).find("a").text == "Contractor Website":
                website = soup1.find("div",{"class":"company-info"}).find("a")['href']
            else:
                website = ''
            full_address = str(soup1.find("div",{"class":"company-info"}).text.strip().split("p:")[0].strip()).strip().replace("  ","")
            dataaa = str(soup1.find("div",{"class":"company-info"})).split('<div class="company-info">')[1].split("<br/>")[0].strip()
            city = full_address.split(", ")[0].replace(dataaa,"").strip()
            state = full_address.split(", ")[1].split(" ")[0]
            zipcode = full_address.split(", ")[1].split(" ")[1]
            print(name)
            store =[name,city,state,zipcode,phone,full_address,website,page_url]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()