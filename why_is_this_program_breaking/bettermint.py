# OP's second attempt https://pastebin.com/fWUe8KGA
name = input("Name: \n")
games_played = int(input("Games: \n"))
volleyball_times = 0
tennis_times = 0
badminton_times = 0
total_points = 0
volley_points = 0
tennis_points = 0
badminton_points = 0
volley = False
tennis = False
badminton = False
for g in range(games_played):
    game = input("Game Name: \n")
    points = int(input("Points: \n"))
    if game == 'volleyball':
        percent = points * 0.07
        points += percent
        volley_points += points
        volleyball_times += 1
    if game == 'tennis':
        percent = points * 0.05
        points += percent
        tennis_points += points
        tennis_times += 1
    if game == 'badminton':
        percent = points * 0.02
        points += percent
        badminton_points += points
        badminton_times += 1
    total_points += points
if volleyball_times > 0:
    if volley_points / volleyball_times > 75:
        volley = True
if tennis_times > 0:
    if tennis_points / tennis_times > 75:
        tennis = True
if badminton_times > 0:
    if badminton_points / badminton_times > 75:
        badminton = True
if volley and tennis and badminton:
    print(f'Congratulations, {name}! You won the cruise games with {int(total_points)} points.')
else:
    print(f'Sorry, {name}, you lost. Your points are only {int(total_points)}.')
