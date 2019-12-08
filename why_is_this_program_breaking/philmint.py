name = input("Name: \n")
games_played = int(input("Games: \n"))
games = {0: dict(name="volleyball", times=0, points=0, multiplier=0.07),
         1: dict(name="tennis", times=0, points=0, multiplier=0.05),
         2: dict(name="badminton", times=0, points=0, multiplier=0.02)}
total_points = 0
winner = True
for g in range(games_played):
    game = input("Game Name: \n")
    points = int(input("Points: \n"))
    for i in games:
        if games[i]["name"] == game:
            percent = points * games[i]["multiplier"]
            points += percent
            games[i]["points"] += points
            games[i]["times"] += 1
            break
    total_points += points
for i in games:
    if games[i]["times"] < 1 or (games[i]["points"] / games[i]["times"]) <= 75:
        winner = False
        break
if winner:
    print(f'Congratulations, {name}! You won the cruise games with {int(total_points)} points.')
else:
    print(f'Sorry, {name}, you lost. Your points are only {int(total_points)}.')
