# r/learnpython Adventure Summary
  TEXT

## File Overview:
  File | SIZE | BRIEF
--- | --- | ---
README.md | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/MD_Templates/README.md?style=plastic) | README.md file for this adventure.
requirements.txt | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/MD_Templates/requirements.txt?style=plastic) | requirements.txt for this adventure.
  
## Source Link:
  * [ r/learnpython/.../SOURCE_NAME ]( SOURCE_URL )
  
## Post Title:
  > On the subject of: Efficiency
  
## Post Body:
  > Hey guys,
  >
  > I've been learning Python, hence why I'm here, and I had a thought run through my mind. Today I made a very short game and simple text game using a single while loop and some if/elif statements. The game generates a random number between 1 and 100 and you try and guess it, it tells you if you're warmer/colder, etc...
  >
  > The Udemy course I'm following suggested to build the project on my own and compare it to the code they wrote.
  >
  > Now I'm assuming that the dude teaching the course knows quite a bit about the language (maybe that's just wishful thinking) but his code is only 19 lines and does the same thing as my 24 line game, just in a more compact way. My question is this:
  >
  > Do you learn more efficient ways of doing things by experience or by hearing it from others? Is there an advantage to shorter programs vs. long ones? Does it really matter, that 5 line difference?
  >
  > I'm sure this question is all over the place here and elsewhere, but I was just curious some more experienced answers. I'm far from expecting to write elegant code in a weeks worth of learning, but am curious whether or not I should be keeping that idea on the backburner while I'm practicing.
  >
  > Thank you for the hopefully eventual responses!
  > 
  > I put my code in the pastebin.
  > The "solution" the dude gave is in a Jupyter Notebook and so that would be a little bit difficult to pull out.
  >
  > My count was off because I added a few things just to try and learn some things on my own. Other than that it is fairly similar to my original.
  > https://pastebin.com/XRx7mKGc

## My Comment(s):
  > Here are a few things you could do to slim your line count down:
  > ```python
  > from random import randint
  > print("Pick a number from 1 to 100!\n\nMake sure to stay within range,\nor else...\n")
  > num = randint(1, 100)
  > guessed = []
  > while True:
  >     guess = int(input("Guess the number: "))
  >     guessed.append(guess)
  >     player_turn = len(guessed)
  >     if 1 <= guess <= 100:
  >         if guess == num:
  >             input(f"\nThat's it!\nYou guessed it in {player_turn} turn(s)!"
  >                   f"\n\nYour guesses were: {guessed}\nPress ENTER to exit.")
  >             break
  >         if player_turn == 1:
  >             if abs(num - guess) <= 10:
  >                 print("Warm!")
  >             else:
  >                 print("Cold!")
  >         else:
  >             prev_guess = guessed[-2]
  >             if abs(num - prev_guess) > abs(num - guess):
  >                 print("Warmer!")
  >             else:
  >                 print("Colder!")
  >     else:
  >         print("Your number is out of bounds.")
  > ```
  > First thing I noticed is when you initialized   `guessed = [0]` this results in `0` being displayed as a guess when you pass `guessed` into your endgame prompt. I would initialize it as an empty list `guessed = []` to avoid this.
  >
  > The next thing I noticed is you don't need to initialize  `player_turn = 0` outside your `while True` loop. This variable should always be `==` to the length `len()` of `guessed`. Thus we can just assign  `player_turn = len(guessed)` after we `.append` each `guess` to `guessed`.
  >
  > I personally think the first conditional looks nicer with two `<=`  instead of `<` and `<=` but that's just me.
  >
  > Inside of the first nested `if` conditional block you can just use a single call of `input()` here, insead of `print()` and `input()` . I also used `f"` stings here to make it more readable in code.
  >
  > Since you used `brake` in that first conditional, you don't need an else: condition following that break. Removing it saves you one level of indentation.
  >
  > You also don't need to do `elif abs(num-guess) >= 10:` . `else:` will work just fine there.
  >
  > Finally you can remove all your `continue`s
