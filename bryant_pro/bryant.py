import csv
import requests
import json
from bs4 import BeautifulSoup

def write_output(data):
	with open('bryant.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","city","state","zipcode","full_address","business_hour","phone_no","page_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    for data1 in open("yelp_target_zip_codes.csv",'r',encoding='utf-8'):
        print(data1.strip())
        url = "https://www.bryant.com/en/us/BryantDealerLocator/FindDealers/"
        payload = '{"zipCode":"'+str(data1.strip())+'","radius":"0.01"}'
        headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,gu;q=0.4,de;q=0.3',
        'content-length': '34',
        'content-type': 'application/json',
        'cookie': 'bryant_State=Maharashtra; bryant_City=Mumbai; bryant_Language=en; bryant_Location=us; bryant_Parent=; bryant_en_us_IsVisited=True; TAFSessionId=tridion_dc5df5a8-d528-4b17-89f2-be6fd6c6316c; ASP.NET_SessionId=3gxtci52gko4kx52tie1kqsq; _vwo_uuid_v2=D4FBC4BCAEB422DC8942995AF0369FE32|6e0a8bd0111b55c9e815d6fa9704e327; notice_behavior=implied,us; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D4FBC4BCAEB422DC8942995AF0369FE32; _gcl_au=1.1.1008872265.1670580856; _gid=GA1.2.1743457780.1670580857; _vis_opt_exp_9_combi=2; _vis_opt_exp_12_combi=2; _vis_opt_exp_30_combi=2; _vis_opt_exp_40_combi=2; bryant_Zipcode=10001; _vwo_ds=3%3Aa_1%2Ct_0%3A0%241670580853%3A27.96075094%3A%3A%3A3_1%3A1; _ga_5L7FHWT3B0=GS1.1.1670580857.1.1.1670581220.0.0.0; _ga=GA1.1.1784514510.1670580857; _vwo_sn=0%3A8%3Ar2.visualwebsiteoptimizer.com%3A8%3A1; notice_preferences=2:; notice_gdpr_prefs=0,1,2:; cmapi_gtm_bl=; cmapi_cookie_privacy=permit 1,2,3; __atuvc=1%7C49; __atuvs=63930bec71a667cd000; mdLogger=false; kampyle_userid=c3de-fbf0-ab99-89b5-f793-91d1-019d-e10d; kampyleUserSession=1670581228383; kampyleUserSessionsCount=1; kampyleSessionPageCounter=1; _hp2_id.220611411=%7B%22userId%22%3A%224444670226529580%22%2C%22pageviewId%22%3A%227021706975485554%22%2C%22sessionId%22%3A%225810138517943284%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; cebs=1; _hp2_ses_props.220611411=%7B%22r%22%3A%22https%3A%2F%2Fwww.bryant.com%2Fen%2Fus%2Fhvac-contractors%2F%22%2C%22ts%22%3A1670581228559%2C%22d%22%3A%22www.bryant.com%22%2C%22h%22%3A%22%2Fen%2Fus%2Fhvac-contractors%2F%22%7D; cebsp=1; _ce.s=v~894b9745d366bb36bbbce4dc2039530a9a6313c6~vpv~0~v11.rlc~1670581229376; bryant_Language=en; bryant_Location=us; bryant_Parent=; bryant_Zipcode='+str(data1.strip()),
        'origin': 'https://www.bryant.com',
        'referer': 'https://www.bryant.com/en/us/hvac-contractors/',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        # open("test.txt",'w',encoding='utf-8').write(str(response.text))
        json_data = json.loads(response.text)
        zipcode = json_data['Zipcode']
        for item in json_data['Dealers']:
            dealerId = item['DealerID']
            print(dealerId)
            all_page_urls = "https://www.bryant.com/en/us/hvac-contractors/detail/?zipcode="+str(zipcode)+"&country=USA&dealerId="+str(dealerId)
            headers1 = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,gu;q=0.4,de;q=0.3',
            'cache-control': 'max-age=0',
            'cookie': 'bryant_State=Maharashtra; bryant_City=Mumbai; bryant_Language=en; bryant_Location=us; bryant_Parent=; bryant_en_us_IsVisited=True; TAFSessionId=tridion_dc5df5a8-d528-4b17-89f2-be6fd6c6316c; ASP.NET_SessionId=3gxtci52gko4kx52tie1kqsq; _vwo_uuid_v2=D4FBC4BCAEB422DC8942995AF0369FE32|6e0a8bd0111b55c9e815d6fa9704e327; notice_behavior=implied,us; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D4FBC4BCAEB422DC8942995AF0369FE32; _gcl_au=1.1.1008872265.1670580856; _gid=GA1.2.1743457780.1670580857; _vis_opt_exp_9_combi=2; _vis_opt_exp_12_combi=2; _vis_opt_exp_30_combi=2; _vis_opt_exp_40_combi=2; bryant_Zipcode=10001; _vwo_ds=3%3Aa_1%2Ct_0%3A0%241670580853%3A27.96075094%3A%3A%3A3_1%3A1; notice_preferences=2:; notice_gdpr_prefs=0,1,2:; cmapi_gtm_bl=; cmapi_cookie_privacy=permit 1,2,3; mdLogger=false; kampyle_userid=c3de-fbf0-ab99-89b5-f793-91d1-019d-e10d; cebs=1; _hp2_ses_props.220611411=%7B%22r%22%3A%22https%3A%2F%2Fwww.bryant.com%2Fen%2Fus%2Fhvac-contractors%2F%22%2C%22ts%22%3A1670581228559%2C%22d%22%3A%22www.bryant.com%22%2C%22h%22%3A%22%2Fen%2Fus%2Fhvac-contractors%2F%22%7D; _ce.s=v~894b9745d366bb36bbbce4dc2039530a9a6313c6~vpv~0~v11.rlc~1670581229376; _gat_UA-1758044-1=1; _ga=GA1.1.1784514510.1670580857; _vwo_sn=0%3A10%3Ar2.visualwebsiteoptimizer.com%3A10%3A1; _hp2_id.220611411=%7B%22userId%22%3A%224444670226529580%22%2C%22pageviewId%22%3A%227833236353373212%22%2C%22sessionId%22%3A%225810138517943284%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga_5L7FHWT3B0=GS1.1.1670580857.1.1.1670582779.0.0.0; cebsp=3; __atuvc=3%7C49; __atuvs=63930bec71a667cd002; kampyleUserSession=1670582785053; kampyleUserSessionsCount=2; kampyleSessionPageCounter=1; bryant_Language=en; bryant_Location=us; bryant_Parent=; bryant_Zipcode=10001',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
            }
            response1 = requests.request("GET", all_page_urls, headers=headers1)
            soup = BeautifulSoup(response1.text, 'html.parser')
            name = soup.find("section",{"class":"container dealerdetail"}).find("h1").text.strip()
            print(all_page_urls)
            print(name)
            try:
                city = soup.find("div",{"class":"col-md-7"}).find("address").find("br").text.strip().split(",")[0]
            except:
                city = ''
            try:
                state = soup.find("div",{"class":"col-md-7"}).find("address").find("br").text.strip().split(",")[1].strip().split(" ")[0]
            except:
                state = ''
            try:
                zipcode = soup.find("div",{"class":"col-md-7"}).find("address").find("br").text.strip().split(",")[1].strip().split(" ")[1]
            except:
                zipcode = ''
            try:
                full_address = soup.find("div",{"class":"col-md-7"}).find("address").text.strip().replace(soup.find("div",{"class":"col-md-7"}).find("address").find("br").text.strip(),"") +", "+ city +", "+ state +" "+ zipcode
            except:
                full_address = ''
            try:
                if soup.find("div",{"class":"col-md-7"}).find_all("p")[1].text.strip() == "Prendre rendez-vous maintenant":
                    business_hour = soup.find("div",{"class":"col-md-7"}).find_all("p")[3].text.strip()
                elif soup.find("div",{"class":"col-md-7"}).find_all("p")[1].text.strip() == "Years in Business:":
                    business_hour = ''
                else:
                    business_hour = soup.find("div",{"class":"col-md-7"}).find_all("p")[2].text.strip()
            except:
                business_hour = ''
            phone_no = soup.find("div",{"class":"col-md-7"}).find("a").text.strip().replace("Call us ","")
            page_url = all_page_urls
            store =[name,city,state,zipcode,full_address,business_hour,phone_no,page_url]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()