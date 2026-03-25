import requests
import csv
from bs4 import BeautifulSoup
import json

# def write_output(data):
# 	with open('currys.csv', mode='a', newline="", encoding='utf-8') as output_file:
# 		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
# 		writer.writerow([])
# 		for row in data:
# 			writer.writerow(row)

# def fetch_data():
#   proxies = { 'https' : 'https://brd-customer-c_878f6dc2-zone-zone_priceline_development-country-us:ixuzrn0hwwpw@zproxy.lum-superproxy.io:22225' } 
#   for i in range(1, 297):
#     j = i * 30
#     print(i)
url = "https://www.currys.co.uk/computing/laptops/laptops?start=20&sz=20&viewtype=listView"
headers = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,gu;q=0.4,de;q=0.3',
'cookie': 'ACS={"mcvisid":"43896773743037628752567834049589526192"}; logglytrackingsession=87b935b2-ca0e-4046-a1c4-b66c5a2d202e; sid=kaiVaQrjJDx0bl4J605lvKfGfq9enWMtaOg; dwanonymous_c1575c7fdffeee6c1c87c9bab9ccac08=abEJmWTfPIcOPaTVzHY1ZykR4c; dwsid=uku8lc54nahQRqWNTHpX84wlV1OaBtq5TMAMhVpGqGKxOAVoXRXW1YJMrFafGrJ_JJ4hjzpYhu1XcSKo74glBA==; AMCVS_0DC638B35278395A0A490D4C%40AdobeOrg=1; _cs_mk_aa=0.4071089087119546_1672311398842; gpv_login=logged_out; OptanonAlertBoxClosed=2022-12-29T10:56:42.356Z; QueueITAccepted-SDFrts345E-V3_peakcurrys2020=EventId%3Dpeakcurrys2020%26RedirectType%3Dsafetynet%26IssueTime%3D1672311402%26Hash%3Da45c3e9bbc94965ad7a85da110059dc64e00be7e9e5b71d665b6098015129a36; _gid=GA1.3.1799294216.1672311405; _gcl_au=1.1.1402658463.1672311405; s_cc=true; _cs_c=1; AMCV_0DC638B35278395A0A490D4C%40AdobeOrg=-2121179033%7CMCIDTS%7C19356%7CMCMID%7C43896773743037628752567834049589526192%7CMCAAMLH-1672916213%7C7%7CMCAAMB-1672916213%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1672318613s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C914077848%7CvVersion%7C5.3.0; ACS={"mcvisid":"43896773743037628752567834049589526192"}; lantern=08ada670-072d-44e5-9a5d-92a70f5d7135; smc_uid=1672311417353184; smc_tag=eyJpZCI6MTkyNCwibmFtZSI6ImN1cnJ5cy5jby51ayJ9; smc_session_id=6oDkL1afjct3rUIysj2qGYOEr6BozuoP; smc_group_events=A; smc_group_test_value=B; smc_refresh=24866; _rl_rl=0; _rlgm=83|y|1dHnC6uC|MZ9mK38LQ:y/289AKB5D1:y|; _rlu=b89d677a-4f0d-40c2-b173-a03d60e6d8d2; _rlsnk=b89d_lc8z1glf; smct_dyn_BasketCount=0; smc_sesn=1; smc_not=default; _mibhv=anon-1672311420907-859996693_8082; _tt_enable_cookie=1; _ttp=Vs1tKo9th9TcpCjIMkKUaIPisO9; _fbp=fb.2.1672311429448.215299183; dwOptanonConsentCookie=true; dwpersonalization_c1575c7fdffeee6c1c87c9bab9ccac08=0a434d5a8bdd9521bf7b42993f20221231000000000; __cq_dnt=0; dw_dnt=0; gpv_url=https%3A%2F%2Fwww.currys.co.uk%2Fcomputing%2Flaptops%2Flaptops; gpv_pg=Laptops; gpv_p10=Laptops; gpv_template=rendering%2Fcategory%2FPLP; dwac_2657edce74737ed44718c8ec2e=kaiVaQrjJDx0bl4J605lvKfGfq9enWMtaOg%3D|dw-only|||GBP|false|Europe%2FLondon|true; cqcid=abEJmWTfPIcOPaTVzHY1ZykR4c; cquid=||; __cq_uuid=a17bcda0-8767-11ed-807d-057134a27c2e; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __gads=ID=a919d7300dae91e5:T=1672311481:S=ALNI_MYd1vZFLfTlgu-2zqH4icLG803Z7Q; __gpi=UID=000008ea721a339c:T=1672311481:RT=1672311481:S=ALNI_MZTzncRMemQsuCAgrFRQwMgcaOGng; QSI_HistorySession=https%3A%2F%2Fwww.currys.co.uk%2F~1672311433465%7Chttps%3A%2F%2Fwww.currys.co.uk%2Fcomputing%2Flaptops%2Flaptops%3FsearchTerm%3Dlaptop~1672311496152; at_check=true; QSI_CT={"GIS Call-CTA-Shown":3}; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Dec+29+2022+16%3A39%3A37+GMT%2B0530+(India+Standard+Time)&version=6.20.0&isIABGlobal=false&hosts=&consentId=0fcae827-86dd-4140-8919-a4986ad3b242&interactionCount=1&landingPath=NotLandingPage&groups=C0008%3A1%2CC0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=%3B&AwaitingReconsent=false; _ga=GA1.1.659113438.1672311405; mbox=session#0dba38d2d38a4f1c901e83b9b1f03fa0#1672314053|PC#0dba38d2d38a4f1c901e83b9b1f03fa0.34_0#1735556993; _uetsid=82db73b0876711edb72b7ffea6f3925c; _uetvid=82dc5a20876711edaa30f331cb6c7024; smc_tpv=6; smc_spv=6; cto_bundle=-gtwY19nTVolMkY4NDl6dXd0Q1owd3lRNGdWQ0ZzQiUyRmRvRGwlMkZvMm5mVDVVSkVLWUdZaDd5TlpZOENvajNJRDl0cU4lMkI1JTJCbXdpSXRSbFZvVk0zaWtrM1ZyUzBxcnZKSE5uVWhxVEpCWndycHFId2wxYnhNSjNjWDZhR1lHNE5SeU9uYUx6b2NIa3NKWnRzcVlDaEpvWHc3Tm5CbmNBJTNEJTNE; __cf_bm=lAjt3dOxvHu4nk8y3IkfpmS964YPYbAjza17TkbCXwo-1672312736-0-AbVyIgYP2vv+PkKAXqiI6Ngb0ayfjqe+lPEmxXmYiSUJY75icOW/tKnKd3rQb+Owf6yP05mBmQop+U/+kEy4ElA=; _gat_gtag_UA_16885468_32=1; _cs_id=6dba0b50-1a40-aa73-a544-b57a8cf46c0e.1672311411.1.1672312747.1672311411.1.1706475411765; _cs_s=6.0.0.1672314547269; s_sq=dixonsrtcurrysomnichannelprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DLaptops%2526link%253DHP%25252015s-eq2517na%25252015.6%252522%252520Laptop%252520-%252520AMD%252520Ryzen%2525203%25252C%252520256%252520GB%252520SSD%25252C%252520Silver%2526region%253Dhash-10238815%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c; smct_session=%7B%22s%22%3A1672311418406%2C%22l%22%3A1672312756823%2C%22lt%22%3A1672312756825%2C%22t%22%3A1010%2C%22p%22%3A330%7D; _ga_3VD8P50ZM5=GS1.1.1672311405.1.1.1672312757.31.0.0',
'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
response = requests.request("GET", url, headers=headers,)
soup = BeautifulSoup(response.text, 'html.parser')
print(response.text)
print(response)


#       store =[]
#       yield store
# def scrape():
#     data = fetch_data()
#     write_output(data)
# scrape()

