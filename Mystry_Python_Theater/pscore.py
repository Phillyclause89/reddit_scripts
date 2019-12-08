def get_player_score():
    score = []
    for i in range(0, 5):
        while True:
            try:
                s = float(input('Enter golf scores between 78 and 100: '))
                if 78 <= s <= 100:
                    score.append(s)
                    break
                raise ValueError
            except ValueError:
                print("Invalid Input!")
    return score


print(get_player_score())
