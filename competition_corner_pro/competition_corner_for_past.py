import encodings
import requests
import csv
from bs4 import BeautifulSoup
from encodings.utf_8 import encode
import json
def write_output(data):
	with open('competition_corner_for_past.csv', mode='a', newline="", encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["title_name","venue","street_address","city","region","country","postalCode","competition_corner","price","priceCurrency","organizer","type_description","subtitle","startDate","startMonth","startYear","endDate","endMonth","endYear","page_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    for i in range(300,1000):
        print(i)
        url = "https://competitioncorner.net/Event/GetFilteredEventsHtml?timing=past&page="+str(i)+"&perPage=10"
        response = requests.request("GET", url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for links in soup.find_all("div",{"class":"event_info"}):
            link = "https://competitioncorner.net" + links.find("a")["href"] + "/details"
            if links.find("a")["href"] == None:
                break
            print(link)
            response1 = requests.request("GET", link)
            soup1 = BeautifulSoup(response1.text, 'html.parser')
            data = soup1.find("app-root")["eventdata"]
            json_data = json.loads(data.strip())
            try:
                venue = json_data['event']['location']['venue']
            except:
                venue = ''
            try:
                street_address = json_data['event']['location']['street']
                if "https://" in json_data['event']['location']['street']:
                    street_address = ''
            except:
                street_address = ''
            try:
                city = json_data['event']['location']['city']
            except:
                city = ''
            try:
                region = json_data['event']['location']['state']
            except:
                region = ''
            try:
                country = json_data['event']['location']['country']
            except:
                country = ''
            try:
                postalCode = json_data['event']['location']['zip']
            except:
                postalCode = ''
            try:
                competition_corner = json_data['event']['organizer']['title']
            except:
                competition_corner = ''
            try:
                price = json_data['event']['price']
            except:
                price = ''
            try:
                priceCurrency = json_data['offers']['currency']
            except:
                priceCurrency = ''
            organizer = json_data['event']['organizer']['title']
            try:
                type_description1 = json_data['event']['description']
            except:
                type_description1 = ''
            soup2 = BeautifulSoup(type_description1, 'html.parser')
            type_description3 = []
            for data in soup2.find_all("p"):
                type_description2 = data.text.replace("***","")
                type_description3.append(type_description2)
            type_description = " ".join(type_description3)
            try:
                subtitle = json_data['subtitle']
            except:
                subtitle = ''
            try:
                title_name = json_data['event']['name'].strip()
            except:
                title_name = ''
            try:
                startDate = json_data['event']['startDateTime'].split("T")[0].split("-")[2]
            except:
                startDate = ''
            try:
                startMonth = json_data['event']['startDateTime'].split("T")[0].split("-")[1]
            except:
                startMonth = ''
            try:
                startYear = json_data['event']['startDateTime'].split("T")[0].split("-")[0]
            except:
                startYear = ''
            try:
                endDate = json_data['event']['endDateTime'].split("T")[0].split("-")[2]
            except:
                endDate = ''
            try:
                endMonth = json_data['event']['endDateTime'].split("T")[0].split("-")[1]
            except:
                endMonth = ''
            try:
                endYear = json_data['event']['endDateTime'].split("T")[0].split("-")[0]
            except:
                endYear = ''
            print(title_name)
            page_url = link
            store =[title_name,venue,street_address,city,region,country,postalCode,competition_corner,price,priceCurrency,organizer,type_description,subtitle,startDate,startMonth,startYear,endDate,endMonth,endYear,page_url]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()
