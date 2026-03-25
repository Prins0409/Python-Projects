import requests
from bs4 import BeautifulSoup
import csv

def write_output(data):
	with open('cFake.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["website_url","page_url","video_title","length_of_video","number_of_views","date_of_upload","uploader_username","categories","tags","video_description","related_video_titles"])
		for row in data:
			writer.writerow(row)
def fetch_data():
	for i in range(0,133):
		print(i)
		url = "https://cfake.com/videos/gallery/p"+str(i)+"/"
		payload={}
		headers = {
		'cookie': 'PHPSESSID=bvgglnl28fb3r6i0j1jcc3kj74; light=disable; __utmc=9731434; __utmz=9731434.1663175415.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); sort=1; sort_list=2; mcountry=246; mtag=163; _ga=GA1.2.801114621.1663175415; d=true; _gid=GA1.2.1005242621.1663782800; __utma=9731434.801114621.1663175415.1663785915.1663868047.4; zone-cap-3975288=1; statu_picture=pending; statu_video=pending; _gat=1'
		}
		response = requests.request("GET", url, headers=headers, data=payload)
		soup = BeautifulSoup(response.text, "html.parser")
		for item in soup.find("div",{"id":"media_content"}).find_all("div",{"class":"responsive"}):
				website_url = "https://cfake.com/"
				video_title = item.find("div",{"id":"title_vignette"}).find("a").text.strip()
				try:
					length_of_video = item.find("div",{"id":"img_pellicule"}).find("a")['title'].replace("Duration :","").strip()
				except:
					length_of_video = ''
				date_of_upload = item.find("div",{"id":"date_vignette"}).text.strip()
				page_url = "https://cfake.com" + item.find("div",{"id":"img_pellicule"}).find("a")['href']
				if page_url == "https://cfake.com/register/":
					break
				print(page_url)
				headers1 = {
				'Cookie': 'PHPSESSID=ilsuet2c2gcakupuogcfp2tpu7'
				}
				response1 = requests.request("GET", page_url, headers=headers1)
				soup1 = BeautifulSoup(response1.text, "html.parser")
				try:
					for item1 in soup1.find("div",{"class":"content_tags"}).find_all("div",{"class":"tags"}):
						tags = item1.text.replace("Tags : ","").strip()
				except:
					tags = ''
				categories = ''
				uploader_username = ''
				number_of_views = ''
				try:
					video_description = soup1.find("meta",{"name":"description"})["content"].split(",")[0]
				except:
					video_description = ''
				all_titles = []
				for related_video_title in soup1.find_all("div",{"id":"title_vignette"}):
					related_video_titles = related_video_title.text.strip()
					all_titles.append(related_video_titles)
				related_video_titles = "; ".join(all_titles)
				store =[website_url,page_url,video_title,length_of_video,number_of_views,date_of_upload,uploader_username,categories,tags,video_description,related_video_titles]
				yield store
def scrape():
	data = fetch_data()
	write_output(data)
scrape()