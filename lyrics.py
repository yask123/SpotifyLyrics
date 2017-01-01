import requests
from bs4 import BeautifulSoup
import os
import urllib
def get_lyrics(song_name):

	try:
		song_name +=  ' metrolyrics'
		name =  urllib.quote_plus(song_name)

		url = 'http://www.google.com/search?q='+name

		result = requests.get(url, headers={'User-Agent' : "foobar"}).text
		link_start=result.find('http://www.metrolyrics.com')
		link_end=result.find('html',link_start+1)


		link = result[link_start:link_end+4]
		lyrics_html = requests.get(link, headers={'User-Agent' : "foobar"}).text
		soup = BeautifulSoup(lyrics_html, "lxml")
		raw_lyrics= (soup.findAll('p', attrs={'class' : 'verse'}))
		paras=[]
		final_lyrics=unicode.join(u'\n',map(unicode,raw_lyrics))

		final_lyrics= (final_lyrics.replace('<p class="verse">','\n'))
		final_lyrics= (final_lyrics.replace('<br/>',' '))
		final_lyrics = final_lyrics.replace('</p>',' ')
		return (final_lyrics)
	except:
		return 'Coundnt find lyrics for this song:( '
def get_current_song_playing():
	return os.popen('osascript current_song_name_as.AppleScript').read()


get_lyrics(get_current_song_playing())
