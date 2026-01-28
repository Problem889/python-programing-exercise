import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

movies = soup.find_all('div', class_='item')
for movie in movies:
    title = movie.find('span', class_='title').get_text()
    rating = movie.find('span', class_='rating_num').get_text()
    print(f'Title: {title}, Rating: {rating}')