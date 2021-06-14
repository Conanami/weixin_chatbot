import requests
from bs4 import BeautifulSoup 
import pprint
import json

def download_all_htmls():
    htmls=[]
    for idx in range(24):
        url = f"http://www.crazyant.net/page/{idx+1}"
        print("crawl html:",url)
        r = requests.get(url)
        if r.status_code !=200:
            raise Exception("error")
        htmls.append(r.text)
    return htmls
#htmls = download_all_htmls()

def parse_single_html(html):
    soup = BeautifulSoup(html,'html.parser')
    articles = soup.find_all("article")
    datas=[]
    for article in articles:
        title_node = (
            article.find('h2',class_='entry-title')
            .find('a')
        )
        title = title_node.get_text()
        link = title_node['href']
        # #查找标签列表
        publish_date=(
            article.find("div")
            .find("p")
            

        )

        #print(publish_date)
        datas.append(
            {"title":title,"link":link}
            )
    return datas

htmls = download_all_htmls()
all_datas=[]
for html in htmls:
    all_datas.extend(parse_single_html(html))

with open("all-article-links.json","w") as fout:
    for data in all_datas:
        fout.write(json.dumps(data,ensure_ascii=False)+"\n")

