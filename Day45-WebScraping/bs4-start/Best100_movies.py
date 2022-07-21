from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")


web = response.text
soup = BeautifulSoup(web, "lxml")


title_movies = soup.find_all(name= "h3", class_ = "title")
print(title_movies)