from song import Song
def print_songs(song_list):
    for song in song_list:
        print(song) 
songs= [
    Song("butterflies", "Michael Jackson", 3.7),
    Song("dangerous", "Michael Jackson", 3.5)
]
print_songs(songs)