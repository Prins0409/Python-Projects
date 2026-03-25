from encodings.utf_8 import encode
from bs4 import BeautifulSoup
import requests
import csv
def write_output(data):
	with open('taxpayer.csv', mode='w', newline="", encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["business","address","city_state_zip","contact","telephone","service","page_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    for i in range(26338,26726):
        url = "https://www.irs.gov/efile-index-taxpayer-search?zip=&state=All&page="+str(i)
        payload={}
        headers = {
        'Cookie': '_abck=0A199F71F1E20591EFB875EF0D3E6F94~-1~YAAQpJQZuKvrlJCCAQAASiwnkwgo5Z8M7KJCpdEyQgXc/6tzSYRlflmcxeHfE7NWlTvJi1wBLgFtHCgvq1U2qqzCMCfVZM18WaIs+4BfrAmLkuIumX65Ph4J3XYTs6dQi6jyy0Yu9FDErOEm0eXFzDpInhH53drFTKMSMlmKulGRT8umWfHGo+VumXhmmTDYMkW1s/8rmO11FTHng7S8nrVTWkzmwNsskS5XH7xi0LXax3cBCVLjNoi/QmAQ/jMraa9z3H9R71xZ44QxkZm0Bt1zHmO2Yjf4p79dEHCMbI1xggrgBgBRIZXFMbGyIED1K3FrFY3bpfEr9gjsyUFX7tsILboAHPRCFyHQ0j4B2E3z5Nb4pfo=~-1~-1~-1; bm_sz=5280835FA816C16263F123F3E9B86AAE~YAAQpJQZuKzrlJCCAQAASiwnkxDygDsgsLJxS/y/LfR3iSYtAc2Wsz8D1j2MtEOTZpPqEWDuNXpDjzi1FBN9PuU7/U0Z8HLs9igl5BmRh03f9pK7dP54FdGZhLdwBuU4dvoDVQ0jO9bxNB44+6l2/sAJEN/q/tYScI+D9t66Kss+eoWCvk2AyZZdcFXvEogi5nnzH3e2jpO1d43oXd9PMd/lw3XZCEv53FCzWoIOJ3+KT1nP0K8CN0yyMUjA20VHBtOlxH1TN/5kBSfEh7rfZMu4+ir33IDZdnxI7ksqv5o=~3294519~3158337'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        soup = BeautifulSoup(response.text, 'html.parser')

        datas = soup.find("table",{"class":"tablesaw tablesaw-stack table table-hover table-striped pup-table"}).find_all("tr")
        for item in datas:
            business = item.find("td",{"class":"views-field views-field-nothing-1 views-align-left"}).text.splitlines()[0].replace('"','')
            print(business)
            address = item.find("td",{"class":"views-field views-field-nothing-1 views-align-left"}).text.splitlines()[1]
            city_state_zip = item.find("td",{"class":"views-field views-field-nothing-1 views-align-left"}).text.splitlines()[2]
            contact = item.find("td",{"class":"views-field views-field-nothing-1 views-align-left"}).text.splitlines()[3]
            telephone = item.find("td",{"class":"views-field views-field-nothing-1 views-align-left"}).text.splitlines()[4]
            service = item.find("td",{"class":"views-field views-field-nothing-1 views-align-left"}).text.splitlines()[5]
            page_url = url
            store =[business,address,city_state_zip,contact,telephone,service,page_url]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()