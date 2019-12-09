# r/learnpython Adventure Summary
  TEXT

## File Overview:
  File | SIZE | BRIEF
--- | --- | ---
README.md | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/second_user_input_doesnt_seem_to_be_saving_in_my/README.md?style=plastic) | README.md file for this adventure.
requirements.txt | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/second_user_input_doesnt_seem_to_be_saving_in_my/requirements.txt?style=plastic) | requirements.txt for this adventure.
jersy_input.py | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/second_user_input_doesnt_seem_to_be_saving_in_my/jersy_input.py?style=plastic) | code for this adventure.
  
## Source Link:
  * [ r/learnpython/.../second_user_input_doesnt_seem_to_be_saving_in_my ]( https://www.reddit.com/r/learnpython/comments/e4otmh/second_user_input_doesnt_seem_to_be_saving_in_my/ )
  
## Post Title:
  > Second user input doesn't seem to be saving in my dict
## Post Body:
  > So Im trying to get my program to past out 5 sets of 2 user inputs in order- I can do this (mostly) using the sorted built in function. And it works! For the first set of user inputs anyways, my output for the second user input is the last user input (as if it's not saving the second user input to my key-which is the first user input) I can't seem to find a fix for this.
  > [https://pastebin.com/uUGnBF9Q](https://pastebin.com/uUGnBF9Q)
  > So, if you run it, you'll see that for the output, it will print out the jersey numbers in order- hell yeah! BUT, it only prints out the last input value for player rating 5 times. Am I not making my key correctly with roster[player_jersey] = player_rating?
  

### My Comment(s):
  > Since `player_jersey` is the key for your `roster` dict, you can retrieve the value (`rating`) for that key using an assessor `[]`.  All you need to change is the print statement on the last line to this and you'll get the output you're looking for:
  > ```python
  > for player_jersey in sorted_roster:
  >     print('jersey number: {0}, rating: {1}'.format(player_jersey, roster[player_jersey]))
  > ```
#### OP Follow up Comment:
  > Your kidding? Shit man thanks
  