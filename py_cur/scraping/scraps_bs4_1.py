import requests
from bs4 import BeautifulSoup

r  = requests.get('https://www.yellowpages.in/search/hyderabad/coffee')

soupe = BeautifulSoup(r.content)
links =soupe.find_all("a")
for link in links :
	# print(link)
	# if 'http' in link.get('href'):
		# print("<a href=%s> %s</a>" %(link.get('href'),link.text))
	pass

g_data = soupe.find_all('div',{'class':'eachPopularTitleBlock'})
for items in g_data:
	# print(items.contents[3].text)#find_all('li',{'class':'eachPopularTagsList'})[0].text)
	print(items.contents[0].find_all('a',{'class':'eachPopularTagsList'}).text)