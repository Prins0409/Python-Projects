from lib2to3.pgen2 import driver
from selenium import webdriver
import time,json,csv
from bs4 import BeautifulSoup
from encodings.utf_8 import encode

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://datarade.ai/data-categories")
time.sleep(3)

def write_output(data):
    with open('datarade.csv', mode='w', newline="", encoding='utf-8') as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(["page_url"])
        for row in data:
            writer.writerow(row)
def fetch_data():
    soup1 = BeautifulSoup(driver.page_source, 'html.parser')
    for site_name in soup1.find_all("a",{"class":"categories__list-item"}):
        title = site_name.find("h2",{"class":"categories__list-item__title"}).text.strip().replace(" ","+")
        for_url = "https://datarade.ai" + site_name['href']
        driver.get(for_url)
        time.sleep(3)
        soup2 = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup2.find("div",{"class":"item-search-rendered__count"}).text.strip().replace("Results","").replace(" ","")
        if results != range(0,11):
            sub_link = "https://datarade.ai/search/products?keywords=" + title
            driver.get(sub_link)
            time.sleep(2)
            soup4 = BeautifulSoup(driver.page_source, 'html.parser')
            for no_of_pages in soup4.find_all("div",{"class":"dtrd-menu pagination"}):
                no_of_page = no_of_pages.find("a",{"class":"item"})
                sub_links = "https://datarade.ai/search/products?keywords=" + title + "&page=" + str(no_of_page)
                driver.get(sub_links)
                time.sleep(3)
                soup2 = BeautifulSoup(driver.page_source, 'html.parser')
                for links in soup2.find_all("div",{"class":"data-product-card__trust-logo"}):
                    link = "https://datarade.ai" + links.find("a")["href"]
                    print(link)
                    store = [link]
                    yield store
        else:
            for links in soup2.find_all("div",{"class":"data-product-card__trust-logo"}):
                link = "https://datarade.ai" + links.find("a")["href"]
                print(link)
                store = [link]
                yield store
    time.sleep(5)
    driver.quit()
def scrape():
    data = fetch_data()
    write_output(data)
scrape()