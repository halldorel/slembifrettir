from bs4 import BeautifulSoup
import requests
import re
import json

# dv.is

site_data = {'dv.is' : [], 'mbl.is' : []}

for subpage in range(1, 2):
	r = requests.get('http://www.dv.is/frettir/' + str(subpage))
	data = r.text
	soup = BeautifulSoup(data)
	soup = soup.find_all('section', 'generic_section')

	try:
		headlines = soup[0].find_all('h1')
		for hl in headlines:
			site_data['dv.is'].append(hl.get_text())
		print "Woohoo! - dv.is - " + str(subpage)
	except:
		print "Dammit! - dv.is - " + str(subpage)
		pass


r = requests.get('http://www.mbl.is/frettir/innlent/')
data = r.text
soup = BeautifulSoup(data)

# mbl.is

try:
	headlines = soup.find_all('h1')
	subheads = soup.find_all('ul', 'headlines')
	for s in subheads:
		headlines = headlines + s.find_all('li')
	
	for hl in headlines:
		site_data['mbl.is'].append(hl.get_text())
	print "Woohoo! - mbl.is"

except:
	print "Dammit! - mbl.is"
	pass

f = open('scrape_dump.txt', 'w')
f.write(json.dumps(site_data))
f.close()