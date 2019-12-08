from spyobject import SPyObject as SPY

file1 = open(r"creditCards", "r")
# while True:
#     cardNum = file1.readline()
#     print("raw", cardNum)
#
#     cardNum = cardNum.rstrip()
#     print("striped", cardNum)
#     print(len(cardNum))
#
#     if cardNum[0] == str(4) and len(cardNum) == 16:
#
#         print("This card is a Visa, #" + str(cardNum))
#
#     elif cardNum[0] == str(5) and len(cardNum) == 16:
#
#         print("This card is a Mastercard, #" + str(cardNum))
#
#     elif cardNum[0] == str(2) and len(cardNum) == 16:
#
#         print("This card is an American Express, #" + str(cardNum))
#
#     else:
#
#         print("Invalid Card.")


# Determining if a credit card is number is valid

try:
    file1 = open("creditCards.txt", "r")
    S = SPY(file1, globals())
    print(S.attributes, S.obj_info())

except FileNotFoundError:
    print("ERROR! Invalid File!")

else:
    line1 = file1.readline()
    line2 = file1.readline()
    line3 = file1.readline()
    line4 = file1.readline()
    line5 = file1.readline()
    line6 = file1.readline()
    line7 = file1.readline()
    line8 = file1.readline()
    line9 = file1.readline()
    line10 = file1.readline()
    line11 = file1.readline()
    S = SPY(line1, globals())
    print(S.attributes, S.obj_info())

    # while line:
    #     cardNum = file1.readline()
    #     cardNum = cardNum.rstrip()
    #     SPY(cardNum, globals()).obj_info()
    #     if len(cardNum) == 16:
    #         if cardNum[0] == str(4):
    #             print("This card is a Visa, #" + str(cardNum))
    #         elif cardNum[0] == str(5):
    #             print("This card is a Mastercard, #" + str(cardNum))
    #         elif cardNum[0] == str(2):
    #             print("This card is an American Express, #" + str(cardNum))
    #     else:
    #         print("Invalid Card.")
    #     # if len(cardNum) == 0:
    #     #     break

file1.close()
