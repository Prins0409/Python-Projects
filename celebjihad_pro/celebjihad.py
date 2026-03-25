import requests
from bs4 import BeautifulSoup
import csv, re
import json

def write_output(data):
	with open('celebjihad.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["website_url","page_url","video_title","length_of_video","number_of_views","date_of_upload","uploader_username","categories","tags","video_description","related_video_titles"])
		for row in data:
			writer.writerow(row)
def fetch_data():
	for i in range(1,542):
		print(i)
		url = "https://celebjihad.com/wp-admin/admin-ajax.php"
		payload = "action=view_more_posts&nonce=9c7877aacc&page="+str(i)+"&data=a%3A62%3A%7Bs%3A4%3A%22page%22%3Bi%3A0%3Bs%3A5%3A%22error%22%3Bs%3A0%3A%22%22%3Bs%3A1%3A%22m%22%3Bs%3A0%3A%22%22%3Bs%3A11%3A%22post_parent%22%3Bs%3A0%3A%22%22%3Bs%3A7%3A%22subpost%22%3Bs%3A0%3A%22%22%3Bs%3A10%3A%22subpost_id%22%3Bs%3A0%3A%22%22%3Bs%3A10%3A%22attachment%22%3Bs%3A0%3A%22%22%3Bs%3A13%3A%22attachment_id%22%3Bi%3A0%3Bs%3A6%3A%22second%22%3Bs%3A0%3A%22%22%3Bs%3A6%3A%22minute%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22hour%22%3Bs%3A0%3A%22%22%3Bs%3A3%3A%22day%22%3Bi%3A0%3Bs%3A8%3A%22monthnum%22%3Bi%3A0%3Bs%3A4%3A%22year%22%3Bi%3A0%3Bs%3A1%3A%22w%22%3Bi%3A0%3Bs%3A13%3A%22category_name%22%3Bs%3A0%3A%22%22%3Bs%3A3%3A%22tag%22%3Bs%3A0%3A%22%22%3Bs%3A3%3A%22cat%22%3Bs%3A0%3A%22%22%3Bs%3A6%3A%22tag_id%22%3Bs%3A0%3A%22%22%3Bs%3A6%3A%22author%22%3Bs%3A0%3A%22%22%3Bs%3A11%3A%22author_name%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22feed%22%3Bs%3A0%3A%22%22%3Bs%3A2%3A%22tb%22%3Bs%3A0%3A%22%22%3Bs%3A5%3A%22paged%22%3Bi%3A0%3Bs%3A8%3A%22meta_key%22%3Bs%3A0%3A%22%22%3Bs%3A10%3A%22meta_value%22%3Bs%3A0%3A%22%22%3Bs%3A7%3A%22preview%22%3Bs%3A0%3A%22%22%3Bs%3A1%3A%22s%22%3Bs%3A0%3A%22%22%3Bs%3A8%3A%22sentence%22%3Bs%3A0%3A%22%22%3Bs%3A5%3A%22title%22%3Bs%3A0%3A%22%22%3Bs%3A6%3A%22fields%22%3Bs%3A0%3A%22%22%3Bs%3A10%3A%22menu_order%22%3Bs%3A0%3A%22%22%3Bs%3A5%3A%22embed%22%3Bs%3A0%3A%22%22%3Bs%3A12%3A%22category__in%22%3Ba%3A0%3A%7B%7Ds%3A16%3A%22category__not_in%22%3Ba%3A0%3A%7B%7Ds%3A13%3A%22category__and%22%3Ba%3A0%3A%7B%7Ds%3A8%3A%22post__in%22%3Ba%3A0%3A%7B%7Ds%3A12%3A%22post__not_in%22%3Ba%3A0%3A%7B%7Ds%3A13%3A%22post_name__in%22%3Ba%3A0%3A%7B%7Ds%3A7%3A%22tag__in%22%3Ba%3A0%3A%7B%7Ds%3A11%3A%22tag__not_in%22%3Ba%3A0%3A%7B%7Ds%3A8%3A%22tag__and%22%3Ba%3A0%3A%7B%7Ds%3A12%3A%22tag_slug__in%22%3Ba%3A0%3A%7B%7Ds%3A13%3A%22tag_slug__and%22%3Ba%3A0%3A%7B%7Ds%3A15%3A%22post_parent__in%22%3Ba%3A0%3A%7B%7Ds%3A19%3A%22post_parent__not_in%22%3Ba%3A0%3A%7B%7Ds%3A10%3A%22author__in%22%3Ba%3A0%3A%7B%7Ds%3A14%3A%22author__not_in%22%3Ba%3A0%3A%7B%7Ds%3A19%3A%22ignore_sticky_posts%22%3Bb%3A0%3Bs%3A16%3A%22suppress_filters%22%3Bb%3A0%3Bs%3A13%3A%22cache_results%22%3Bb%3A1%3Bs%3A22%3A%22update_post_term_cache%22%3Bb%3A1%3Bs%3A19%3A%22lazy_load_term_meta%22%3Bb%3A1%3Bs%3A22%3A%22update_post_meta_cache%22%3Bb%3A1%3Bs%3A9%3A%22post_type%22%3Bs%3A4%3A%22post%22%3Bs%3A14%3A%22posts_per_page%22%3Bi%3A18%3Bs%3A8%3A%22nopaging%22%3Bb%3A0%3Bs%3A17%3A%22comments_per_page%22%3Bs%3A1%3A%227%22%3Bs%3A13%3A%22no_found_rows%22%3Bb%3A0%3Bs%3A5%3A%22order%22%3Bs%3A4%3A%22desc%22%3Bs%3A11%3A%22post_status%22%3Bs%3A7%3A%22publish%22%3Bs%3A7%3A%22orderby%22%3Bs%3A4%3A%22date%22%3B%7D&vars=a%3A4%3A%7Bs%3A10%3A%22blog_style%22%3Bs%3A7%3A%22puzzles%22%3Bs%3A17%3A%22show_sidebar_main%22%3Bs%3A5%3A%22right%22%3Bs%3A13%3A%22parent_cat_id%22%3Bi%3A0%3Bs%3A3%3A%22ppp%22%3Bi%3A18%3B%7D"
		headers = {
		'content-length': '2818',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'cookie': '_ga=GA1.2.3265766.1663174998; _gid=GA1.2.1207044114.1663785948; _gat_gtag_UA_155987648_1=1',
		'origin': 'https://celebjihad.com',
		'referer': 'https://celebjihad.com/main5',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		json_data = json.loads(response.text)
		data = json_data['data']
		soup = BeautifulSoup(data, 'html.parser')
		for for_url in soup.find_all("h2",{"class":"post_subtitle"}):
			links = for_url.find("a")["href"]
			website_url = "https://celebjihad.com/main5"
			page_url = links
			print(page_url)
			headers1 = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'cookie': '_ga=GA1.2.3265766.1663174998; _gid=GA1.2.1207044114.1663785948',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
			}
			response1 = requests.request("GET", page_url, headers=headers1)
			soup1 = BeautifulSoup(response1.text, 'html.parser')
			video_title = soup1.find("meta",{"property":"og:title"})["content"]
			length_of_video = ''
			number_of_views = ''
			try:
				date_of_upload = soup1.find("meta",{"itemprop":"uploadDate"})["content"].split("T")[0]
			except:
				date_of_upload = ''
			uploader_username = ''
			tags = ''
			categories = ''
			try:
				video_description = soup1.find("meta",{"itemprop":"description"})["content"]
			except:
				video_description = ''
			try:
				for related_video_title in soup1.find_all("a",{"class":"popular"}):
					related_video_titles = related_video_title.text.strip()
			except:
				related_video_titles = ''
			store =[website_url,page_url,video_title,length_of_video,number_of_views,date_of_upload,uploader_username,categories,tags,video_description,related_video_titles]
			yield store
def scrape():
	data = fetch_data()
	write_output(data)
scrape()
