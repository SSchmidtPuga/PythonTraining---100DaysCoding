from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get(url= "https://news.ycombinator.com/")
web = response.text


soup = BeautifulSoup(web, "lxml")



Title_news = soup.find_all( class_ = "titlelink")
score_news = soup.find_all( class_ = "score")

print(Title_news)
# Link_news = soup.find_all(class_"a")


TITLE = []
LINKS = []
SCORES = []

for tag in Title_news:
    TITLE.append(tag.getText())
    LINKS.append(tag.get("href"))


BIGGEST_SCORE = 0
for tag in score_news:
    SCORES.append(int(tag.getText().split()[0]))


# for numbers in range(len(TITLE)-1):
#     print(TITLE[numbers])
#     print(LINKS[numbers])
#     print(SCORES[numbers])

BIGGEST_SCORE = 0
position = 0
for number in SCORES:
    if BIGGEST_SCORE < number:
        BIGGEST_SCORE = number



position = SCORES.index(BIGGEST_SCORE)
print(TITLE[position])
print(LINKS[position])
print(BIGGEST_SCORE)



# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "lxml")
#
# print(soup.title.string)
#
# all_anchor_tag = soup.find_all(name="a")
#
# for tag in all_anchor_tag:
#     print(tag.getText())

