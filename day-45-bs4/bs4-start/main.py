from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tags = soup.select(".titleline a")
article_texts = []
article_links = []

for article_tag in article_tags:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvote_tags = soup.select(".score")
article_upvote_scores = [int(score.getText().split()[0]) for score in article_upvote_tags]

max_upvote = max(article_upvote_scores)
max_upvote_index = article_upvote_scores.index(max_upvote)

title = article_texts[max_upvote_index]
link = article_links[max_upvote_index]
upvote = article_upvote_scores[max_upvote_index]

print(title)
print(link)
print(upvote)



print(article_texts)
print(article_links)
print(article_upvote_scores)


# with open("website.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
#
# all_anchor_tags = soup.find_all(name="a")
#
# # for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# class_is_heading = soup.find_all(class_="heading")
# h3_heading = soup.find_all("h3", class_="heading")
# name = soup.select_one("#name")
# heading = soup.select(".heading")


