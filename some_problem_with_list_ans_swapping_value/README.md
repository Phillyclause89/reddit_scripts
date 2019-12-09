# r/learnpython Adventure Summary
  TEXT

## File Overview:
  File | SIZE | BRIEF
--- | --- | ---
README.md | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/some_problem_with_list_ans_swapping_value/README.md?style=plastic) | README.md file for this adventure.
requirements.txt | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/some_problem_with_list_ans_swapping_value/requirements.txt?style=plastic) | requirements.txt for this adventure.
Henrik.py| ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/some_problem_with_list_ans_swapping_value/Henrik.py?style=plastic) | code for this adventure.
  
## Source Link:
  * [ r/learnpython/.../some_problem_with_list_ans_swapping_value ]( https://www.reddit.com/r/learnpython/comments/e2nyut/some_problem_with_list_ans_swapping_value/ )
  
## Post Title:
  > Some problem with list ans swapping value
  
## Post Body:
  > So i got a list where the user gets to put as many numbers in as he wants, then i have created a variable for the smallest and biggest number in the list, going through a for in range (1, len(list)): where i have two if statements to determine the outcome of the variable. Now i want to swap places (highest and lowest number), but i just cant figure out how... Anybody care to help me a tiny bit? ^^ practicing for exams!
  > when i try to temp store one of the values while swapping the other i gete an error, "list index out of range"

### My Comment(s):
  > Best to include the code causing you trouble. Either in markdown code blocks or a link to a pastebin or git repo
#### OP Response:
  > I is all in Norwegian, soory bout that...
  >
  > #Uendelig liste Melli oppgave >:)
  > evig_liste = []
  > en_gang_til = "ja"
  > print("Skriv inn ønsket tall i listen: ")
  > while en_gang_til == "ja" or en_gang_til == "Ja":
  > legg_til = int(input("Skriv inn tallet du ønsker å legge til i listen: "))
  > evig_liste += [int(legg_til)]
  > en_gang_til = input("ønsker du å legge til flere tall i listen? :")
  >
  > print("listen din til nå: ", evig_liste)
  >
  > minste_tall=evig_liste[0]
  > hoyeste_tall=evig_liste[0]
  >
  > for i in range(1,len(evig_liste)):
  > if evig_liste[i] <= minste_tall:
  > minste_tall = evig_liste[i]
  > if evig_liste[i] >= hoyeste_tall:
  > hoyeste_tall = evig_liste[i]
  >
  > print("minste tallet i listen", minste_tall)
  > print("høyeste tallet i listen", hoyeste_tall)
  >
  > temp = [evig_liste[minste_tall]]
  > minste_tall = [evig_liste[hoyeste_tall]]
  > [evig_liste[hoyeste_tall]] = temp
  > temp = [evig_liste[hoyeste_tall]
  >
  > print(temp)
  > print("listen med byttet høyeste og laveste tall", evig_liste)
#### My Followup Response:
  > Oh snaps it’s foreign Python! Can you confirm your white space looks like this?
  >
  > ```python
  > evig_liste = []
  > en_gang_til = "ja" 
  > print("Skriv inn ønsket tall i listen: ")
  > 
  > while en_gang_til == "ja" or en_gang_til == "Ja":
  >     legg_til = int(input("Skriv inn tallet du ønsker å legge til i listen: "))
  >     evig_liste += [int(legg_til)]
  >     en_gang_til = input("ønsker du å legge til flere tall i listen? :")
  > 
  >     print("listen din til nå: ", evig_liste)
  >     minste_tall=evig_liste[0]
  >     hoyeste_tall=evig_liste[0]
  > 
  > 
  >     for i in range(1,len(evig_liste)):
  >         if evig_liste[i] <= minste_tall:
  >             minste_tall = evig_liste[i]
  >         if evig_liste[i] >= hoyeste_tall:
  >             hoyeste_tall = evig_liste[i]
  > 
  > print("minste tallet i listen", minste_tall)
  > print("høyeste tallet i listen", hoyeste_tall)
  > 
  > 
  > 
  > temp = [evig_liste[minste_tall]]
  > minste_tall = [evig_liste[hoyeste_tall]]
  > [evig_liste[hoyeste_tall]] = temp
  > temp = [evig_liste[hoyeste_tall]
  > 
  > print(temp)
  > print("listen med byttet høyeste og laveste tall", evig_liste)
  > 
  > ```
  > Or is it indented differently?
#### OP Follow-up response:
  > The for loop, print and variables minste, hoyeste is not not in the while loop xD, besides that all same
  > print("listen din til nå: ", evig_liste)
  > minste_tall=evig_liste[0]
  > hoyeste_tall=evig_liste[0]
  > for i in range(1,len(evig_liste)):
  > if evig_liste[i] <= minste_tall:
  > minste_tall = evig_liste[i]
  > if evig_liste[i] >= hoyeste_tall:
  > hoyeste_tall = evig_liste[i]
  > this is not in the while loop, onlt the three lines below the start of the loop
#### My summary comment to the post after talking to OP on discord:
  > Help Desk Summary:
  > 
  > I spent a good while on discord with OP and suggested these code changes to fix his bug and do the action of swapping the highest and lowest values in a list:
  > ```python
  > #Uendelig liste Melli oppgave >:)
  > # Infinite list Melli task> :)
  > 
  > # eternal list = []
  > evig_liste = []
  >  
  > # again = "yes"
  > en_gang_til = "ja"
  >    
  > # print ("Enter the desired number in the list:")
  > print("Skriv inn ønsket tall i listen: ")
  >   
  > # while again == "yes" or again == "Yes":
  >  
  > def validate_input(inpu):
  >     try:
  >         return int(inpu)
  >     except ValueError:
  >         return inpu
  >     
  > def adding_to_evig_liste(e_g_t):
  >     if e_g_t.lower() == "ja":
  >         return True
  >     return False
  >     
  >     
  > while adding_to_evig_liste(en_gang_til):
  >     # add = int (input ("Enter the number you want to add to the list:"))
  >     legg_til = validate_input(input("Skriv inn tallet du ønsker å legge til i listen: "))
  >   
  >     # eternal list + = [int (add)]
  >     evig_liste += [legg_til]
  >   
  >     # again = input ("Do you want to add more numbers to the list?:")
  >     en_gang_til = input("ønsker du å legge til flere tall i listen? :")
  >    
  >     # print ("your list so far:", forever list)
  >     print("listen din til nå: ", evig_liste)
  >    
  >     
  > # smallest number = everlasting list [0]
  > minste_tall_index=0
  > minste_tall=evig_liste[minste_tall_index]
  >     
  > # highest numbers = everlasting list [0]
  > hoyeste_tall_index = 0
  > hoyeste_tall=evig_liste[hoyeste_tall_index]
  >     
  >     
  >     
  > # for in in range (1, len (perpetual list)):
  > for i, n in enumerate(evig_liste):
  >     if n <= minste_tall:
  >         minste_tall_index = i
  >         minste_tall = n
  >     if n>= hoyeste_tall:
  >         hoyeste_tall_index = i
  >         hoyeste_tall = n
  >     
  >     
  >     
  > # print ("smallest number in list", smallest number)
  > print("minste tallet i listen", minste_tall)
  >     
  > # print ("smallest number in list", smallest number)
  > print("høyeste tallet i listen", hoyeste_tall)
  >     
  >     
  > temp = evig_liste[minste_tall_index]
  > temp2 = evig_liste[hoyeste_tall_index]
  > evig_liste[minste_tall_index] = temp2
  > evig_liste[hoyeste_tall_index] = temp
  >     
  > print(temp)
  >     
  > print("listen med byttet høyeste og laveste tall", evig_liste)
  > ```
  > Feel free to make any additional suggestions on how OP can make his code more pythonic.  like for example, I'm pretty sure they don't need that loop to find  `minste_tall`, `minste_tall_index`, `hoyeste_tall` and `hoyeste_tall_index`. I believe they can all be found with built in list methods, but I kept his loop in because I wanted to show OP the `enumerate()`.