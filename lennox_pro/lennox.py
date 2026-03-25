import csv
import requests
import json
from bs4 import BeautifulSoup

def write_output(data):
	with open('lennox.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","city","state","zipcode","address","phone_no","website","page_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    url = "https://www.lennox.com/locate/dealer-list"
    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for item in soup.find_all("li",{"class":"lnx-accordion-item"}):
        all_urls = "https://www.lennox.com" + item.find("a")["href"]
        print(all_urls)
        headers1 = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "cookie": "opvc=def9f148-1399-4636-a232-f2fd192a5791; sitevisitscookie=1; dmid=0c06b795-5705-42f1-acc4-7c4379ee78e2; BVBRANDID=c4b45e15-cc5f-445e-aabe-ae216fefac59; _gcl_au=1.1.223838570.1670590916; _gid=GA1.2.1298868780.1670590918; sa-user-id=s%253A0-0adff713-6ad0-4af7-7d92-0fc81e31bfd2.bzJ%252FaevXRAESXVtgcpR8GvLP1mlXpQvqlFlL2NEYb7Y; sa-user-id-v2=s%253ACt_3E2rQSvd9kg_IHjG_0sGUEjs.JbWvjUK7zKqj0IM2n4%252B7I7rOH7A9hdIRJ804SHx4aFo; _fbp=fb.1.1670590920785.1866628650; cebs=1; OptanonAlertBoxClosed=2022-12-09T13:02:03.122Z; _hjSessionUser_1572359=eyJpZCI6IjY1YmNmZWRhLWYwOTItNTNmOC04NGJiLTkyMWZiMTE1ZjgyOCIsImNyZWF0ZWQiOjE2NzA1OTA5MjE1OTMsImV4aXN0aW5nIjp0cnVlfQ==; JSESSIONID=953BD109627665219B2B87EABE65D6CD; BVBRANDSID=e6b69017-9239-46be-8f8d-31f50a27171b; _hjIncludedInSessionSample=1; _hjSession_1572359=eyJpZCI6IjIzNmQyM2I2LTgyY2EtNDE4ZC1hYjhlLTc3MWZlYmE3M2UwNyIsImNyZWF0ZWQiOjE2NzA2NDc4MDcxNjcsImluU2FtcGxlIjp0cnVlfQ==; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; _ce.s=v~fa1c8dc4d072b5aa4bbdd54324fb26c882dfcdee~vpv~0~v11.rlc~1670647808658; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Dec+10+2022+10%3A32%3A13+GMT%2B0530+(India+Standard+Time)&version=6.27.0&isIABGlobal=false&hosts=&consentId=6589e9b7-12dd-4337-ba20-4d41a4182369&interactionCount=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0001%3A1%2CC0002%3A1%2CC0004%3A1%2CC0005%3A1&geolocation=US%3BNY&AwaitingReconsent=false; AWSALB=lFxaVXh3wVCVUvEN2PXE9MZ91OQaMT2Pgry9SfFj4SIWybkKrn5yK2WhoxKSpMgM1dSRxGS6suIS2IJ+SYxQsTK7sivtgvYs7cbjzYDZAM6lAABV2XTrJKZ6Z7Yi; AWSALBCORS=lFxaVXh3wVCVUvEN2PXE9MZ91OQaMT2Pgry9SfFj4SIWybkKrn5yK2WhoxKSpMgM1dSRxGS6suIS2IJ+SYxQsTK7sivtgvYs7cbjzYDZAM6lAABV2XTrJKZ6Z7Yi; cebsp=16; _ga=GA1.2.1165885123.1670590918; _ga_LHJ3WR8SZT=GS1.1.1670647806.3.1.1670648535.0.0.0",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response1 = requests.request("GET", all_urls, headers=headers1)
        soup1 = BeautifulSoup(response1.text, 'html.parser')
        name = soup1.find("span",{"class":"lnx-dealer-name"}).text.strip()
        print(name)
        phone_no = soup1.find("div",{"class":"lnx-address"}).find("a",{"class":"lnx-dealer-contact"}).text.strip()
        try:
            address = soup1.find("div",{"class":"lnx-address"}).text.strip().replace(phone_no,"").strip()
        except:
            address = ''
        try:
            city = soup1.find("div",{"class":"lnx-address"}).find_all("span")[2].text.strip()
        except:
            city = ''
        try:
            state = soup1.find("div",{"class":"lnx-address"}).text.strip().replace(phone_no,"").split(", ")[1].split(" ")[0].strip()
        except:
            state = ''
        try:
            zipcode = soup1.find("div",{"class":"lnx-address"}).text.strip().replace(phone_no,"").split(", ")[1].split(" ")[1].strip()
        except:
            zipcode = ''
        try:
            website = soup1.find("a",{"class":"lnx-website"}).text.strip()
        except:
            website = ''
        page_url = all_urls
        store =[name,city,state,zipcode,address,phone_no,website,page_url]
        yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()