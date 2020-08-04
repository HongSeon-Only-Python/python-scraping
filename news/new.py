import requests
import pandas as pd
from bs4 import BeautifulSoup as bs4
import csv
soup_object = []
for i in range(1,102,10):

    base_url = 'https://search.naver.com/search.naver?&where=news&query=%EA%B4%91%EC%A3%BC%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%EC%82%AC%EA%B4%80%ED%95%99%EA%B5%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=32&start='
    start_num = i
    end_url ='&refresh_start=0'

    URL = base_url + str(start_num) + end_url
    res = requests.get(URL)
    soup = bs4(res.text, 'html.parser')
    soup_object.append(soup)

titles = []
hrefs = []
for soup in soup_object:
    news_section=(soup.select('div[id=wrap] > div[id=container] > div[id=content] > div[id=main_pack] > div.news.mynews.section._prs_nws > ul.type01 > li'))

    for news in news_section:
    
        title = news.select_one('dl > dt > a').get_text()
        href = news.select_one('dl > dt > a')['href']
        # print('title : {}, href : {}'.format(title, href), '\t')
        
        news_data = {
            "title" : title,
            "news_link" : href 
        }
        titles.append(title)
        hrefs.append(href)
        
        
# print(news_data)
# df_news_data = pd.DataFrame(news_data) 
# pd.to_csv('news_Data', df_news_data)
    # csv file 만들기
    with open('./naver_csv','a') as csvfile:
        fieldnames = ['title','news_link']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writerow(news_data)