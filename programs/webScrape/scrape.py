# library to query a website
import urllib2

# import beautiful soup to parse data from website
from bs4 import BeautifulSoup

# specify url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

# query website and return the html to variable 'page'
# page is a "markup"
page = urllib2.urlopen(wiki)

# parge html in page; store as BS format
# lxml as parser
soup = BeautifulSoup(page, "lxml")

# print out structured HTML page
#print soup.prettify()

# print all the links on page; first find href tags
#allLinks = soup.find_all("a")
#for link in allLinks:
#	print link.get("href")

# find tables
allTables = soup.find_all('table')

# find specifi table
rightTable = soup.find('table', class_='wikitable sortable plainrowheaders')
print rightTable
