# This function takes an int parameter called months
# And will return a string corresponding to the number of months we passed into it
def get_time_frame(months):
    # we construct a dict that will be used to validate our input
    # Order of our dict keys will dictate the order of our conditional arguments
    divisors = {12: ["Annual", f"{int(months / 12)} year"],
                3: ["Quarterly", f"{int(months / 3)} quarter"],
                1: ["Monthly", f"{months} month"]}
    # This conditional checks if our timescale can be represented in years, then quarters then months
    # Order of our conditionals matter here because if we checked for quarters before years
    # then we would always return quarters since 12 is also divisible by 3
    for d in divisors:
        if months % d == 0:
            if months / d == 1:
                return divisors[d][0]
            else:
                return divisors[d][1]
    # The above loop through he dict is functionally equivalent to the following if, elif else chain:
    # if months % 12 == 0:
    #     if months / 12 == 1:
    #         return "Annual"
    #     else:
    #         return f"{int(months / 12)} year"
    # elif months % 3 == 0:
    #     if months / 3 == 1:
    #         return "Quarterly"
    #     else:
    #         return f"{int(months / 3)} quarter"
    # else:
    #     if months == 1:
    #         return "Monthly"
    #     else:
    #         return f"{months} month"


# The information function does what yours does
# and more if needed, this is thanks to the additional optional params:
# t_frame (time frame) and m (months)
# Note that we default t_frame="Monthly" and m=1 making them optional
# exp default call: information(monthly_costs)
# exp optional call: information(monthly_costs, "Annual", 12)
def information(mon, t_frame="Monthly", m=1):
    # inside or information function, we'll loop through our costs dict
    for mn in mon:
        # for each cost in our dict, we'll construct and print a string using our all parameters
        print(f"{t_frame} {mn} cost: ${format((mon[mn] * m), ',.2f')}")
    # Once we break the loop, we print your divider lines
    print('-------------------------------------------------')


# Thanks to our t_frame and m params we can now have just one period_total function
# (instead of the two nearly identical _total functions you had)
def period_total(mon, t_frame="Monthly", m=1):
    # t is our total cost variable. It will start at 0
    t = 0
    # We'll calculate total cost by looping through our dict
    # and adding the product of the user entered cost times our m param
    for mn in mon:
        t += (mon[mn] * m)
    # Finally, print our total cost for the period
    print(f"{t_frame} total cost: ${format(t, ',.2f')}")
    print('-------------------------------------------------')


# I like my main() function at the bottom of the script, but that's just me
def main():
    # Prompt user.
    print('Hi there. Please enter the following information:')
    print('-------------------------------------------------')
    # Initialize monthly_costs dict:
    # (Notice that this is the only time we ever have to spell maintenance.)
    # Warning I constructed the dict in this way because in your source code,
    # you don't seem to be concerned with error handling when you nested input() inside float().
    # If I was writing this script, I would want error handling in case the user types "1O.OO" or something
    monthly_costs = {"loan": float(input('Monthly Loan Cost: $')),
                     "insurance": float(input('Monthly Insurance Cost: $')),
                     "gas": float(input('Monthly Gas Cost: $')),
                     "oil": float(input('Monthly Oil Cost: $')),
                     "maintenance": float(input('Monthly Maintenance Cost: $'))}
    print('-------------------------------------------------')

    # Call the necessary functions using a loop of the time frames we want to populate
    for i in [1, 2, 3, 9, 12, 24, 36]:
        # For each time frame we want to print, we'll use i as an argument in our get_time_frame function
        # and have the returned string assigned to tf
        tf = get_time_frame(i)
        # we then pass all our arguments into our two print functions
        information(monthly_costs, tf, i)
        period_total(monthly_costs, tf, i)


# Call the main function. Good opportunity to use "if __name__ == "__main__":" here if you wan to be fancy!
if __name__ == "__main__":
    main()
