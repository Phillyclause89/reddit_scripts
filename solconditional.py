userBudget = float( input( "What is your monthly budget?"))
while userBudget <= 0:\
      userBudget = int( input('That is not a valid number. Please enter again: '))

expenses = []
for day_number in range (1, 31 + 1):
    while True:
        user_input = input(f"How much did you spend on day {day_number}?\n> ")
        try:
            user_input = float(user_input)
            if user_input < 0:
                raise ValueError
            expenses.append(user_input)
            break
        except ValueError:
            print(f"Amount may not be negative. Try again:")