from bs4 import BeautifulSoup
import requests


response=requests.get("https://news.ycombinator.com/news")
yc_web_page=response.text
# print(yc_web_page)

soup= BeautifulSoup(yc_web_page,'html.parser')

print(soup.title)
head_line=soup.find(name='span',class_='titleline')
print(head_line.getText())

article_link= soup.select_one('.titleline a').get('href')
print(article_link)
# or
# article_link=head_line.get('href')
# print(article_link)

article_upvote= soup.select_one('span .score').getText()
print(article_upvote)

article_links=[]
article_texts=[]

all_anchour_tags=soup.select('.titleline a')
for tag in all_anchour_tags:
    article_texts.append(tag.getText())
    article_links.append(tag.get('href'))

article_upvotes=[ int(score.getText().split()[0]) for score in soup.select('span .score')]

print(f'{article_texts}\n{article_links}\n{article_upvotes}')


largest_number=max(article_upvotes)


largest_index=article_upvotes.index(largest_number)

print(f'{article_texts[largest_index]}\n{article_links[largest_index]}')








# with open('website.html', encoding="utf8") as file:
#     contents = file.read()
#     # holds the markups ,parser
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title.name)
#
# # to find all anchor tag
# all_anchour_tags= soup.find_all(name='a')
# print(all_anchour_tags)
#
# for tag in all_anchour_tags:
#     print(tag.getText())
#     print(tag.get('href'))
#
# heading = soup.find(name='h1', id='name')
# print(heading)
#
# section_heading= soup.find(name='h3',class_='heading')
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get('class'))
#
# soup.find_all('a')
#
#
# company_url = soup.select_one(selector='p a')
# print(company_url)
#
# name= soup.select_one(selector='#name')
# print(name)
#
# headings = soup.select(selector='.heading')
# print(headings)
