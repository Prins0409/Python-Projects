import csv
import requests
import json

def write_output(data):
	with open('burger.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["latitude","longitude","locator_domain","store_no","location_name","street_address","street_no","city","state","zipcode","phone_no","page_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():           
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "origin": "https://acburger.com",
        "referer": "https://acburger.com/",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    url = "https://media.acburger.com/api/locations/json"
    data = requests.get(url, headers=headers)
    json_data = json.loads(data.text)
    for item in json_data:
        latitude = item['lat']
        longitude = item['lng']
        locator_domain = "https://acburger.com/"
        store_no = item['store']
        location_name = item['name']
        street_address = item['address']
        street_no = item['address'].split(" ")[0]
        city = item['city']
        state = item['state']
        zipcode = item['zip']
        phone_no = item['phone']
        page_url = "https://acburger.com/menu/"
        store =[latitude,longitude,locator_domain,store_no,location_name,street_address,street_no,city,state,zipcode,phone_no,page_url]
        yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()