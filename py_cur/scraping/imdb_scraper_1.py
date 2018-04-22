from bs4 import BeautifulSoup as bs
import requests as rq
url = 'https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = rq.get(url).text

# print(response)
soup  = bs(response, 'lxml')
# print(soup.prettify())
content  =  soup.find('div', class_ = 'pagecontent')
header = content.find('div', class_ = 'article')
headline = header.h1.text
# print(soup.prettify())
sort_by = header.find('div', class_='sorting')
for j,i in enumerate(sort_by.text.strip().split('        ')):
	print(' ' .join(i.split('\n')))

lister_list = header.find("div", class_="lister-list")
movie_name = lister_list.div.h3.a.text
duration_and_type = lister_list.div.p.text.split('|')
for d_ in duration_and_type:
	print(''.join(d_.split('\n')).strip,end = ' ')
ratings_data = lister_list.find("div", class_ = 'ratings-bar')
ratin = ratings_data.text.strip()#split("     ")
print('\n')
ratins = ratin.split('     ')
for rat in ratins:
	print(' '.join(rat.split("\n")))
description_ = lister_list.find_all("p", class_ = 'text-muted')[1]
description = description_.text
print(description)

director_star__ = lister_list.find_all('p')[2]
director_star = director_star__.text.split("          ")
for dire_sta  in director_star:
	di_st = dire_sta.split('|')
	for d_s in di_st:
		print(''.join(d_s.split("\n")).strip())
footers  =  lister_list.find_all('p')[3].text.split('|')
for footer in footers:
	print(''.join(footer.split('\n')).strip())
