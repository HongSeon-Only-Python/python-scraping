import requests
from bs4 import BeautifulSoup as bs4
import pandas as pd
# import csv

url = "https://movie.naver.com/movie/running/current.nhn"
res = requests.get(url)

soup = bs4(res.text, "html.parser")
get_a = soup.select("dt.tit > a")
movie = []


for a_tag in get_a:
    movie_data = {}
    movie_data['title'] = a_tag.text
    # movie_data['href'] = a_tag["href"]
    movie_data['code'] = a_tag["href"].split("code=")[1]
    movie.append(movie_data)

print(movie)

df = pd.DataFrame(movie, columns=['title', 'code'])
df.to_csv(r'movie.csv', header=True, index=False)

# with open('./movie.csv', 'a') as csvfile:
#         fieldnames = ['name', 'code']
#         csvwriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
#         csvwriter.writerow(movie)