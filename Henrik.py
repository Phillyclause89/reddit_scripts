
#Uendelig liste Melli oppgave >:)
# Infinite list Melli task> :)

# eternal list = []
evig_liste = []

# again = "yes"
en_gang_til = "ja"

# print ("Enter the desired number in the list:")
print("Skriv inn ønsket tall i listen: ")

# while again == "yes" or again == "Yes":

def validate_input(inpu):
    try:
        return int(inpu)
    except ValueError:
        return inpu

def adding_to_evig_liste(e_g_t):
    if e_g_t.lower() == "ja":
        return True
    return False


while adding_to_evig_liste(en_gang_til):
    # add = int (input ("Enter the number you want to add to the list:"))
    legg_til = validate_input(input("Skriv inn tallet du ønsker å legge til i listen: "))

    # eternal list + = [int (add)]
    evig_liste += [legg_til]

    # again = input ("Do you want to add more numbers to the list?:")
    en_gang_til = input("ønsker du å legge til flere tall i listen? :")

    # print ("your list so far:", forever list)
    print("listen din til nå: ", evig_liste)


# smallest number = everlasting list [0]
minste_tall_index=0
minste_tall=evig_liste[minste_tall_index]

# highest numbers = everlasting list [0]
hoyeste_tall_index = 0
hoyeste_tall=evig_liste[hoyeste_tall_index]



# for in in range (1, len (perpetual list)):
for i, n in enumerate(evig_liste):
    if n <= minste_tall:
        minste_tall_index = i
        minste_tall = n
    if n>= hoyeste_tall:
        hoyeste_tall_index = i
        hoyeste_tall = n



# print ("smallest number in list", smallest number)
print("minste tallet i listen", minste_tall)

# print ("smallest number in list", smallest number)
print("høyeste tallet i listen", hoyeste_tall)


temp = evig_liste[minste_tall_index]
temp2 = evig_liste[hoyeste_tall_index]
evig_liste[minste_tall_index] = temp2
evig_liste[hoyeste_tall_index] = temp

print(temp)

print("listen med byttet høyeste og laveste tall", evig_liste)