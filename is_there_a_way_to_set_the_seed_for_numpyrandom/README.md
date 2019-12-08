# r/learnpython Adventure Summary
  TEXT

## File Overview:
  File | SIZE | BRIEF
--- | --- | ---
README.md | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/is_there_a_way_to_set_the_seed_for_numpyrandom/README.md?style=plastic) | README.md file for this adventure.
requirements.txt | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/is_there_a_way_to_set_the_seed_for_numpyrandom/requirements.txt?style=plastic) | requirements.txt for this adventure.
randomness.py | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/is_there_a_way_to_set_the_seed_for_numpyrandom/randomness.py?style=plastic) | A script showing how RNG is controlled by the seed.
  
## Source Link:
  * [ r/learnpython/.../is_there_a_way_to_set_the_seed_for_numpyrandom ]( https://www.reddit.com/r/learnpython/comments/du4f22/is_there_a_way_to_set_the_seed_for_numpyrandom/ )
  
## Post Title:
  > Is there a way to set the seed for numpy.random for an entire script (aka not have to set it every time you call the RNG)?
  
## Post Body:
  > If there isn't that's fine, I just don't want to look like an idiot if I reset the RNG seed every time I call it (which is a lot in this application)
  > Thank you!

## My Comment(s):
  > [https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.seed.html](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.seed.html)
  > ```Python
  >  import numpy as np
  >  
  >  print("No Seed initialization:")
  >  for i in range(5):
  >      print("random roll:", np.random.randint(1, 7))
  >  
  >  print("Outer Seed initialization 69:")
  >  np.random.seed(69)
  >  for i in range(5):
  >      print("random roll:", np.random.randint(1, 7))
  >  
  >  print("Outer Seed initialization 666:")
  >  np.random.seed(666)
  >  for i in range(5):
  >      print("random roll:", np.random.randint(1, 7))
  >  
  >  print("Inner Seed init 69:")
  >  for i in range(5):
  >      np.random.seed(69)
  >      print("random roll:", np.random.randint(1, 7))
  >  
  >  print("Inner Seed init 666:")
  >  for i in range(5):
  >      np.random.seed(666)
  >      print("random roll:", np.random.randint(1, 7))
  > ```
  > prints:
  >
  > >No Seed initialization:  
  > >  
  > >random roll:  {Actually Random Number}  
  > >  
  > >random roll:  {Actually Random Number}  
  > >  
  > >random roll:  {Actually Random Number}  
  > >  
  > >random roll:  {Actually Random Number}  
  > >  
  > >random roll:  {Actually Random Number}  
  > >  
  > >Outer Seed initialization 69:  
  > >  
  > >random roll: 4  
  > >  
  > >random roll: 2  
  > >  
  > >random roll: 4  
  > >  
  > >random roll: 3  
  > >  
  > >random roll: 5  
  > >  
  > >Outer Seed initialization 666:  
  > >  
  > >random roll: 5  
  > >  
  > >random roll: 3  
  > >  
  > >random roll: 6  
  > >  
  > >random roll: 2  
  > >  
  > >random roll: 5  
  > >  
  > >Inner Seed init 69:  
  > >  
  > >random roll: 4  
  > >  
  > >random roll: 4  
  > >  
  > >random roll: 4  
  > >  
  > >random roll: 4  
  > >  
  > >random roll: 4  
  > >  
  > >Inner Seed init 666:  
  > >  
  > >random roll: 5  
  > >  
  > >random roll: 5  
  > >  
  > >random roll: 5  
  > >  
  > >random roll: 5  
  > >  
  > >random roll: 5
  >
  > Remember a game is always looping. You can do powerful things with random generators and seed values to load a specific states without heavy savefile overhead. it's how games like minecraft and No Man's Sky load huge worlds with little overhead. BUT you must be careful where you initialize your seed value in relation to your game loops. play around with this script i just wrote to show how seeds work inside and outside a loop.
  ### OP Follow up Comment:
  > Thanks for the response! Right, I guess my question is, is it possible to set the seed of the RNG once that so every time you call the RNG it uses that seed like is done in a inner seed init for loop? It seems like there is not
  #### My Response:
  > I'm confused my what you want here?  Can you show some code of how you want to use the seed?
  >
  > you can re-randomize the seed just by doing
  > ```Python
  > print("Inner Seed init 69:")
  > for i in range(5):
  >     if i != 4:
  >         np.random.seed(69)
  >     else:
  >         np.random.seed()
  >     print("random roll:", np.random.randint(1, 7))
  > ```
  >  
  > prints:
  >  
  > >Inner Seed init 69:  
  > >  
  > >random roll: 4  
  > >  
  > >random roll: 4  
  > >  
  > >random roll: 4  
  > >  
  > >random roll: 4  
  > >  
  > >random roll: {Actually Random Number}
  >
  > notice that with that code the first 4 rolls will always be `==` to `4` with seed reset to `69` each iteration of the loop, but on the last roll, calling `np.random.seed()` without an argument randomizes the seed and that roll will be truly random.
