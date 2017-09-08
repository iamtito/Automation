"""
Author Name: Kabir Bolatito
"""
import urllib
import urllib.request
import time

from bs4 import BeautifulSoup

twitter = "https://twitter.com/"
tHandle = input('Please enter a twitter handle:')
url = twitter + tHandle
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser")
print ("------------------------------------------------")
time.sleep(2)
print('**Below are the recent tweets from',tHandle,'**')
print ("*************************************************")
print(soup.title.text)
print ("------------------------------------------------")
time.sleep(2)
#print(soup.findAll('a'))
"""
for eachLink in soup.findAll('a'):
	print(eachLink.get('href'))
	print(eachLink.text)
"""
print(soup.find('div',{"class":"ProfileHeaderCard"}).find('p').text)
print ("---------------THE POTUS TWEETS---------------------------------")
time.sleep(2)
i = 1
for tweets in soup.findAll('div', {"class":"content"}):
	#print(i)
	print(i,'-',tweets.find('p').text)
	
	time.sleep(2)
	#print(tweets.text)
	i = i+1
