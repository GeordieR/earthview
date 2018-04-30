import urllib2
import json
from bs4 import BeautifulSoup
result = []
file = open('output.json','a')
for x in xrange(1000, 7030): #You should able to run this in parallel, but I don't know how to do it
	x = str(x)
	try:
		print "Fetching" + x + " ..."
		response = urllib2.urlopen('https://earthview.withgoogle.com/' + x)
		html = response.read()
		html = BeautifulSoup(html, "html.parser")
		Region = str((html.find("div", class_="content__location__region")).text.encode('utf-8'))
		Country = str((html.find("div", class_="content__location__country")).text.encode('utf-8'))
		Copyright = str((html.find("div", class_="content__attribution__text")).text.encode('utf-8'))[2:]
		Everything = html.find("a", id="globe", href=True)
		GMapsURL = Everything['href']
		Image = 'https://www.gstatic.com/prettyearth/assets/full/' + x + '.jpg'
		result.append({'id': x, 'region': Region, 'country': Country, 'copyright': Copyright, 'map': GMapsURL, 'image': Image})
	
	except urllib2.HTTPError, e:
		continue #If the page is 404, then it will skip to the next one

meow = json.dumps(result) #because I love cat...
file.write(meow)			
file.close()
