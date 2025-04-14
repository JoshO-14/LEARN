import autumnsongs
import random


# Function to generate a random curated playlist


playlist = []

def randcurplaylist(num_of_songs):
    all_songs = autumnsongs.gc3 + autumnsongs.gc2 + autumnsongs.b2mr + autumnsongs.others
    random.shuffle(all_songs)
    global playlist
    playlist = all_songs[:num_of_songs]
    return playlist

# Function to generate a manually selected playlist

def man_playlist():
    selection = True
    while selection:
        print("\nSelect an album to add songs from:")
        print("1. Golden Child 3")
        print("2. Golden Child 2")
        print("3. Back 2 My Roots")
        print("4. Others")
        print("5. Done")
        
        album_select = input("Which album do you want to select from? (1-5): ")
        
        if album_select == "1":
            _add_songs_to_playlist("Golden Child 3", autumnsongs.gc3)
        elif album_select == "2":
            _add_songs_to_playlist("Golden Child 2", autumnsongs.gc2)
        elif album_select == "3":
            _add_songs_to_playlist("Back 2 My Roots", autumnsongs.b2mr)
        elif album_select == "4":
            _add_songs_to_playlist("Others", autumnsongs.others)
        elif album_select == "5":
            print("Done selecting songs.")
            selection = False
        else:
            print("Invalid selection. Please try again.")
    return playlist


def _add_songs_to_playlist(album_name, album_songs):
    print(f"\nHere are the songs from {album_name}:\n")
    for song in album_songs:
        print(song)
        print("--------------------------------------------------") 
    song_select = input("\nWhich song do you want to add to your playlist? Please type the full song name: ")
    if song_select in album_songs:
        playlist.append(song_select)
        print(f"\nAdded \"{song_select}\" to your playlist.")
    else:
        print("Song not found.")

def display_playlist():
    print("\nYour playlist:")
    for song in playlist:
        print(song)
        print("--------------------------------------------------")
    if not playlist:
        print("Your playlist is empty.")
