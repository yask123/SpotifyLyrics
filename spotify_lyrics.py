from rumps import *
from utils import lyrics

class SpotifyLyrics(rumps.App):
    def __init__(self):
        super(SpotifyLyrics, self).__init__(type(self).__name__, menu=['Lyrics'])
        rumps.debug_mode(True)

    @clicked('Lyrics')
    def button(self, sender):
        sender.title = 'Lyrics'
        default_text= lyrics.get_lyrics(lyrics.get_current_song_playing())
        title = 'Spotify Lyrics \n ' + lyrics.get_current_song_playing()
        Window(default_text, title=title, default_text='',  dimensions=(0,0)).run()

print lyrics.get_lyrics(lyrics.get_current_song_playing())
if __name__ == "__main__":
    SpotifyLyrics().run()
