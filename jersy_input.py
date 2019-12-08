roster = {}
# roster is name of dict

for i in range(1, 6):
    # {}\'s to get ' to print literally, \n for newline i for variables in range 1, 6 which is 1,2,3,4,5
    player_jersey = int(input('Enter player {}\'s jersey number:\n'.format(i)))
    player_rating = int(input('Enter player {}\'s rating:\n'.format(i)))
    print()
    # if the jersey is les than 0, greater than 99, or rating less than 0 or greater than 9=invalid
    if player_jersey < 0 or player_jersey > 99:
        print('invalid entry')
    if player_rating < 0 or player_rating > 9:
        print('invalid entry')
        # sets player jersey as key in dictionary with player rating attached to it
    else:
        roster[player_jersey] = player_rating
print('ROSTER')
sorted_roster = sorted(roster)
for player_jersey in sorted_roster:
    print('jersey number: {0}, rating: {1}'.format(player_jersey, roster[player_jersey]))
print(roster)
print(sorted_roster)