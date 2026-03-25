import csv
import requests
import json
from bs4 import BeautifulSoup

def write_output(data):
	with open('bright_data_1.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","title","company_name"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    json_data ={}
    # data1= open('4.json','r',encoding='utf-8')
    data1= open('5.json','r',encoding='utf-8')
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