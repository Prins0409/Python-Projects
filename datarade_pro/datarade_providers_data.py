from lib2to3.pgen2 import driver
from selenium import webdriver
import time,json,csv
from bs4 import BeautifulSoup
from encodings.utf_8 import encode

PATH = "C:\Program Files (x86)\chromedriver_win32_2\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def write_output(data):
    with open('datarade_providers_data.csv', mode='w', newline="", encoding='utf-8') as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(["title_name","title_provider","title_provider_location","description","all_logos","all_reviews","website_url","page_url"])
        for row in data:
            writer.writerow(row)
def fetch_data():
    with open('dataradeurls.csv','r') as f:
        for urls in f.readlines():
            driver.get(urls)
            time.sleep(3)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            try:
                title_name = soup.find("h1",{"class":"vendor__header-name"}).text.strip()
            except:
                title_name = ''
            title_provider = soup.find("div",{"class":"provider__trust-subheader"}).text.strip()
            title_provider_location = soup.find("div",{"class":"provider-profile__headquarter-country"}).text.strip()
            if title_provider == "No reviews yet":
                title_provider = ''
            elif title_provider == "No reviews yetVerified Data Provider":
                title_provider = ''
            else:
                title_provider = title_provider
            try:
                short_description = soup.find("div",{"class":"provider-profile__subtitle"}).text.strip()
            except:
                short_description = ''
            try:
                long_description = soup.find("div",{"class":"enhanced-readability m-b-xs"}).text.strip()
            except:
                long_description = ''
            description = str(short_description + '\n' + long_description)
            try:
                logos = []
                for all_logo in soup.find_all("div",{"class":"vendor-trust-bar__logo"}):
                    logo = str(all_logo.find("img",{"class":"ui image lazyloaded"})).split('src="')[1].split('png"/>')[0]
                    logos.append(logo)
                all_logos = "; ".join(logos)
            except:
                all_logos = ''
            try:
                reviews = []
                for all_reviewer in soup.find_all("div",{"class":"reviews-list__review-header-author"}):
                    reviewer_name = all_reviewer.find("div",{"class":"reviews-list__review-header-author-name"}).text
                    reviewer_company = all_reviewer.find("div",{"class":"reviews-list__review-header-author-company"}).text
                    review = reviewer_name + ',' + reviewer_company
                    reviews.append(review)
                all_reviews = "; ".join(reviews)
            except:
                all_reviews = ''
            website_urls = str(soup.find_all("script",{"type":"application/ld+json"})[1]).split('ld+json">')[1].split('</script>')[0]
            json_data = json.loads(website_urls)
            website_url = json_data['url']
            page_url = urls
            print(page_url)
            store = [title_name,title_provider,title_provider_location,description,all_logos,all_reviews,website_url,page_url]
            yield store
    time.sleep(5)
    driver.quit()
def scrape():
    data = fetch_data()
    write_output(data)
scrape()