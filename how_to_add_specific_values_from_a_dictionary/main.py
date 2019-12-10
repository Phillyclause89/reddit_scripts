# import csv

# def statistics():
#     year = {}
#     with open("BLS_private.csv") as f:
#         reader = csv.reader(f)
#         for row in reader:
#             year[row[0]] = {"January":row[1],"Febuary":row[2],"March":row[3],"April":row[4],"May":row[5],"June":row[6],"July":row[7],"August":row[8],"September":row[9],"October":row[10],"November":row[11],"December":row[12]}
#     print(year)
# statistics()

monthly_d = {
    '1961': {
        'January': '45119',
        'Febuary': '44969',
        'March': '45051',
        'April': '44997',
        'May': '45119',
        'June': '45289',
        'July': '45400',
        'August': '45535',
        'September': '45591',
        'October': '45716',
        'November': '45931',
        'December': '46035',
    },
    '1962': {
        'January': '46040',
        'Febuary': '46309',
        'March': '46375',
        'April': '46679',
        'May': '46668',
        'June': '46644',
        'July': '46720',
        'August': '46775',
        'September': '46888',
        'October': '46927',
        'November': '46910',
        'December': '46901',
    },
}

yearly_d = {  # Assign our new dict to a variable
    year: str(  # Key will be year (already a string) and item will need to be a string as per your expected behavior.
        sum(  # Item will also need to be a sum of all the items in that year.
            [  # Sum takes an irritable so we'll generate a list
                int(value) for value in monthly_d[year].values()  # Make sure to convert our values to int or float
            ]  # Don't forget to close our list
        )  # Don't forget to close our sum() call
    ) for year in monthly_d  # Make sure we define our year variable
}  # Finally, don't forget to close our Dict

print(yearly_d)
