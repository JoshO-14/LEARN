import autumnsongs
import time
import playlistfunctions

gc3 = autumnsongs.gc3
gc2 = autumnsongs.gc2
b2mr = autumnsongs.b2mr
others = autumnsongs.others



print("Welcome to the Autumar Wick Playlist Generator!")
print("\nThis program will take all of Autumn's songs and create a playlist for you based on your preference.\n")

menu = True
while menu:
    print("\nMenu:")
    print("1. Random curated playlist (Selecting this again will overwrite your previous playlist)")
    print("2. Manually selected playlist")
    print("3. Display your playlist")
    print("4. Display all songs")
    print("5. Exit")
    
    playlistch = input("Choose an option (1-5): ")
    
    if playlistch == "1":
        num_of_songs = int(input("How many songs do you want (max) in your playlist: "))
        print("Alright! Selecting the best mix of Autumn's songs...")
        time.sleep(2)
        print("Done!")
        time.sleep(1)
        print("Here is your playlist:")
        print("--------------------------------------------------")
        time.sleep(1)
        songs = playlistfunctions.randcurplaylist(num_of_songs)
        for song in songs:
            print(song)
            time.sleep(0.1)
            print("--------------------------------------------------")
    elif playlistch == "2":
        playlistfunctions.man_playlist()
        time.sleep(1)
    elif playlistch == "3":
        playlistfunctions.display_playlist()
        time.sleep(1)
    elif playlistch == "4":
        print("Here are all of Autumn's songs:")
        print("--------------------------------------------------")
        time.sleep(2)
        print("Golden Child 3:\n")
        for song in gc3:
            print(song)
            time.sleep(0.1)
        time.sleep(1)
        print("--------------------------------------------------")
        print("Golden Child 2:\n")
        for song in gc2:
            print(song)
            time.sleep(0.1)
        time.sleep(1)
        print("--------------------------------------------------")
        print("Back 2 My Roots:\n")
        for song in b2mr:
            print(song)
            time.sleep(0.1)
        time.sleep(1)
        print("--------------------------------------------------")
        print("Others:\n")
        for song in others:
            print(song)
            time.sleep(0.1)
        time.sleep(1)
        print("--------------------------------------------------")
        print("Done displaying all songs.")
    elif playlistch == "5":
        print("Exiting the program. Goodbye!")
        menu = False
    else:
        print("Invalid choice. Please select a valid option.")
