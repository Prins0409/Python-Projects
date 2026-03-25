from lib2to3.pgen2 import driver
from selenium import webdriver
import time,json,csv
from bs4 import BeautifulSoup
from encodings.utf_8 import encode

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.carmax.com/cars")
time.sleep(3)
soup = BeautifulSoup(driver.page_source, 'html.parser')

def write_output(data):
    with open('cars_links.csv', mode='w', newline="", encoding='utf-8') as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(["link"])
        for row in data:
            writer.writerow(row)
def fetch_data():
    urls = soup.find("div",{"class":"brand-tiles"})
    for url in urls.find_all("a",{"class":"icon-tile text-centered"}):
        link = url['href']
        print(link)
        store = [link]
        yield store
    urls1 = soup.find("div",{"class":"brand-links"})
    for url1 in urls1.find_all("a"):
        link = url1['href']
        print(link)
        store = [link]
        yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()