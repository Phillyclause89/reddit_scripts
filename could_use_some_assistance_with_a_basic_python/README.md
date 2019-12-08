# r/learnpython Helpdask Summary
## Source Link:
  * [r/learnpython/.../could_use_some_assistance_with_a_basic_python/](https://www.reddit.com/r/learnpython/comments/e4tg67/could_use_some_assistance_with_a_basic_python/)
## Post Title:
  Could use some assistance with a basic python program
## Post Body:
  > Edit: Solved, thank you everyone!
  > 
  > Hello, I'm looking for some help with a simple python program. This program is supposed to read each line from a text file (fake credit card numbers on each line) and determine if it is of valid length, and starts with a valid character. (For this program, a 2, 4, or 5). The program seems to run correctly and do what I want it to do, but it still comes up with an error. I have:
  > 
  > #Determining if a credit card is number is valid
  > try:
  > file1 = open("creditCards.txt","r")
  > except:
  > print("ERROR! Invalid File!")
  > else:
  > line = file1.readline()
  > while line:
  > cardNum=file1.readline()
  > cardNum=cardNum.rstrip()
  > if cardNum[0] == str(4) and len(cardNum) ==16:
  > print("This card is a Visa, #" + str(cardNum))
  > elif cardNum[0] == str(5) and len(cardNum) == 16:
  > print("This card is a Mastercard, #" + str(cardNum))
  > elif cardNum[0] == str(2) and len(cardNum) == 16:
  > print("This card is an American Express, #" + str(cardNum))
  > else:
  > print("Invalid Card.")
  > file.close()
  > 
  > When I run this, I get this error: Traceback (most recent call last):
  > 
  > File "C:/Users/lrems/OneDrive/Desktop/Python Work/creditCardValid.py", line 11, in <module>
  > if cardNum[0] == str(4) and len(cardNum) ==16:
  > IndexError: string index out of range
  > 
  > Can anyone point me in the direction to fix this?
  > 
  > Thank you!

## My Comment(s):
  > I'm assuming your code looks like this, which will get the error you noted. The way you pasted it in without white space would causes a different error.
  > 
  >   # Determining if a credit card is number is valid
  >   
  >   try:
  >   
  >       file1 = open("creditCards", "r")
  >   
  >   except:
  >   
  >       print("ERROR! Invalid File!")
  >   
  >   else:
  >   
  >       line = file1.readline()
  >   
  >       while line:
  >   
  >           cardNum = file1.readline()
  >   
  >           cardNum = cardNum.rstrip()
  >   
  >           if cardNum[0] == str(4) and len(cardNum) == 16:
  >   
  >               print("This card is a Visa, #" + str(cardNum))
  >   
  >           elif cardNum[0] == str(5) and len(cardNum) == 16:
  >   
  >               print("This card is a Mastercard, #" + str(cardNum))
  >   
  >           elif cardNum[0] == str(2) and len(cardNum) == 16:
  >   
  >               print("This card is an American Express, #" + str(cardNum))
  >   
  >           else:
  >   
  >               print("Invalid Card.")
  >   
  >   file.close()
  > 
  > my output on a test file with 10 invalid cards, (one on each line):
  > 
  >   Invalid Card.
  >   Invalid Card.
  >   Invalid Card.
  >   Invalid Card.
  >   Invalid Card.
  >   Invalid Card.
  >   Invalid Card.
  >   Invalid Card.
  >   Invalid Card.
  >   Traceback (most recent call last):
  >     File "C:/Users/Me/PycharmProjects/reddit_scripts/inplis.py", line 55, in <module>
  >       if cardNum[0] == str(4) and len(cardNum) == 16:
  >   IndexError: string index out of range
  >   
  >   Process finished with exit code 1
  > 
  > The first thing I'm noticing is that you are only validating from the second line on because you did `line = file1.readline()` before you enter your `while line` loop and you never actually validate the line assigned to `line` inside your loop, you just use it as the truth value for your loop.  The `<class '_io.TextIOWrapper'>` object you assigned to `file1` with `file1 = open("creditCards.txt", "r")` is now on the second line.  So when you do `cardNum = file1.readline()` on the first iteration of your loop, you are assigning the second line to that variable, not the first.  Its possible the file you are loading only has data from the second line on, but if there is a number on the first line that needs validating than you'll miss it, so I thought I would call that out.  Now your IndexError is occurring on the last line, because the `.readline()` will return an empty string when it gets to the end of the document, so when you do `cardNum[0]` to access the first index of the empty string that has zero indexes, you end up with your `IndexError` . One method of preventing this error is to check if `len(cardNum])` is greater than zero before you try to access the first character in the string. or better yet you could do your `len(cardNum) == 16` check first the do the other checks if that passes:
  > 
  >           if len(cardNum) == 16:
  >               if cardNum[0] == str(4):
  >                   print("This card is a Visa, #" + str(cardNum))
  >               elif cardNum[0] == str(5):
  >                   print("This card is a Mastercard, #" + str(cardNum))
  >               elif cardNum[0] == str(2):
  >                   print("This card is an American Express, #" + str(cardNum))
  >           else:
  >               print("Invalid Card.")
  > 
  > Doing this you'll notice that you no longer error out when you get an empty string returned from `file1.readline()`. You'll now get an indefinite loop because   `while line:` will continue to evaluate to `True` since you do nothing with `line` to make it not true. Honestly instead of trying to manage your while loop, I would just use the `.readlines()` method which will return all your lines in a list. You can then use a for loop to validate all the lines in that list.
