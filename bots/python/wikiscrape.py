import urllib2
from BeautifulSoup import BeautifulSoup
import re
import time
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

url = ('https://en.wikipedia.org/wiki/List_of_American_comedy_films')

ourUrl = opener.open(url).read()

soup = BeautifulSoup(ourUrl)

for link in soup.findAll('a', attrs={'href': re.compile("^/wiki/")}):
	find = re.compile('/wiki/(.*?)"')
	searchMovie = re.search(find, str(link))
	movie = searchMovie.group(1)
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	url = ('https://en.wikipedia.org/wiki/' + movie)
	ourUrl = opener.open(url).read()
	soup = BeautifulSoup(ourUrl)
	try:
		outfile = open('/home/tito/movies/' + str(link.text) + '.txt','a')
		outfile.write(str(soup.title) + '\n')
	except:
		print "this movie could not be written >>> " + str(link.text)
	
	#outfile.write('')
