def getMonthly():
    anotherMonth = 'y'
    MIN_INVESTMENT = 100
    MAX_INVESTMENT = 10000
    while anotherMonth == 'y':
        try:
            monthly = float(input("Enter Monthly Investment:$ "))
            if monthly < MIN_INVESTMENT:
                print("Monthly investment must be between $100 and $10,000.")
            elif thly > MAX_INVESTMENT:
                print("Monthly investment must be between $100 and $10,000.")
        else:
        anotherMonth = input("Enter another Investment? (y/n) ")
    return monthly
# yearly interest rate (between 5% and 20%)

def getInterest():
    anotherRate = 'y'
    while anotherRate == 'y':
        MAX_INTEREST = 20
        MIN_INTEREST = 5
        interest = float(input("Enter Yearly Interest Rate: %"))
        if interest < MIN_INTEREST:
            print("Interest Rate must be between 5% and 20%")
        if interest > MAX_INTEREST:
            print("Interest Rate must be between 5% and 20%")
        else:
            anotherRate = input("Enter another Interest Rate? (y/n) ")
        return interest
        # duration of investment (bewtween 2 and 30)


def getYears():
    anotherYear = 'y'
    while anotherYear == 'y':
        MAX_YEAR = 30
        MIN_YEAR = 2
        year = int(input("Enter Duration: "))
        if year < MIN_YEAR:
            print("Entry must be between 2 and 30")
        if year > MAX_YEAR:
            print("Entry must be between 2 and 30")
        else:
            anotherYear = input("Enter another Entry? (y/n) ")
        return year
        # calculate future value


def getCalc(monthly, interest, price):
    return monthly, interest, price


def main():
    anotherInvestment = 'y'
    while anotherInvestment == 'y':
        # Welcome to python investing
        print("Welcome to Python Investing!")
        # Make Calls
        monthly = getMonthly()
        interest = getInterest()
        year = getYears()
        getCalc(monthly, interest, year)
        # Display Data
        print("***** Investment Results *****")
        print("Monthly Investment: ", monthly)
        print("Interest Rate (APR): ", interest)
        print("Duration in Years: ", year)
        print("Future Value of the Investment: ")
        # Prompt for antoher investment
        anotherInvestment = input("Another Investment? Enter 'y' to continue or 'x' to quit ")
        # ask user to give following information
        # def monthly investment


main()

# MI = monthly
#
# YI = interest * .01
#
# MIR = YI * 12
#
# FV = MI * MIR
#
# print("Monthly Investment: ",monthly)
#
# print("Interest Rate (APR): ",interest)
#
# print("Duration in Years: ",year)
#
# print("Future Value of the Investment: ",)


# enhancement converty yearly to montly values then make calls
