import autumnsongs
import time
import playlist

gc3 = autumnsongs.gc3
gc2 = autumnsongs.gc2
b2mr = autumnsongs.b2mr
others = autumnsongs.others



print("Welcome to the Autumar Wick Playlist Generator!")
print("\nThis program will take from all of Autumn's songs and create a playlist for you.\n")

playlistch = input("Do you want a random curated playlist(1) or manually selected(2): ")
num_of_songs = int(input("How many songs do you want (max) in your playlist: "))


if playlistch == "1":
    print("Selecting the best mix of Autumn's songs...")
    time.sleep(2)
    print("Done!")
    time.sleep(1)
    print("Here is your playlist:")
    print("--------------------------------------------------")
    time.sleep(2)
    playlist.randcurplaylist()
if playlistch == "2":
    playlist.man_playlist()
    print("Done!")
    time.sleep(1)


