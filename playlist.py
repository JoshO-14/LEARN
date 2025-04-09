import autumnsongs
import random
import creation

# Function to generate a random curated playlist

number_of_songs = creation.num_of_songs
playlist = []

def randcurplaylist():
    all_songs = autumnsongs.gc3 + autumnsongs.gc2 + autumnsongs.b2mr + autumnsongs.others
    random.shuffle(all_songs)
    playlist = all_songs[:number_of_songs]
    return playlist

# Function to generate a manually selected playlist

def man_playlist():
    selection = True
    while selection:
        album_select = input("Which album do you want to select from?")
        print("1. Golden Child 3")
        print("2. Golden Child 2")
        print("3. Back 2 My Roots")
        print("4. Others")
        print("5. Done")

        if album_select == "1":
            print("Here are the songs from Golden Child 3: \n")
            for i in autumnsongs.gc3:
                print(i)
            song_select = input("Which song do you want to add to your playlist?")
            if song_select in autumnsongs.gc3:
                playlist.append(song_select)
                print(f"Added {song_select} to your playlist.")
            else:
                print("Song not found.")
        elif album_select == "2":
            print("Here are the songs from Golden Child 2: \n")
            for i in autumnsongs.gc2:
                print(i)
            song_select = input("Which song do you want to add to your playlist?")
            if song_select in autumnsongs.gc2:
                playlist.append(song_select)
                print(f"Added {song_select} to your playlist.")
            else:
                print("Song not found.")
        elif album_select == "3":
            print("Here are the songs from Back 2 My Roots: \n")
            for i in autumnsongs.b2mr:
                print(i)
            song_select = input("Which song do you want to add to your playlist?")
            if song_select in autumnsongs.b2mr:
                playlist.append(song_select)
                print(f"Added {song_select} to your playlist.")
            else:
                print("Song not found.")
        elif album_select == "4":
            print("Here are the songs from Others: \n")
            for i in autumnsongs.others:
                print(i)
            song_select = input("Which song do you want to add to your playlist?")
            if song_select in autumnsongs.others:
                playlist.append(song_select)
                print(f"Added {song_select} to your playlist.")
            else:
                print("Song not found.")
        elif album_select == "5":
            print("Done selecting songs.")
            selection = False
        else:
            print("Invalid selection. Please try again.")
    return playlist
# Function to display the playlist