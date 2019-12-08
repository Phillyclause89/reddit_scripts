# r/learnpython Adventure Summary
  TEXT

## File Overview:
  File | SIZE | BRIEF
--- | --- | ---
README.md | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/looking_for_criticism_conways_game_of_life_in/README.md?style=plastic) | README.md file for this adventure.
requirements.txt | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/looking_for_criticism_conways_game_of_life_in/requirements.txt?style=plastic) | requirements.txt for this adventure.
  
## Source Link:
  * [ r/learnpython/.../looking_for_criticism_conways_game_of_life_in/ ]( https://www.reddit.com/r/learnpython/comments/e5ag24/looking_for_criticism_conways_game_of_life_in/ )
  
## Post Title:
  > Looking for criticism? Conway's Game of Life in Python
  
## Post Body:
  > I haven't programmed in a while and feel like I've totally lost whatever knack I had for it. I've been wanting to implement Conway's Game of Life for some time and thought that I'd ease my way back into programming with it. It's in pure Python. Thoughts? Please comment below! I know its not the most efficient way of going about it.
  > [Link](https://pastebin.com/x83euzwM)

### My Comment(s):
  > Your code appears to work and personally I think that's all that matters. So with that all I have to offer in [my more class based approach](https://pastebin.com/BLWiumKW) to your functional program.  Let me know if you have any questions about what I changed.
  >
  > To elaborate on what u/misho88 mentioned about docstrings:
  >
  > > You should put those long string comments inside the functions:  
  > > ```Python 
  > >`def f(): """function does something"""`  
  > > ```
  > >which makes them "docstrings" and you can access them with f.\_\_doc\_\_and help(f) in the interactive interpreter. For the same reason, that comment about this being Conway's game of life should go into a string near the top of the file, before the imports: it'll become your module's docstring that way.
  > 
  > If you do them right, you can also use tools like  [pdoc](https://pdoc3.github.io/pdoc/)  to auto generate some of the [documentation](https://pste.eu/p/djNY.html) for your code.
  #### OP Follow up Comment:
  > Interesting, and thank you! :) What advantage does a class-based approach offer in this case?
  #### My Response:
  > The topic of the pros and cons of [programming paradigms ](https://en.wikipedia.org/wiki/Comparison_of_programming_paradigms?wprov=sfti1) is highly debated and largely personal preference of the programmer. I thought using classes in this example would be fitting since your functions aren’t purely functional. Most are dependent on variables being initialized in the outer scope.   Programming this way isn’t really bad, so long as you are able too keep track of all your global references and are willing to except the fact that most of your functions are useless outside of the context your script. In one sense, your whole script is essentially being treated like a class. The only difference between my class and your script is that mine is a self contained object that can be imported and incorporated into other programs more easily.