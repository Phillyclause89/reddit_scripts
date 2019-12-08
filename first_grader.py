import random
# import sound
# import dialogs

# spelling lists for each week
dicty = {'Nov 8': 'on mom job hop top mop as be by did move prove',
        'Nov 1': 'not hot pot got box fox are all am has boat float',
        'Oct 18': 'if big dig pig did him have here come little',
        'Oct 11': 'it bit sit is his in with like play said',
        'Oct 4': 'jet set met bed yes leg he she you look',
        'Sep 27': 'let get net pet pen men the we is can',
        'Sep 20': 'at am cat hat has and big add my to',
        'Sep 13': 'an can man ran dad had',
        'BONUS': 'alert insert charm alarm allow little pitch stitch catch batch boat float move prove'}

# pick a list to quiz
# choose = dialogs.list_dialog(title='Choose spelling list', items=list(dict.keys()), multiple=False)
choose = random.choice(['Nov 8','Nov 1','BONUS'])
pick = dicty[choose]

# get individual words
words = pick.split()
current = random.sample(words, len(words))

# loop through each word and evaluate the answer
for c in current:
    prompt = input('How do you spell ' + c + '?\n')
    if prompt == c:
        # sound.play_effect('game:Ding_3')
        print(c)
    else:
        # sound.play_effect('game:Crashing')
        print(c)

# ending sound and message
# sound.play_effect('arcade:Explosion_6')
print('All done!')
