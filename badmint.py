name = input("What is your Name?\n")
games_played = int(input("How many games do you want to play?\n"))
winner = False
volley_points = 0
tennis_points = 0
badminton_points = 0
volley_times = 0
tennis_times = 0
badminton_times = 0
total_points = 0
for g in range(1, games_played + 1):
    game_name = input("What game would you like to play? choices: volleyball | badminton | tennis \n")
    points = int(input("Points?"))

    if game_name == 'volleyball':
        volley_points += int((points + (points * 0.07)))
        volley_times += 1
        total_points += int((points + (points * 0.07)))
    elif game_name == 'badminton':
        tennis_times += 1
        badminton_points += int((points + (points * 0.02)))
        total_points += int((points + (points * 0.07)))
    elif game_name == 'tennis':
        tennis_times += 1
        tennis_points += int((points + (points * 0.05)))
        total_points += int((points + (points * 0.07)))

if (volley_points / volley_times) > 75 and (tennis_points / volley_points) > 75 and (
        badminton_points / badminton_times) > 75:
    winner = True

if winner:
    print(f'Congratulations, {name}! You won the cruise games with {tennis_points} points.')
else:
    print(f'Sorry, {name}, you lost. Your points are only {total_points}.')