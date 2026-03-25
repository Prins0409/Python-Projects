import csv
from bs4 import BeautifulSoup
import requests
import json
import urllib.request
import os
def write_output(data):
	with open('image.csv', mode='w',newline="") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","company","type","image_url","category","detail","finish","pack"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "amcookie_policy_restriction=allowed; _ga=GA1.2.1196373120.1654022380; f24_personId=66a6b839-03cd-4dbf-920b-7690fbfa34fe; f24_autoId=66a6b839-03cd-4dbf-920b-7690fbfa34fe; form_key=gsr722aCEcjJnBIn; PHPSESSID=2n9g8712a4rc7t4a3ogmhvcrsf; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; form_key=gsr722aCEcjJnBIn; mage-messages=; product_data_storage=%7B%7D; private_content_version=d5fce948ad6bc86f17c5f40eee089fc8; amcookie_allowed=0; section_data_ids=%7B%7D; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; _gid=GA1.2.1878784881.1654192790; _gat_UA-51553789-1=1",
        "referer": "https://www.carlislebrass.com/products",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    url = "https://www.carlislebrass.com/products"
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    for item in soup.find_all("a",{"class":"category-item-text"}):
        link = item['href']
        url2 = requests.get(link)
        soup2 = BeautifulSoup(url2.text, 'html.parser')
        for item2 in soup2.find_all("a",{"class":"category-item-text"}):
            link2 = item2['href']
            url3 = requests.get(link2)
            soup3 = BeautifulSoup(url3.text, 'html.parser')
            for item3 in soup3.find_all("div",{"class":"product-item-info"}):
                link4 = item3.find("a")['href']
                headers1 = {
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "cache-control": "max-age=0",
                    "cookie": "PHPSESSID=itthe9s53ihcj5po2vdf2o3eic; form_key=MvnPL75dFf9BeOOQ; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; amcookie_policy_restriction=allowed; mage-messages=; product_data_storage=%7B%7D; form_key=MvnPL75dFf9BeOOQ",
                    "referer": "https://www.carlislebrass.com/products/door-handles-knobs/lever-on-rose",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
                }
                url4 = requests.get(link4,headers=headers1)
                soup4 = BeautifulSoup(url4.text, 'html.parser')
                try:
                    details = soup4.find(text='Details').next_element.next_element.text
                except:
                    details =  ''
                title = soup4.find('span',{'data-ui-id':'page-title-wrapper'}).text.strip()
                try:
                    category = 'Home'+', All product, '+', '.join(link4.split('products/')[1].split('/')[0: -1]).capitalize().replace('-'," ") +', ' + title
                except:
                    category = 'Home'+', All product, '+', ' + title
                comp = soup4.find_all('img',{'loading':'lazy'})[2]['title']
                imgs = soup4.find_all('script',{'type':'text/x-magento-init'})[7]
                itm = json.loads(imgs.text)['[data-gallery-role=gallery-placeholder]']['mage/gallery/gallery']
                for itms in itm['data']:
                    main_img = itms['img']
                if soup4.find_all('div',{'class':'field configurable required'}) != []:
                    attr = soup4.find_all('div',{'class':'field configurable required'})[0].find('select')['id'].replace('attribute','').strip()
                    scrr = soup4.find_all('script',{'type':'text/x-magento-init'})[11]
                    immgse = '[{"thumb":"'+str(soup4).split('"data": [{"thumb":"')[1].split('}],')[0]+"}]"
                    imgse = json.loads(immgse)[0]['img_webp']
                    try:    
                        os.mkdir(title.replace("/",' '))
                    except:
                        pass 
                    urllib.request.urlretrieve(imgse,title.replace("/",' ')+"//"+title.replace("/",' ')+".jpg")
                    try:
                        attr1 = soup4.find_all('div',{'class':'field configurable required'})[1].find('select')['id'].replace('attribute','').strip()
                        tumb = json.loads(scrr.text)['#product_addtocart_form']['configurable']['spConfig']['images']
                        attributes = json.loads(scrr.text)['#product_addtocart_form']['configurable']['spConfig']['attributes'][attr]['options']
                        attributes1 = json.loads(scrr.text)['#product_addtocart_form']['configurable']['spConfig']['attributes'][attr1]['options']
                        main  = {}
                        for it1 in attributes:
                            for its in it1['products']:
                                main[its]=it1['label']   
                        op = {}
                        for index,it in enumerate(attributes1):
                            try:
                                
                                op[it['products'][0]] = it['label']
                            except:
                                continue
                        for thumbs in tumb:
                            tumbe = main[thumbs].strip()
                            for img in tumb[thumbs]:
                                imgss = img['img']
                                typse = imgss.split('/')[-1].replace('_'," ").split()[0].upper().replace('.JPG',"").strip()
                                try:
                                    file_name = op[thumbs].strip()
                                except:
                                    continue
                                try:
                                    os.mkdir(title.replace("/",' ')+"/"+tumbe.title.replace("/",' '))
                                except:
                                    pass
                                image_url = title+"/"+tumbe+"/"+file_name +".jpg"
                                urllib.request.urlretrieve(imgss, title.replace("/",' ')+"/"+tumbe.replace("/",' ')+"/"+file_name +".jpg")
                                store =[title,comp,typse,imgse,category,details,tumbe,file_name]
                                store = [str(x).encode('ascii', 'ignore').decode('ascii').strip() if x else "" for x in store]
                                yield store
                    except:
                        store =[title,comp,typse,imgse,category,details,tumbe,file_name]
                        store = [str(x).encode('ascii', 'ignore').decode('ascii').strip() if x else "" for x in store]
                        yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()