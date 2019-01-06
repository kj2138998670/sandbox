"""
Name: Wang Haonan
Date:06/01/19
Brief Project Description:
GitHub URL: https://github.com/JCUS-CP1404/a2--kj2138998670
"""
import pandas as pd
from kivy.app import App
from kivy.lang import Builder
from a2.songlist import SongList
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from a2.song import Song
# Create your main program in this file, using the SongsToLearnApp class


Songs = pd.read_csv('songs.csv',header=None)
songs_title=list(Songs[0])
singer_name=list(Songs[1])
year=list(Songs[2])
learned=list(Songs[3])


class SongsToLearnApp(App):



    test = StringProperty()  # Define status text
    tests = StringProperty()
    current_sort = StringProperty()  # Define song sorting
    sort_choices = ListProperty()

    def __init__(self, **kwargs):
        """Set sort"""
        super(SongsToLearnApp, self).__init__(**kwargs)
        self.song_list = SongList()
        self.sort_choices = ["title", "artist", "year"]# Sort options
        self.current_sort = self.sort_choices[0]
        self.song_list.read_songs()

    def build(self):
        """Loading GUI"""
        self.learn= "Songs to learn 2.0 by Hung"
        self.title = self.learn
        self.root = Builder.load_file('app2.kv')
        self.Judgement()
        return self.root

    def ChangeSort(self, sorting_choice):
        """Sort by option"""
        self.test = "song have been sorted by: {}".format(sorting_choice)
        self.song_list.sort(sorting_choice)
        self.root.ids.entriesBox.clear_widgets()
        self.Judgement()
        sort_index = self.sort_choices.index(sorting_choice)
        self.current_sort = self.sort_choices[sort_index]

    def Clear(self):
        """Setting Clear Button"""
        self.root.ids.song_title.text = ''
        self.root.ids.song_artist.text = ''
        self.root.ids.song_year.text = ''

    def Judgement(self):
        """Judgement song"""
        num_song = len(self.song_list.list_songs)
        learned_song = 0
        for song in self.song_list.list_songs:

            display_text = self.Display(song.title, song.artist,song.year, song.is_required)  # display what should be added to the widget

            if song.is_required == "n":

                learned_song += 1
                button_color = self.ChouseColor(song.is_required)
            else:
                button_color = self.ChouseColor(song.is_required)  # Distinguishing the colours of learning from those of not learning，and Display the number of songs


            temp_button = Button(text=str(display_text),id=str(song.title),background_color=button_color)  # Marking song
            temp_button.bind(on_release=self.press_entry)  # Display all kinds of information

            self.root.ids.entriesBox.add_widget(temp_button)
        self.test = "To learn: {}. Learned: {}".format(num_song - learned_song, learned_song)


    def Display(self,title,artist,year,is_required ):
        if is_required == "y":
            display_text = "{} by {} ({})".format(title,artist,year)
        else:
            display_text = "{} by {} ({}) (learned)".format(title,artist,year)

        return display_text

    def ChouseColor(self, learned):  # Set color
        if learned == "n":
            button_color = [0.5, 1, 0.2, 0.7]
        else:
            button_color = [1, 0.6, 0.4, 0.6]
        return button_color

    def press_entry(self, button):
        buttonText = button.text
        selectedSong = Song()
        for song in self.song_list.list_songs:


            songDisplayText = self.Display(song.title, song.artist, song.year, song.is_required)

            if buttonText == songDisplayText:
                selectedSong = song
                break

        selectedSong.mark_learned()
        self.root.ids.entriesBox.clear_widgets()
        self.Judgement()

        self.tests = "You have learned {}".format(selectedSong.title)

    def AddSongs(self):
        """Adding songs"""


        if self.root.ids.song_title.text == "" or self.root.ids.song_artist.text == "" or self.root.ids.song_year.text == "":
            self.root.ids.status2.text = "All fields must be completed"
            return
        try:

            song_title = str(self.root.ids.song_title.text)
            song_artist = str(self.root.ids.song_artist.text)
            song_year = int(self.root.ids.song_year.text)
            is_required = "y"


            self.song_list.add_to_list(song_title, song_artist, song_year, is_required)
            temp_button = Button(text=self.Display(song_title, song_artist, song_year, is_required))
            temp_button.bind(on_release=self.press_entry)


            temp_button.background_color = self.ChouseColor(is_required)
            self.root.ids.entriesBox.add_widget(temp_button)


            self.root.ids.song_title.text = ""
            self.root.ids.song_artist.text = ""
            self.root.ids.song_year.text = ""

        except ValueError:
            self.tests = "Please enter a valid year"

    def stop(self):
        self.song_list.save_songs()#Stop it



SongsToLearnApp().run()


