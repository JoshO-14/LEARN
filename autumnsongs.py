import random

gc3 = [
    "Laws of Power",
    "God\'s Child!",
    "All My Duffles Goyard",
    "Chelsea, NY",
    "Backseat!",
    "Toothache & Gaslighting!",
    "You > Them (Hate It!)"
    "Them > You (Gotta Go!)",
    "My Collection! 2",
    "No Good!",
    "Still the Same!",
    "Still the Same! 2",
    "If It Means Anything!",
    "If It Means Anything! 2",
    "Girl From the Club! 2",
    "50M Freestyle!",
    "Can't Rent Anymore!",
    "Twotimestwo!",
    "Colors!",
    "Baby Fewch!",
    "Recollections of Fame!",
    "I Am The Goat!",
    "The Remorse!"
]

gc2 = [
    "Golden Child 2 Intro!",
    "Inside My Head!",
    "Can We Talk!",
    "Golden Child!",
    "Jay N Bey!"
    "Should Know Me Better!",
    "Myself!"
]

b2mr = [
    "Replica!",
    "Brainrot!",
    "Passenger Princess!",
    "Sunburn!",
    "Something New!",
    "Laws of Power!",
    "Upper Echelon!",
    "Louis V Everything!",
    "One Way! 2",
    "Still the Same! 3",
    "Both Ways!",
    "Did It Again!",
    "Count It Faster!",
    "Free Promo!",
    "Stuck In A Loop!",
    "When I Pray!"
]

others = [
    "Not 3 Not 2!"
    "Comedy!",
    "Recollections of Loyalty and Pain!",
    "Girl From the Club!",
    "My Collection!",
    "One Way!",
    "TWO CHROME NECKLACES!",
    "Uptown Coolin!",
    "Average Night!",
    "Don't Come Around Interlude!",
    "Solitude!",
    "Now They Shocked!"
]


def rc_playlist():
    allsongs = gc3 + gc2 + b2mr + others
    random.shuffle(allsongs)
    playlist = allsongs[:10]
    return playlist