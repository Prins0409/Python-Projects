import csv
import requests
import json
import urllib.request
import os

def write_output(data):
	with open('ironmongery_all_page.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["id","name","category","category1","category2","img_url","description","page_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    for i in range(1,14):
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "ocp-apim-subscription-key": "cd1817ac421a4eae8bd985e95b139fb1",
            "origin": "https://www.ironmongerydirect.co.uk",
            "referer": "https://www.ironmongerydirect.co.uk/",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "universe": "ironmongery",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
        }
        url = "https://api.manutantraders.com/product/brands/yale?page="+str(i)
        data = requests.get(url, headers=headers)
        json_data = json.loads(data.text)
        data1 = json_data['view']
        for item in data1['products']:
            id = item['id']
            headers1 = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "ocp-apim-subscription-key": "cd1817ac421a4eae8bd985e95b139fb1",
            "origin": "https://www.ironmongerydirect.co.uk",
            "referer": "https://www.ironmongerydirect.co.uk/",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "universe": "ironmongery",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
        }
            data1 = requests.get('https://api.manutantraders.com/product/ProductDetail/'+str(id),headers=headers1)
            json_data1 = json.loads(data1.text)
            name = json_data1['name']
            category = json_data1['catLvl1Name']
            category1 = json_data1['catLvl2Name']
            category2 = json_data1['catLvl3Name']
            img_url = json_data1['image']
            try:    
                os.mkdir(name.replace("/",' ').replace(':'," ").replace('.'," ").strip())
            except:
                pass 
            image_url = name.replace("/",' ')+"//"+name.replace("/",' ').replace(':'," ").replace('.'," ").strip()+".jpg"
            urllib.request.urlretrieve(img_url,name.replace("/",' ').replace(':'," ").replace('.'," ").strip()+"//"+name.replace('.'," ").replace("/",' ').replace(':'," ").strip()+".jpg")
            description = json_data1['productDescription'].replace(" <li>", ", ")
            page_url = "https://www.ironmongerydirect.co.uk/product/" + json_data1['skuUrl']
            store =[id,name,category,category1,category2,img_url,description,page_url]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()