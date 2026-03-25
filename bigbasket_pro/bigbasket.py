from bs4 import BeautifulSoup
import requests
import csv, json

def write_output(data):
	with open('bigbasket.csv', mode='a', newline="", encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name", "price", "image", "description", "page_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    proxies = {
    'http': 'https://brd-customer-c_878f6dc2-zone-zone_priceline_development-country-us:ixuzrn0hwwpw@zproxy.lum-superproxy.io:22225'
    }
    count = 1
    while True:
        print(count)
        url = "https://www.bigbasket.com/listing-svc/v2/products?type=ps&slug=rice&page=" + str(count)
        count += 1
        headers = {
        'accept-encoding': 'gzip, deflate, br',
        'cookie': '_bb_locSrc=default; _bb_cid=3; x-channel=web; _bb_loid=4460; _bb_bhid=; _bb_nhid=6; _bb_vid=NjU3NzI2MDEyNw==; _bb_dsevid=; _bb_dsid=; csrftoken=QRUSEdnLXeQPkbDQzwZjgXgSWktpSs8e6vcleVPjEoCdArqvrADcbTuVNZ1Vsy6j; _bb_home_cache=941df463.2.visitor; _bb_bb2.0=1; is_global=0; _bb_sa_ids=10198; isPwaPilot=false; bb2_enabled=true; ufi=1; _gcl_au=1.1.343909026.1671518298; bigbasket.com=19c7d04d-18b2-49f1-94b0-d8698e3616ea; _bb_hid=6; sessionid=b38u5sbs0xw0h4wgvn2lftq40aqnzbxn; _bb_aid="MzE2MzExOTIyNw=="; adb=0; _bb_tc=0; _bb_rdt="MzExODkxNzExMQ==.0"; _bb_rd=6; _gid=GA1.2.2040852836.1671518299; _fbp=fb.1.1671518299646.373723046; _client_version=2620; csurftoken=PRholA.NjU3NzI2MDEyNw==.1671599284810.viB9IPNnRtoTcpuTd5BVpXL658t/lgypAPOOIQH7H70=; _ga=GA1.2.895175931.1671518298; _gat_UA-27455376-1=1; ts=2022-12-21 05:11:13.363; _ga_FRRYG5VKHX=GS1.1.1671599288.4.1.1671599474.0.0.0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        response = requests.request("GET", url, headers=headers, proxies=proxies)
        if response.status_code != 200:
            break
        json_data = json.loads(response.text)

        for data in json_data["tabs"]:
            for data1 in data["product_info"]["products"]:
                urls = "https://www.bigbasket.com" + data1["absolute_url"]
                print(urls)
                response1 = requests.request("GET", urls, headers=headers)
                soup = BeautifulSoup(response1.text, 'html.parser')
                data4 = str(soup.find("script",{"type":"application/json"})).split('type="application/json">')[1].replace("</script>","")
                open("test.txt",'w',encoding='utf-8').write(str(data4))
                json_data1 = json.loads(data4)
                name = json_data1["props"]["pageProps"]["productDetails"]["children"][0]["desc"]
                price = json_data1["props"]["pageProps"]["productDetails"]["children"][0]["pricing"]["discount"]["prim_price"]["sp"]
                img = []
                for data3 in json_data1["props"]["pageProps"]["productDetails"]["children"][0]["images"]:
                    data2 = data3["s"]
                    img.append(data2)
                image = ", ".join(img)
                description = str(json_data1["props"]["pageProps"]["productDetails"]["children"][0]["tabs"][0]["content"]).split("<ul>")[1].replace("<li>","").replace("</li>","").replace("</ul>","").replace("</div>","").strip()
                page_url = urls
                store =[name, price, image, description, page_url]
                yield store

def scrape():
    data = fetch_data()
    write_output(data)
scrape()
