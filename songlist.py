# create your SongList class in this file #
from assn2.song import Song
from operator import attrgetter

class SongList:
    def __init__(self):
        self.list_songs = []

    def read_songs(self):
        # Read songs file #
        in_file = open("songs.csv","r")
        lines = in_file.readlines()
        for line in lines:
            song_item = line.split(',')
            song_item[3] = song_item[3].strip('\n')
            loaded_song = Song(song_item[0],song_item[1],song_item[2],song_item[3])
            self.list_songs.append(loaded_song)
        in_file.close()

    def sort(self, key):
        self.list_songs = sorted(self.list_songs, key=attrgetter(key, "title"))

    def add_to_list(self, title, artist, year, is_required):
        is_required="n"
        newSong = Song(title, artist, year,is_required)
        self.list_songs.append(newSong)


    def save_songs(self):#format
        csv_string = ""
        for each in self.list_songs:
            csv_string += "{},{},{},{}\n".format(each.title, each.artist, each.year, each.is_required)
        out_file = open("songs.csv", 'w')
        out_file.write(csv_string)
        out_file.close()



