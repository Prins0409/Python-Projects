import csv
import requests
import json
from bs4 import BeautifulSoup

def write_output(data):
	with open('american_standard_air.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","brand_ID","addressLine1","addressLine2","city","state","country","zipcode","phone1","phone2","phone3","email","finance_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    for data1 in open("yelp_target_zip_codes.csv",'r',encoding='utf-8'):
        print(data1.strip())
        url = "https://prd.irapis.com/dealers/locations?brand=AS&zipcode="+str(data1.strip())+"&url=https%3A%2F%2Fwww.americanstandardair.com%2Ffind-your-dealer%2F&anonymousId=null&sessionId=null"
        headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response = requests.request("GET", url, headers=headers)
        json_object = json.loads(response.text)
        for datas in json_object['dealers']:
            name =  datas['data']['name']
            brand_ID =  datas['data']['brandID']
            addressLine1 =  datas['data']['addressLine1']
            addressLine2 =  datas['data']['addressLine2']
            city =  datas['data']['city']
            state =  datas['data']['state']
            country =  datas['data']['country']
            zipcode =  datas['data']['zipcode']
            phone1 =  datas['data']['phone1']
            phone2 =  datas['data']['phone2']
            phone3 =  datas['data']['phone3']
            email =  datas['data']['email']
            finance_url =  datas['data']['financeURL']
            print(name)
            store =[name,brand_ID,addressLine1,addressLine2,city,state,country,zipcode,phone1,phone2,phone3,email,finance_url]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()