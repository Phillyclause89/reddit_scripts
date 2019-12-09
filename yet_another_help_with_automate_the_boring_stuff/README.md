# r/learnpython Adventure Summary
  TEXT

## File Overview:
  File | SIZE | BRIEF
--- | --- | ---
README.md | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/yet_another_help_with_automate_the_boring_stuff/README.md?style=plastic) | README.md file for this adventure.
requirements.txt | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/yet_another_help_with_automate_the_boring_stuff/requirements.txt?style=plastic) | requirements.txt for this adventure.
Comma_Code.py | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/yet_another_help_with_automate_the_boring_stuff/Comma_Code.py?style=plastic) | All the functions proposed by people commenting in the post.
  
## Source Link:
  * [ r/learnpython/.../yet_another_help_with_automate_the_boring_stuff ]( https://www.reddit.com/r/learnpython/comments/d2ikcl/yet_another_help_with_automate_the_boring_stuff/ )
  
## Post Title:
  > Yet another help with Automate the Boring Stuff Chapter 4 (Comma Code)
  
## Post Body:
  > Hi, I've searched through this subreddit for a solution with the Comma Code challenge in Automate the Boring Stuff and didn't find anyone solving like I did. I really don't think my code is efficient in any matter, but it gets the job done.
  > 
  > Could you please point in which direction I should improve it to be more efficient?
  > 
  > > Comma Code
  > >
  > > Say you have a list value like this:
  > > 
  > > spam = ['apples', 'bananas', 'tofu', 'cats']
  > > 
  > > Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.
  > 
  > My code (I've decided to remove the Oxford Comma):
  > ```python
  > def comma_and(spam):
  > for i in range(len(spam)):
  > if i < len(spam)-2:
  > print(spam[i] + ', ', end='')
  > elif i < len(spam)-1:
  > print(spam[i] + ' ', end='')
  > else:
  > print('and ' + spam[i] + '.')
  > 
  > spam = ['apples', 'bananas', 'tofu', 'cats']
  > comma_and(spam)
  > ```

### My Comment(s):
  > Assign len(spam) to a variable so you’re not calling it multiple times. Also I would construct the string in the loop so you only have to print once
#### OP's Reply:
  > Nice touch about the len(spam) becoming a variable. To construct the string in the loop should I set an empty string and manipulate it through methods? I can't understand how to do it...
#### My Reply:
  > ```python
  > def comma_and(spam):
  >     n,  s = len(spam) - 1, ""
  >     for i in range(n):
  >         if i == n - 1:
  >             s += "{} and {}.".format(spam[i], spam[i+1])
  >         else:
  >             s += "{}, ".format(spam[i])
  >     return s
  > ```
  > I would have wrote the function like this. I’m sure there are shorter more pythonic ways of writing the function, maybe even down to a one liner, but I can actually visualize what it’s doing this way. Also one thing that slipped by me the first time I read your post, is the problem statement ask you to return the solution, not print it. To print what your function returns just nest the function call in the print(). (Edits because whitespace is a bitch to get right on mobile)
  > 
#### OP's Reply:
  > As u/o5a have commented, there is indeed an one liner for it, using only join() and slices:
  > `def comma_and(spam):`
  > `return ', '.join(spam[:-1]) + ' and ' + spam[-1]`
  > 
  > Thank you very much for your example, it's really easy to follow and used only stuff already covered in the book, including string adding to itself, which I totally forgot. I haven't thought about using only one condition in the n-1 loop by using the i+1, nice solution.

#### My Reply:
  > I haven’t tested to confirm, but I think .join() requires the data all ready be in string data type. If you know your list is only ever going to be strings then o5a’s solution is likely the best as I believe it will execute faster. If you need it to work on lists with other data types then mine maybe better since .format() will take care of the data type conversion .
