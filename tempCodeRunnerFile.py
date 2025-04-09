# Removed unused import of random
import autumnsongs
import time
# Assuming playlist is a module with a function randcurplaylist
# If not, implement a mock function for demonstration
try:
    import playlist
    randomplaylist = playlist.randcurplaylist()
except ImportError:
    print("Error: 'playlist' module not found. Using a mock playlist.")
    randomplaylist = ["Song 1", "Song 2", "Song 3"]  # Mock playlist
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
    print(randomplaylist)
