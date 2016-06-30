# AUTHOR: MOHAMMAD M. GHASSEMI, MIT
# IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests
import string
from ast import literal_eval
from subprocess import call
import csv
import urllib2
import re

# Clear the screen
call(["clear"])

# Go to the website
url = 'http://www.ic.nc.gov/ncic/pages/70000.htm'


# Grab the HTML
#r = requests.get(url)
#r_html = r.text

r_html = urllib2.urlopen(url)

# Format the HTML using Beautiful Soup
soup = BeautifulSoup(r_html,"lxml")

# Grab the stories from h1s
cpt_costs = []
mydivs = soup.findAll('td')
stories = []
for hs in mydivs:
	try:
		cpt_costs.append(hs.font.string.encode("utf-8"))
	except:
		try:
			d_data = hs.font.span.string.encode("utf-8")
			d_data = re.sub("[^0-9a-zA-Z.]", '', d_data)
			cpt_costs.append(d_data)
		except:
			cpt_costs.append('')
cpt_costs = cpt_costs[11:]
cpt_costs = zip(*[iter(cpt_costs)]*4)

with open('radiology.csv','w') as out:
    csv_out=csv.writer(out)
    for row in cpt_costs:
        csv_out.writerow(row)



# Go to the website
url = 'http://www.ic.nc.gov/ncic/pages/00000a.htm'

# Grab the HTML
#r = requests.get(url)
#time.sleep(10)
#r = requests.get(url)
#r_html = r.text
r_html = urllib2.urlopen(url)

# Format the HTML using Beautiful Soup
soup = BeautifulSoup(r_html,"lxml")

# Grab the stories from h1s
cpt_costs = []
mydivs = soup.findAll('td')
stories = []
for hs in mydivs:
	try:
		cpt_costs.append(hs.font.string.encode("utf-8"))
	except:
		try:
			d_data = hs.font.span.string.encode("utf-8")
			d_data = re.sub("[^0-9a-zA-Z.]", '', d_data)
			cpt_costs.append(d_data)
		except:
			cpt_costs.append(' ')
cpt_costs = cpt_costs[11:]
cpt_costs = zip(*[iter(cpt_costs)]*7)

with open('surgery1.csv','w') as out:
    csv_out=csv.writer(out)
    for row in cpt_costs:
        csv_out.writerow(row)











# Go to the website
url = 'http://www.ic.nc.gov/ncic/pages/00000b.htm'

# Grab the HTML
#r = requests.get(url)
#time.sleep(10)
#r = requests.get(url)
#r_html = r.text
r_html = urllib2.urlopen(url)


# Format the HTML using Beautiful Soup
soup = BeautifulSoup(r_html,"lxml")

# Grab the stories from h1s
cpt_costs = []
mydivs = soup.findAll('td')
stories = []
for hs in mydivs:
	try:
		cpt_costs.append(hs.font.string.encode("utf-8"))
	except:
		try:
			d_data = hs.font.span.string.encode("utf-8")
			d_data = re.sub("[^0-9a-zA-Z.]", '', d_data)
			cpt_costs.append(d_data)
		except:
			cpt_costs.append(' ')
cpt_costs = cpt_costs[11:]
cpt_costs = zip(*[iter(cpt_costs)]*7)

with open('surgery2.csv','w') as out:
    csv_out=csv.writer(out)
    for row in cpt_costs:
        csv_out.writerow(row)












# Go to the website
url = 'http://www.ic.nc.gov/ncic/pages/00000c.htm'

# Grab the HTML
#r = requests.get(url)
#time.sleep(10)
#r = requests.get(url)
#r_html = r.text
r_html = urllib2.urlopen(url)


# Format the HTML using Beautiful Soup
soup = BeautifulSoup(r_html,"lxml")

# Grab the stories from h1s
cpt_costs = []
mydivs = soup.findAll('td')
stories = []
for hs in mydivs:
	try:
		cpt_costs.append(hs.font.string.encode("utf-8"))
	except:
		try:
			d_data = hs.font.span.string.encode("utf-8")
			d_data = re.sub("[^0-9a-zA-Z.]", '', d_data)
			cpt_costs.append(d_data)
		except:
			cpt_costs.append(' ')
cpt_costs = cpt_costs[11:]
cpt_costs = zip(*[iter(cpt_costs)]*7)

with open('surgery3.csv','w') as out:
    csv_out=csv.writer(out)
    for row in cpt_costs:
        csv_out.writerow(row)



# Go to the website
url = 'http://www.ic.nc.gov/ncic/pages/80000.htm'

# Grab the HTML
#r = requests.get(url)
#time.sleep(10)
#r = requests.get(url)
#r_html = r.text
r_html = urllib2.urlopen(url)


# Format the HTML using Beautiful Soup
soup = BeautifulSoup(r_html,"lxml")

# Grab the stories from h1s
cpt_costs = []
mydivs = soup.findAll('td')
stories = []
for hs in mydivs:
	try:
		cpt_costs.append(hs.font.string.encode("utf-8"))
	except:
		try:
			d_data = hs.font.span.string.encode("utf-8")
			d_data = re.sub("[^0-9a-zA-Z.]", '', d_data)
			cpt_costs.append(d_data)
		except:
			cpt_costs.append(' ')
cpt_costs = cpt_costs[11:]
cpt_costs = zip(*[iter(cpt_costs)]*6)

with open('pathology.csv','w') as out:
    csv_out=csv.writer(out)
    for row in cpt_costs:
        csv_out.writerow(row)




# Go to the website
url = 'http://www.ic.nc.gov/ncic/pages/90000.htm'

# Grab the HTML
#r = requests.get(url)
#r_html = r.text
r_html = urllib2.urlopen(url)


# Format the HTML using Beautiful Soup
soup = BeautifulSoup(r_html,"lxml")

# Grab the stories from h1s
cpt_costs = []
mydivs = soup.findAll('td')
stories = []
for hs in mydivs:
	try:
		cpt_costs.append(hs.font.string.encode("utf-8"))
	except:
		try:
			d_data = hs.font.span.string.encode("utf-8")
			d_data = re.sub("[^0-9a-zA-Z.]", '', d_data)
			cpt_costs.append(d_data)
		except:
			cpt_costs.append(' ')
cpt_costs = cpt_costs[11:]
cpt_costs = zip(*[iter(cpt_costs)]*7)

with open('eval_and_manage.csv','w') as out:
    csv_out=csv.writer(out)
    for row in cpt_costs:
        csv_out.writerow(row)













