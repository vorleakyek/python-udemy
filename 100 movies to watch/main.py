import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

title_tags = soup.find_all("h3", class_="title")
titles = [title.getText() for title in title_tags]
titles.reverse()
# print(titles)

with open("100-top-movies", "w") as file:
    for title in titles:
        file.write(title + "\n")


