import encodings
import requests
import csv
from bs4 import BeautifulSoup
from encodings.utf_8 import encode
import json
def write_output(data):
	with open('competition_corner.csv', mode='a', newline="", encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["title_name","address1","address2","city","region","country","postalCode","competition_corner","price","priceCurrency","organizer","type_description","contact_details","startDate","startMonth","startYear","endDate","endMonth","endYear","page_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    for i in range(1,7): 
        url = "https://competitioncorner.net/Event/GetFilteredEventsHtml?timing=upcoming&page="+str(i)+"&perPage=100"
        response = requests.request("GET", url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for links in soup.find_all("div",{"class":"event_info"}):
            link = "https://competitioncorner.net" + links.find("a")["href"] + "/details"
            response1 = requests.request("GET", link)
            soup1 = BeautifulSoup(response1.text, 'html.parser')
            for data in soup1.find("script",{"type":"application/ld+json"}):
                json_data = json.loads(data.strip())
                try:
                    address1 = json_data['location']['name']
                except:
                    address1 = ''
                try:
                    address2 = json_data['location']['address']['streetAddress'].split("#")[0]
                except:
                    address2 = ''
                try:
                    city = json_data['location']['address']['addressLocality']
                except:
                    city = ''
                try:
                    region = json_data['location']['address']['addressRegion']
                except:
                    region = ''
                try:
                    country = json_data['location']['address']['addressCountry']
                except:
                    country = ''
                try:
                    postalCode = json_data['location']['address']['postalCode']
                except:
                    postalCode = ''
                try:
                    competition_corner = json_data['organizer']['name']
                except:
                    competition_corner = ''
                try:
                    price = json_data['offers']['price']
                except:
                    price = ''
                try:
                    priceCurrency = json_data['offers']['priceCurrency']
                except:
                    priceCurrency = ''
                data1 = soup1.find("div",{"class":"page-wrap"}).find("app-root")["eventdata"]
                json_data1 = json.loads(data1)
                organizer = json_data1['event']['organizer']['title']
                try:
                    type_description = json_data1['subtitle']
                except:
                    type_description = ''
                try:
                    contact = json_data1['event']['location']['zip']
                except:
                    contact = ''
                try:
                    title_name = json_data1['event']['name']
                except:
                    title_name = ''
                contact_details = ''
                if "@" in contact:
                    contact_details = contact
                try:
                    startDate = json_data1['event']['startDateTime'].split("T")[0].split("-")[2]
                except:
                    startDate = ''
                try:
                    startMonth = json_data1['event']['startDateTime'].split("T")[0].split("-")[1]
                except:
                    startMonth = ''
                try:
                    startYear = json_data1['event']['startDateTime'].split("T")[0].split("-")[0]
                except:
                    startYear = ''
                try:
                    endDate = json_data1['event']['endDateTime'].split("T")[0].split("-")[2]
                except:
                    endDate = ''
                try:
                    endMonth = json_data1['event']['endDateTime'].split("T")[0].split("-")[1]
                except:
                    endMonth = ''
                try:
                    endYear = json_data1['event']['endDateTime'].split("T")[0].split("-")[0]
                except:
                    endYear = ''
                print(title_name)
                page_url = link
                store =[title_name,address1,address2,city,region,country,postalCode,competition_corner,price,priceCurrency,organizer,type_description,contact_details,startDate,startMonth,startYear,endDate,endMonth,endYear,page_url]
                yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()