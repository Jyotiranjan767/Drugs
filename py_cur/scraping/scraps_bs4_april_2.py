from bs4 import BeautifulSoup as bs
import requests as rq
import csv 

def corey():
	
	url = "http://coreyms.com/"
	content = rq.get(url).text
	soup = bs(content,'lxml') 
	# print(response.prettify())
	print(soup.title.text, end= '\n')

	# with open("cms_scrape.csv", 'w') as csv_file :
	csv_file = open('cms_scrape.csv', 'w')
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(['headline', 'summary', 'video_link'])
	articles = soup.find_all('article')
	for article in articles:
		header = article.find("header", class_ = 'entry-header')
		headline = header.a.text
		hint = header.p.text 	
		print(headline)
		print(hint, end = '\n')
		entry_content = article.find('div', class_ = 'entry-content')
		summary = entry_content.p.text
		print(summary)
		try:
			link = article.find('iframe', class_ = 'youtube-player')
			video_link  = link['src'].split('/')[4].split('?')[-2]
			yt_link = f'http://youtube.com/watch?v={video_link}'
		except Exception as e:
			yt_link = None
		print(yt_link)	
		footer = article.find('footer', class_ = 'entry-footer')
		print(footer.span.text, end = '\n\n')
		csv_writer.writerow([headline, summary, yt_link])
	csv_file.close()
corey()