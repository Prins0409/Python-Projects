from ast import While
import requests
import json
import csv
import requests
import json
import csv
import requests, csv, time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# elliscolindj@gmail.com
# business_email_with_10k_plus_followers

def write_data(data):
    with open('emails_data11.csv', mode='a', encoding="utf-8", newline="") as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(data)

write_data(["birthdate","code","country","description","follower_count","following_count","index","name","sec_key","username","email","verify"])

# def write_output(data):
#     with open("verify_data.csv", mode="w",newline="") as output_file:
#         writer = csv.writer(output_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
#         # Header
#         writer.writerow(["username","name","email","follower_count","engagement_rate"])
#         # Body
#         for row in data:
#             writer.writerow(row)


def get_cookies():
	global headers
	chrome_options = Options()
	chrome_options.add_argument("no-sandbox")
	chrome_options.add_argument("--disable-gpu")
	chrome_options.add_argument("--disable-dev-shm-ussage")
	chrome_options.add_argument("--allow-running-insecure-content")
	chrome_options.add_argument("--disable-web-security")
	driver = webdriver.Chrome(ChromeDriverManager().install())

	return driver
	
	
		
def fetch_data():

	driver = get_cookies()

	fs = csv.DictReader(open("tiktok_10k_email_bio_and_gmail_230K_data.csv",'r',encoding='utf-8'))
	
	for index,ts in enumerate(fs):
		if "<<not-applicable>>" == ts['email']:
			continue
		print("::: ",ts['email'])
		time.sleep(2)
		# booking@espacial.pt
		# wesoo92@yahoo.com
		# date2 = driver.find_element("xpath", '/html/body/div[3]/div/div/main/article/div/div/div[2]/div[1]/div/form/div/p/input[1]')
		cont = 0 
		while True:
			try:
				# time.sleep(4)
				driver.get("https://breadcrumbs.io/email-verification")
				time.sleep(3)
				driver.delete_all_cookies()
				date2 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/main/article/div/div/div[2]/div[1]/div/form/div/p/input[1]")))
				# driver.find_element("xpath", '/html/body/div[3]/div/div/main/article/div/div/div[2]/div[1]/div/form/div/p/input[1]')
				date2.clear()
				date2.send_keys(ts['email'])
				e2 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/main/article/div/div/div[2]/div[1]/div/form/div/p/input[2]")))
				# driver.find_element("xpath", '/html/body/div[3]/div/div/main/article/div/div/div[2]/div[1]/div/form/div/p/input[2]').click()
				e2.click()
				time.sleep(5)
				try:
					e3 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/main/article/div/div/div[2]/div[1]/div/div/div/div[2]/div[7]/i")))
				except:
					e3 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/main/article/div/div/div[2]/div[1]/div/div/div/div[3]/div[7]/i")))
					
				fs = e3.get_attribute('class').strip()
				# fs = driver.find_element("xpath", '/html/body/div[3]/div/div/main/article/div/div/div[2]/div[1]/div/div/div/div[2]/div[7]/i').get_attribute('class').strip()
				# fs = driver.find_element("xpath", '/html/body/div[3]/div/div/main/article/div/div/div[2]/div[1]/div/div/div/div[2]/div[7]/i').get_attribute('class').strip()
				ttts = "Yes"
				if "icon icon-status status-false status-negative" == fs:
					ttts = "No"
				print("::: ",ttts)
				# yield [ts['username'],ts['name'],ts['email'],ts['follower_count'],ts['engagement_rate'],ttts]
				
				write_data([ts['birthdate'],ts['code'],ts['country'],ts['description'],ts['follower_count'],ts['following_count'],ts['index'],ts['name'],ts['sec_key'],ts['username'],ts['email'],ttts])
				break
			except:
				cont += 1
				if cont >= 3:
					break
				else:
					driver = get_cookies()
					continue
				

				
				

fetch_data()

# def scrape():
#     data = fetch_data()
#     write_output(data)

# scrape()
