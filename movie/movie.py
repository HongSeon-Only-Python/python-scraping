import requests
from bs4 import BeautifulSoup as bs4

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