import urllib2
import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen
import os
import predict

genres = ['Fantasy-Romance', 'Biography-Crime', 'Comedy', 'Crime', 'Thriller', 'Biography', 'Thriller', 'War', 'Adventure', 'Comedy', 'Family', 'Fantasy', 'Crime', 'Mystery', 'Sport', 'Action', 'Horror', 'Romance', 'Drama', 'Mystery', 'Romance', 'Biography', 'Comedy', 'Crime', 'History', 'Romance', 'Film-Noir', 'Musical', 'War', 'Adventure', 'Comedy', 'Fantasy', 'Romance', 'Adventure', 'Comedy', 'Drama', 'Romance', 'Crime', 'Mystery', 'Romance', 'Thriller', 'Adventure', 'Biography', 'Drama', 'War', 'Comedy', 'Drama', 'Sci-Fi', 'Biography', 'Documentary', 'Drama', 'Comedy', 'History', 'Romance', 'Adventure', 'Comedy', 'Thriller', 'Comedy', 'Crime', 'History', 'Thriller', 'Animation', 'Comedy', 'Family', 'Horror', 'Biography', 'Comedy', 'Documentary', 'Comedy', 'Crime', 'Horror', 'Mystery', 'Action', 'Biography', 'Comedy', 'Documentary', 'Action', 'Adventure', 'Comedy', 'Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sitcom', 'Sport', 'Thriller', 'War', 'Western', 'Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western', 'Anime']

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
def removeHtml(s):
	res = ""
	check = True
	for i in s:
		if check:
			if i == "<":
				check = False
			else:
				res = res+i
		else:
			if i ==">":
				check = True
	return res.strip()
def sumUP(arr):
	sumA = 0
	for i in arr:
		try:
			sumA = sumA + int(i)
		except:
			pass
	return sumA

def deleteDuplicates(lis):
	newLis=[]
	for item in lis:
		if item not in newLis:
			newLis.append(item)
	return newLis
def turnToSearch(name):
	name = name.strip()
	name = name.replace(" ","+")
	url = "http://www.imdb.com/find?ref_=nv_sr_fn&q="+name+"&s=all"
	return url
def getMLFromName(name):
	return getInfoForMovieML(getImdbLink(name))
#gets imdb link of actual movie
def getImdbLink(name):
	try:
		url = turnToSearch(name)
		arr=[]
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		for link in soup.findAll('td', class_="result_text"):
			s = str(link)
			if "(TV Episode)" not in s:
				begin = s.find("href=")
				if begin == -1:
					return
				end = s.find(">",begin)

				return "http://www.imdb.com"+s[begin+6:end-1]


	except:
		print "Error at: "+str(url)
def getInfoForMovieML(link):
	source_code=requests.get(link)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text)
	return getInfoForMLviaLinkSignUp(soup)
def getInfoForMLviaLinkSignUp(soup):
	info = []
	rating = 7
	for link in soup.findAll('div', class_="ratingValue"):
			rating = float(removeHtml(str(link))[:-3])
			break
	metaRating = int(rating*10)
	for link in soup.findAll('div', class_="metacriticScore score_favorable titleReviewBarSubItem"):
			metaRating = float(removeHtml(str(link)))
	info.append(rating)
	info.append(metaRating)
	gen = []
	for link in soup.findAll('div', class_="see-more inline canwrap"):
			gen = removeHtml(str(link)).replace("\xc2\xa0","").replace("\n","").replace("Genres:","").split("|")
	gens = []
	for i in gen:
		gens.append(i.strip())
	##print gens
	info.append(gens)
	awards = 0
	for link in soup.findAll('span', itemprop="awards"):
		awards = awards + sumUP(removeHtml(str(link)).replace("\n","").split(" "))
	##print awards
	info.append(awards)
	lengthMovie = 0
	for link in soup.findAll('time',itemprop="duration"):
		t=removeHtml(link)
		lengthMovie = t[:t.find("m")]
	info.append(int(lengthMovie))
	
	return info
def getRelatedFromName(name):
	link = getImdbLink(name)
	source_code=requests.get(link)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text)
	return getRelatedFromSoup(soup)
def getRelatedFromSoup(soup):
	recs = []
	for link in soup.findAll('div', class_="rec-title"):
		s = str(link)
		a = []
		begin = s.find("href")+6
		end = s.find('"',begin)
		href = s[begin:end]
		#print href
		begin = end
		title = s[begin+5:s.find("</b>")]
		if isEnglish(title):
			#print title
			recs.append(title)
	return recs

#array = getMLFromName("Kill Bill vol 2")
#print array
#print translateToML(array)

















