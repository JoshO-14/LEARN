import random
import autumnsongs
import time


gc3 = autumnsongs.gc3
gc2 = autumnsongs.gc2
b2mr = autumnsongs.b2mr
others = autumnsongs.others
rc_playlist = autumnsongs.rc_playlist()

print("Welcome to the Autumar Wick Playlist Generator!")
print("\nThis program will take from all of Autumn's songs and create a playlist for you.\n")

playlistch = input("Do you want a random curated playlist(1) or manually selected(2): ")

if playlistch == "1":
    print("Selecting the best mix of Autumn's songs...")
    time.sleep(2)
    print("Done!")
    time.sleep(1)
    print("Here is your playlist:")
    time.sleep(2)
    for song in rc_playlist:
        print(song)
    


