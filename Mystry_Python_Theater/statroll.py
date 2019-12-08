import random

attack = 10
defence = 10

statroll = random.randint(1, 2)
if statroll == 1:
    attack = attack + 1
print(attack, "Attack")
