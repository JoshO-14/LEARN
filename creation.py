cash = int(input("Enter your specified amount of cash: "))


if cash < 2:
    print("You broke ah boi")
elif cash == 2:
    print("You shall pass ah mf")
elif cash > 2:
    print(f"Overpaid loser, Here is your change of {cash-2}")
else:
    print("Whats wrong w u bru")