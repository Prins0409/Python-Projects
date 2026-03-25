import csv
import requests
import json
from bs4 import BeautifulSoup

def write_output(data):
	with open('bright_datas.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","title","company_name"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    json_data ={}
    for i in range(0,7):
        if i == 4:
            continue
        if i == 5:
            continue
        data1= open(str(i)+'.json','r')
        datas = data1.read()
        json_data =json.loads(datas)
        datas = json_data["data"]["html"].replace("\\n","").replace("\\","")
        soup = BeautifulSoup(datas, 'html.parser')
        for all_data in soup.find_all("article",{"class":"brd_testimonial_item"}):
            name = all_data.find("div",{"class":"author_name"}).text.strip()
            title = all_data.find("div",{"class":"author_title"}).text.strip()
            try:
                company_names = all_data.find("div",{"class":"brd_testimonial_item_company_logo"}).find("img")["src"]
            except:
                company_names = ''
            if company_names != "": 
                if " at " in title:
                    company_name = title.split(" at ")[1].split(",")[0]
                elif " of " in title:
                    company_name = title.split(" of ")[1]
                elif ", " in title:
                    company_name = title.split(", ")[1]
                else:
                    company_name = title
            else:
                company_name = ''
            print(name)
            store =[name,title,company_name]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()