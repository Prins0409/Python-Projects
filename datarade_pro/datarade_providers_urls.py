from bs4 import BeautifulSoup

with open('datarade.xml','r') as f:
    file = f.read()
soup = BeautifulSoup(file, 'xml')
with open('dataradeurls.csv','w',encoding='utf-8') as f:
    for links in soup.find_all("url"):
        url = links.text.split("2022")[0].split("2021")[0].split("2020")[0]
        if "/data-providers/" in url:
            if "profile" in url:
                continue
            urls = url.split("alternatives")[0]+'\n'
            print(urls)
            f.write(str(urls))