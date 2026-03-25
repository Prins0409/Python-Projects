import requests
import csv
from bs4 import BeautifulSoup
import json

def write_output(data):
	with open('throw_down_hub_past_with_register_link.csv', mode='a', newline="", encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["title_name","address","address1","for_description","country","competition_corner","startDate","startMonth","startYear","endDate","endMonth","endYear","organizer_name","organizer_url","register_url","page_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    for i in range(1,898):
        print(i)
        url = "https://throwdownhub.io/calendar/competition/info/"+str(i)
        headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "cookie": "_ga=GA1.1.567032749.1671102249; __stripe_sid=124dbe51-92ed-45c1-84ca-d036daa4466d28f5ce; __stripe_mid=c9371cdf-e788-440c-b91d-a2e5fcf9332a85ed2c; ci_session=rotqb22o6p3detr6uqqjjqfklf79mjf8; _ga_H9V2QZBEML=GS1.1.1671102248.1.1.1671104179.0.0.0",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response = requests.request("GET", url, headers=headers)
        if response.url == "https://throwdownhub.io/calendar/competition/list":
            continue
        soup = BeautifulSoup(response.text, 'html.parser')
        data1 = str(soup.find("script",{"type":"application/ld+json"})).replace('<script type="application/ld+json">',"").replace(" </script>","").split('"description":')[0]
        data2 = str(soup.find("script",{"type":"application/ld+json"})).replace('<script type="application/ld+json">',"").replace(" </script>","").split('"of')[1].replace('fers"','"offers"')
        for_description = str(soup.find("script",{"type":"application/ld+json"})).replace('<script type="application/ld+json">',"").replace(" </script>","").split('"description":')[1].split('"off')[0].replace("&nbsp;","").replace('",',"").replace('"',"").strip()
        data = str(data1) + str(data2)
        json_data = json.loads(data)

        title_name = json_data["name"]
        try:
            address = json_data['location']['address']['streetAddress']
        except:
            address = ''
        try:
            address1 = json_data['location']['name']
        except:
            address1 = ''
        try:
            country = json_data['location']['address']['addressCountry']
        except:
            country = ''
        competition_corner = soup.find("div",{"class":"col-12 mb-2 h4 text-break te"}).find("span",{"class":"text-mute"}).text
        try:
            startDate = json_data['startDate'].split("T")[0].split("-")[2].split(" ")[0]
        except:
            startDate = ''
        try:
            startMonth = json_data['startDate'].split("T")[0].split("-")[1]
        except:
            startMonth = ''
        try:
            startYear = json_data['startDate'].split("T")[0].split("-")[0]
        except:
            startYear = ''
        try:
            endDate = json_data['endDate'].split("T")[0].split("-")[2].split(" ")[0]
        except:
            endDate = ''
        try:
            endMonth = json_data['endDate'].split("T")[0].split("-")[1]
        except:
            endMonth = ''
        try:
            endYear = json_data['endDate'].split("T")[0].split("-")[0]
        except:
            endYear = ''
        organizer_name = json_data['organizer']['name']
        organizer_url = json_data['organizer']['url']
        register_url = json_data['offers']['url']
        page_url = url

        print(page_url)
        store =[title_name,address,address1,for_description,country,competition_corner,startDate,startMonth,startYear,endDate,endMonth,endYear,organizer_name,organizer_url,register_url,page_url]
        yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()