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

# Part two of https://www.reddit.com/r/learnpython/comments/e8zwkw/how_to_combine_a_list_and_dictionary_together_in/

donkeys_l = ['1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968']
elephants_l = ['1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976']
metrics_d = {'1961': '498717', '1962': '512935', '1963': '521229', '1964': '534660',
             '1965': '556404', '1966': '583399', '1967': '597717', '1968': '615512',
             '1969': '639418', '1970': '641864', '1971': '640888', '1972': '662275',
             '1973': '692498', '1974': '705856', '1975': '683949', '1976': '708708',}

donkeys_d, elephants_d = {}, {}

for year in metrics_d:
    if year in donkeys_l:
        donkeys_d[year] = metrics_d[year]
    elif year in elephants_l:
        elephants_d[year] = metrics_d[year]

print(donkeys_d, elephants_d )

