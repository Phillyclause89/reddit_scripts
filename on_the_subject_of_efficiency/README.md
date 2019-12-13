# r/learnpython Adventure Summary
  [http://pythontutor.com/visualize](http://pythontutor.com/visualize.html#code=from%20random%20import%20randint%0Aprint%28%22Pick%20a%20number%20from%201%20to%20100!%5Cn%5CnMake%20sure%20to%20stay%20within%20range,%5Cnor%20else...%5Cn%22%29%0Anum%20%3D%20randint%281,%20100%29%0Aguessed%20%3D%20%5B%5D%0Awhile%20True%3A%0A%20%20%20%20guess%20%3D%20int%28input%28%22Guess%20the%20number%3A%20%22%29%29%0A%20%20%20%20guessed.append%28guess%29%0A%20%20%20%20player_turn%20%3D%20len%28guessed%29%0A%20%20%20%20if%201%20%3C%3D%20guess%20%3C%3D%20100%3A%0A%20%20%20%20%20%20%20%20if%20guess%20%3D%3D%20num%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20input%28f%22%5CnThat's%20it!%5CnYou%20guessed%20it%20in%20%7Bplayer_turn%7D%20turn%28s%29!%22%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20f%22%5Cn%5CnYour%20guesses%20were%3A%20%7Bguessed%7D%5CnPress%20ENTER%20to%20exit.%22%29%0A%20%20%20%20%20%20%20%20%20%20%20%20break%0A%20%20%20%20%20%20%20%20if%20player_turn%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20abs%28num%20-%20guess%29%20%3C%3D%2010%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Warm!%22%29%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Cold!%22%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20prev_guess%20%3D%20guessed%5B-2%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20abs%28num%20-%20prev_guess%29%20%3E%20abs%28num%20-%20guess%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Warmer!%22%29%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Colder!%22%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28%22Your%20number%20is%20out%20of%20bounds.%22%29&cumulative=true&curInstr=5&heapPrimitives=true&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## File Overview:
  File | SIZE | BRIEF
--- | --- | ---
README.md | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/on_the_subject_of_efficiency/README.md?style=plastic) | README.md file for this adventure.
requirements.txt | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/on_the_subject_of_efficiency/requirements.txt?style=plastic) | requirements.txt for this adventure.
nguess.py | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/on_the_subject_of_efficiency/nguess.py?style=plastic) | code for this adventure.
  
## Source Link:
  * [ r/learnpython/.../on_the_subject_of_efficiency ]( https://www.reddit.com/r/learnpython/comments/dtpn9x/on_the_subject_of_efficiency/ )
  
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

### My Comment(s):
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
