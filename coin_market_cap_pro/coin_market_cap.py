import csv
import requests
import json
from bs4 import BeautifulSoup

def write_output(data):
	with open('coin_market_cap.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["coin_name","coin_symbol","coin_slug","coin_price","coin_volume24h","coin_volume7d","coin_volume30d","coin_marketCap","coin_percentChange1h","coin_percentChange24h","coin_percentChange7d","coin_marketCapByTotalSupply","coin_circulatingSupply","cryptos","exchanges","market_cap","crypto_24h_volume","dominance","eth_Gas","todays_crypto_market_cap","todays_market_increase_or_decrease"])
		for row in data:
			writer.writerow(row)
            
def fetch_data():
    for i in range(0,90):
        j = (i*100)
        url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start="+str(1+j)+"&limit=100&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap"
        url1 = "https://coinmarketcap.com/"
        headers = {
        "accept": "application/json, text/plain, */*",
        "origin": "https://coinmarketcap.com",
        "referer": "https://coinmarketcap.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "x-request-id": "12fa0c469d9240fcb27bd971319e0529"
        }
        response = requests.request("GET", url, headers=headers)
        response1 = requests.request("GET", url1, headers=headers)
        soup = BeautifulSoup(response1.text, 'html.parser')
        json_data = json.loads(response.text)
        for data in json_data['data']['cryptoCurrencyList']:
            coin_name = data['name']
            coin_symbol = data['symbol']
            coin_slug = data['slug']
            coin_price = data['quotes'][2]['price']
            coin_volume24h = data['quotes'][2]['volume24h']
            coin_volume7d = data['quotes'][2]['volume7d']
            coin_volume30d = data['quotes'][2]['volume30d']
            coin_marketCap = data['quotes'][2]['marketCap']
            coin_percentChange1h = data['quotes'][2]['percentChange1h']
            coin_percentChange24h = data['quotes'][2]['percentChange24h']
            coin_percentChange7d = data['quotes'][2]['percentChange7d']
            coin_marketCapByTotalSupply = data['quotes'][2]['marketCapByTotalSupply']
            coin_circulatingSupply = data['circulatingSupply']
            cryptos = soup.find("div",{"class":"sc-c3d05745-1 dbjsyd global-stats"}).find("span",{"class":"sc-d7deda17-0 kHANOr"}).text.strip().replace("Cryptos:","").strip()
            exchanges = soup.find("div",{"class":"sc-c3d05745-1 dbjsyd global-stats"}).find_all("span",{"class":"sc-d7deda17-0 kHANOr"})[1].text.strip().replace("Exchanges:","").strip()
            market_cap = soup.find("div",{"class":"sc-c3d05745-1 dbjsyd global-stats"}).find_all("span",{"class":"sc-d7deda17-0 kHANOr"})[2].text.strip().replace("Market Cap:","").strip()
            crypto_24h_volume = soup.find("div",{"class":"sc-c3d05745-1 dbjsyd global-stats"}).find_all("span",{"class":"sc-d7deda17-0 kHANOr"})[3].text.strip().replace("24h Vol:","").strip()
            dominance = soup.find("div",{"class":"sc-c3d05745-1 dbjsyd global-stats"}).find_all("span",{"class":"sc-d7deda17-0 kHANOr"})[4].text.strip().replace("Dominance:","").strip()
            eth_Gas = soup.find("div",{"class":"sc-c3d05745-1 dbjsyd global-stats"}).find_all("span",{"class":"sc-d7deda17-0 kHANOr"})[5].text.strip().replace("ETH Gas:","").strip()
            todays_crypto_market_cap = soup.find("div",{"class":"sc-aef7b723-0 EPENP"}).find("p").text.strip().split(", a")[0] + ", a"
            todays_market_increase_or_decrease = soup.find("div",{"class":"sc-aef7b723-0 EPENP"}).find("p").text.strip().split(", a")[1].strip()
            
            store =[coin_name,coin_symbol,coin_slug,coin_price,coin_volume24h,coin_volume7d,coin_volume30d,coin_marketCap,coin_percentChange1h,coin_percentChange24h,coin_percentChange7d,coin_marketCapByTotalSupply,coin_circulatingSupply,cryptos,exchanges,market_cap,crypto_24h_volume,dominance,eth_Gas,todays_crypto_market_cap,todays_market_increase_or_decrease]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()
