import csv
import requests
import json
from bs4 import BeautifulSoup

def write_output(data):
	with open('carrier.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","city","state","country","zipcode","full_address","email","fax","phone_no_1","phone_no_2","business_hour","website","page_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    for data1 in open("yelp_target_zip_codes.csv",'r',encoding='utf-8'):
        print(data1.strip())
        url = "https://www.carrier.com/residential/en/ca/ResidentialDealerLocator/FindDealers/"
        payload = '{"zipCode":"'+str(data1.strip())+'","radius":"0.01"}'
        headers = {
        "accept": "application/json, text/plain, */*",
        "content-length": "47",
        "content-type": "application/json",
        "cookie": "residential_State=Zuid-Holland; residential_City=Naaldwijk; residential_Language=en; residential_Location=ca; residential_Parent=; residential_en_ca_IsVisited=True; TAFSessionId=tridion_82b80e12-7c73-4997-a007-8fc81e014f35; ASP.NET_SessionId=dphotbwcoh1kzexltjf4fweo; _vwo_uuid_v2=D21BD7481A53CDDAB4F12A90E02ED41F9|8881d7a9bccce0800e4610e62ed0c5d2; _gcl_au=1.1.682120908.1670650362; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D21BD7481A53CDDAB4F12A90E02ED41F9; _vis_opt_exp_151_combi=2; notice_preferences=0:; notice_gdpr_prefs=0:; cmapi_gtm_bl=ga-ms-ua-ta-asp-bzi-sp-awct-cts-csm-img-flc-fls-mpm-mpr-m6d-tc-tdc; cmapi_cookie_privacy=permit 1 required; notice_behavior=implied,us; _gid=GA1.2.179063490.1670821637; residential_Zipcode=35201; residential_SearchType=Territory; _vwo_sn=257342%3A1; _ga=GA1.2.1306095024.1670650362; _gat_UA-26423662-5=1; _vwo_ds=3%3Aa_0%2Ct_0%3A0%241670650360%3A73.38936391%3A%3A6_0%2C5_0%2C2_0%2C1_0%3A3_0%3A3; _ga_1BFPS3YXP0=GS1.1.1670907704.6.1.1670907729.0.0.0",
        "origin": "https://www.carrier.com",
        "referer": "https://www.carrier.com/residential/en/ca/find-a-dealer/",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        json_data = json.loads(response.text)
        for item in json_data['Dealers']:
            dealerId = item['DealerID']
            all_page_urls = "https://www.carrier.com/residential/en/ca/find-a-dealer/detail/?dealerId="+str(dealerId)
            print(all_page_urls)
            name = item['DealerName']
            city = item['DealerCity']
            state = item['DealerState']
            country = item['DealerCountry']
            zipcode = item['DealerZip']
            full_address = str(item['DealerCompleteAddress']).replace("<br/>",", ")
            email = item['DealerEmail']
            fax = item['DealerFaxNumber']
            phone_no_1 = item['DealerPhone']
            phone_no_2 = item['DealerPhone2']
            business_hour = item['DealerBusinessHours']
            website = item['DealerWebsite']
            print(city)
            page_url = all_page_urls
            store =[name,city,state,country,zipcode,full_address,email,fax,phone_no_1,phone_no_2,business_hour,website,page_url]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()