from rumps import *
from lyrics import *

class SpotifyLyrics(rumps.App):
    def __init__(self):
        super(SpotifyLyrics, self).__init__(type(self).__name__, menu=['Lyrics'])
        rumps.debug_mode(False)

    @clicked('Lyrics')
    def button(self, sender):
        sender.title = 'Lyrics'
        default_text= get_lyrics(get_current_song_playing())
        title = 'Spotify Lyrics \n ' + get_current_song_playing()
        Window(default_text, title=title, default_text='',  dimensions=(0,0)).run()

if __name__ == "__main__":
    SpotifyLyrics().run()
