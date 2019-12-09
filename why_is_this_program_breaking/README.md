# r/learnpython Adventure Summary
  TEXT

## File Overview:
  File | SIZE | BRIEF
--- | --- | ---
README.md | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/why_is_this_program_breaking/README.md?style=plastic) | README.md file for this adventure.
requirements.txt | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/why_is_this_program_breaking/requirements.txt?style=plastic) | requirements.txt for this adventure.
badmint.py | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/why_is_this_program_breaking/badmint.py?style=plastic) | OP's broken code.
bettermint.py | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/why_is_this_program_breaking/bettermint.py?style=plastic) | OP's improved code.
philmint.py | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/why_is_this_program_breaking/philmint.py?style=plastic) | My proposed changes to OP's code.
  
## Source Link:
  * [ r/learnpython/.../why_is_this_program_breaking ]( https://www.reddit.com/r/learnpython/comments/dqnptq/why_is_this_program_breaking/ )
  
## Post Title:
  > Why is this program breaking?
  
## Post Body:
  > Whenever I get to the 3rd input, it just skips it... you can see it with the debugger.. it is working with first two inputs but whenever its 'badminton' breaks....
  > 
  > https://pastebin.com/R9xcMF9n
  > 
  > 
  > 
  > name = input()games_played = int(input())winner = Falsevolley_points = 0tennis_points = 0badminton_points = 0volley_times = 0tennis_times = 0badminton_times = 0total_points = 0for g in range(1, games_played + 1):game_name = input()points = int(input())
  > 
  > if game_name == 'volleyball':volley_points += int((points + (points * 0.07)))volley_times += 1total_points += int((points + (points * 0.07)))elif game_name == 'badminton':tennis_times += 1badminton_points += int((points + (points * 0.02)))total_points += int((points + (points * 0.07)))elif game_name == 'tennis':tennis_times += 1tennis_points += int((points + (points * 0.05)))total_points += int((points + (points * 0.07)))
  > 
  > if (volley_points / volley_times) > 75 and (tennis_points / volley_points) > 75 and (badminton_points / badminton_times) > 75:winner = Trueif winner:print(f'Congratulations, {name}! You won the cruise games with {tennis_points} points.')else:print(f'Sorry, {name}, you lost. Your points are only {total_points}.')
  > 
### My Comment(s):
  > I added in some prompt text for your inputs, but let's walk through this:
  > ```python
  > name = input("What is your Name?\n")
  > games_played = int(input("How many games do you want to play?\n"))
  > winner = False
  > volley_points = 0
  > tennis_points = 0
  > badminton_points = 0
  > volley_times = 0
  > tennis_times = 0
  > badminton_times = 0
  > total_points = 0
  > 
  > ```
  >
  > You set a lot of variables to zero here.  This is fine until you decide to divide something by one of these and it still happens to be equal to zero.  Otherwise you going to end up with an error that looks similar like this:
  > 
  >   > Traceback (most recent call last):
  >   >   File "C:/reddit_scripts/badmint.py", line 28, in <module>
  >   >     if (volley_points / volley_times) > 75 and (tennis_points / volley_points) > 75 and (
  >   > ZeroDivisionError: division by zero
  > 
  > Another thing I notice is that you take naked user input with the `input()` function.  I'm calling it naked because you have no logic in place to validate if the user input will work with the functions you call on them. I can break your script on line 2 just by entering a non numeric character because of the `int(input())`.  (And I can break it later via a `ZeroDivisionError:` should I enter 0.) See the [Prompts class](https://github.com/Phillyclause89/risk.py/blob/288fd3f19a10d698b1a2181b99433ad65f9268ae/risk_2.py#L249) in my risk game on github for an example of how to dress up naked user inputs.
  > 
  > \-----------------------------------------------------------------------------------------
  > ```python
  > for g in range(1, games_played + 1):
  >     game_name = input("What game would you like to play? choices: volleyball | badminton | tennis \n")
  >     points = int(input("Points?"))
  >     if game_name == 'volleyball':
  >         volley_points += int((points + (points * 0.07)))
  >         volley_times += 1
  >         total_points += int((points + (points * 0.07)))
  >     elif game_name == 'badminton':
  >         tennis_times += 1
  >         badminton_points += int((points + (points * 0.02)))
  >         total_points += int((points + (points * 0.07)))
  >     elif game_name == 'tennis':
  >         tennis_times += 1
  >         tennis_points += int((points + (points * 0.05)))
  >         total_points += int((points + (points * 0.07)))
  > 
  > ```
  > 
  > The next thing your script does is initiate a `for` loop defined by the user input assigned to the `games_played` variable.  The probability of hitting a `ZeroDivisionError` later in the script is dependent on what number the user assigned to `games_played` . If the user enters `0` the loop wont run at all and you'll jump to the next block and all the variables initialized to `0` in the first block will be passed into this block:
  > ```python
  > if (volley_points / volley_times) > 75 and (tennis_points / volley_points) > 75 and (
  >         badminton_points / badminton_times) > 75:
  >     winner = True
  > 
  > ```
  > 
  > In this block you use `volley_times`, `volley_points` and `badminton_times` as  a **divisor** . If any of those variables are still assigned to zero by the time the script reaches this line, s\*\*\* gunna break.  To your credit you try to change these variables in the preceding `for` loop but in order to do so, the lines with
  > 
  > `volley_times += 1`, `volley_points += int((points + (points * 0.07)))` and s\*\*\* i just realized you don't do anything with `badminton_times` so the probability of `ZeroDivisionError` just jumped to 100%. You probably want to reevaluate your logic here and try to make a program flow that has zero probability of `ZeroDivisionError` by the time it gets to the second to last code block.
  > 
#### OP's Reply:
  > Thank you so much for your review!!! This really helped me understand some core things. I will update the code and will post it again. Thank you brother!!!
  > https://pastebin.com/fWUe8KGA
  > 
  > This is my new code. It's enough to give me 100 points for the task. This are the inputs they are checking with and the expected output:https://pastebin.com/haLVGy48
  > 
  > 
  > 
  > And again thank you for your response! It was really helpful!
#### My Reply:
  > Congrats on solving your issue! One last thing I would recommend is start learning about dictionaries.  You're writing a lot of the same code twice in your script just to change a few things for each game. This habit can lead you down a path of horrible copypasta bugs (I'm guilty of plenty myself.)  If you keep all the different variables for each game in a dictionary, you can then write one loop that does the same thing on all the games in the dict. Below is an example of a script that does exactly what  the one you just shared with me does, but in 40% less lines:
  > ```python
  > name = input("Name: \n")
  > games_played = int(input("Games: \n"))
  > games = {0: dict(name="volleyball", times=0, points=0, multiplier=0.07),
  >          1: dict(name="tennis", times=0, points=0, multiplier=0.05),
  >          2: dict(name="badminton", times=0, points=0, multiplier=0.02)}
  > total_points = 0
  > winner = True
  > for g in range(games_played):
  >     game = input("Game Name: \n")
  >     points = int(input("Points: \n"))
  >     for i in games:
  >         if games[i]["name"] == game:
  >             percent = points * games[i]["multiplier"]
  >             points += percent
  >             games[i]["points"] += points
  >             games[i]["times"] += 1
  >             break
  >     total_points += points
  > for i in games:
  >     if games[i]["times"] < 1 or (games[i]["points"] / games[i]["times"]) <= 75:
  >         winner = False
  >         break
  > if winner:
  >     print(f'Congratulations, {name}! You won the cruise games with {int(total_points)} points.')
  > else:
  >     print(f'Sorry, {name}, you lost. Your points are only {int(total_points)}.')
  > 
  > ```
  > Getting in the habit of writing scripts like this will save you a lot of work in the long run. Say you wanted to add a fourth game `"pickleball"`. In your version of the script, you would have to copy, paste and modify code throughout the whole file in order to add that in.  In my version, you would just add it to the dictionary `games` at the top of the script like so:
  > ```python
  > games = {
  >     0: dict(name="volleyball", times=0, points=0, multiplier=0.07),
  >     1: dict(name="tennis", times=0, points=0, multiplier=0.05),
  >     2: dict(name="badminton", times=0, points=0, multiplier=0.02),
  >     3: dict(name="pickleball", times=0, points=0, multiplier=0.0001)}
  > ```
  > then the rest of the code would just magically work with it.
#### OP's Reply:
  > Wow man, this is so helpful!!! THANK YOU!!! It is really a step I need and I just started reading about dictionaries last night. Your rewriting on my code is the best example I can ever get!!! So appreciated !!!
#### My Reply (Using My Alt Reddit Handle):
  > Same dude here, just using my SFW account ATM. Another cool thing about dictionaries is that you can nest other data structures inside them. Say you wanted to make your script more user friendly, by increasing the possible inputs a user can make to select a game. Instead of doing a giant chain of or conditions like this,
  > ```python
  > if game == "tennis" or game == "0" or game == "t":
  >     ...
  > ```
  > we could just have the "name" key in the games dict point to an array of strings that represent possible names of the game:
  > ```python
  > games = {0: dict(name=["0", "volleyball", "v"], times=0, points=0, multiplier=0.07),
  >          1: dict(name=["1", "tennis", "t"], times=0, points=0, multiplier=0.05),
  >          2: dict(name=["2", "badminton", "b"], times=0, points=0, multiplier=0.02)}
  > ```
  > We can also run .lower() on the user's input to ensure that if the user happened to enter any upper case letters, those letters are converted to lower case before trying to validate.
  > ```python
  > game = input("Game Name: \n").lower()
  > ```
  > Now we can validate the user's input across many possible names for a game using the in keyword:
  > ```python
  > for i in games:
  >     if game in games[i]["name"]:
  >         ...
  > ```