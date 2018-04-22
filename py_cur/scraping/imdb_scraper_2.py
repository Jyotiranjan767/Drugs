from bs4 import BeautifulSoup as bs
import requests as rq
import csv
import pandas as pd

url = 'https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = rq.get(url).text
soup  = bs(response, 'lxml')
content  =  soup.find_all('div', class_ = 'lister-item mode-advanced')
# for all_detail in all_details:	
# csv_file  = open("imdb_2.csv", 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['number','name', 'year', "pic", 'dnt', 'rat', 'desc','footer','v_g'])

names  = []
years = []
numbers = []
for i , con in enumerate(content):
	thundernail = con.find('div', class_= 'lister-item-image float-left').a.img['src']#__getattr__
	#for panda purpose , these list are created

	# print(thundernail)
	all_details = con.find("div",class_ = 'lister-item-content')
	header  = all_details.find_all("span")
	number  = header[0].text
	name = all_details.h3.a.text
	year = header[1].text
	names.append(name)
	years.append(year)
	numbers.append(number)
	# print(number, name, year)
	p = con.find_all("p")
	duration_and_type = p[0].text.split("|")
	dnt_ = []
	for du_an_ty in duration_and_type:
		d_n_t_all = du_an_ty.split('\n')
		d_n_t = ''.join(d_n_t_all).strip()
		dnt_.append(d_n_t)
	# print(dnt_)
	ratings_data = con.find("div", class_ = 'ratings-bar')
	ratin = ratings_data.text.strip()#split("     ")
	# print('\n')
	ratins = ratin.split('     ')
	rat_ = []
	for r in ratins:
		rat_.append(' '.join(r.split('\n')).strip())
	# print(rat_)
	description = p[1].text
	# print(description)
	footers = p[2].text
	foos = footers.split("|")
	fo_ = []
	for fo in foos:
		f = ''.join(fo.split('\n')).strip()
		fo_.append(f)
		# print(fo_)
	votes_gross = p[3].text.split('|')
	v_g_ = []
	for vg in votes_gross:
		v_g = ''.join(vg.split("\n")).strip()
		v_g_.append(v_g)
		# print(v_g_)

	# print(number, name, year)
	# print(thundernail)
	# print(' '.join(dnt_))
	# print(' '.join(rat_))
	# print(description)
	# print(', '.join(fo_))
	# print(' '.join(v_g_))
	# print('\n ====================================')
	# csv_writer.writerow([number, name, year, thundernail,' '.join(dnt_),
	# 	' '.join(rat_),description,', '.join(fo_),' '.join(v_g_)])
# csv_file.close()

# test_df = pd.DataFrame({'number':numbers,
# 						"movie":names,
# 						"year": years
# 					}, index = [0])

# print(test_df.info())
# print(numbers, names, years)

# test_df
