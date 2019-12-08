import re

def count_vowels():
    s = input('Please enter a string:').lower()
    vowels = re.findall(r"a|e|i|o|u|y",s)
    print(vowels)
    print(len(vowels))


count_vowels()