from random import randint
print("Pick a number from 1 to 100!\n\nMake sure to stay within range,\nor else...\n")
num = randint(1, 100)
guessed = []
while True:
    guess = int(input("Guess the number: "))
    guessed.append(guess)
    player_turn = len(guessed)
    if 1 <= guess <= 100:
        if guess == num:
            input(f"\nThat's it!\nYou guessed it in {player_turn} turn(s)!"
                  f"\n\nYour guesses were: {guessed}\nPress ENTER to exit.")
            break
        if player_turn == 1:
            if abs(num - guess) <= 10:
                print("Warm!")
            else:
                print("Cold!")
        else:
            prev_guess = guessed[-2]
            if abs(num - prev_guess) > abs(num - guess):
                print("Warmer!")
            else:
                print("Colder!")
    else:
        print("Your number is out of bounds.")
