# import mysql.connector
# import sys
# import csv
#
# mydatabase = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="password12345"
# )
#
# mycursor = mydatabase.cursor()
# # mycursor.execute("CREATE DATABASE project3")
# mycursor.execute("use project3")
# # mycursor.execute("SHOW DATABASES")
#
# # mycursor.execute("CREATE TABLE instructor (ID VARCHAR(25) PRIMARY KEY, name VARCHAR(240), dept_name VARCHAR(240))")
# # mycursor.execute("CREATE TABLE department (dept_name VARCHAR(240) PRIMARY KEY, location VARCHAR(240), budget numeric(15,2))")
#
# file1 = open("instructor.txt", "r+")
# file2 = open("department.txt", "r+")
#
# # file1_read = csv.reader(file1)
# # file2_read = csv.reader(file2)
# # for row in file1_read:
# #     mycursor.execute('insert into instructor(id, name, dept_name)values(%s, %s, %s)', row)
# #
# # for row in file2_read:
# #     mycursor.execute('insert into department(dept_name, location, budget)values(%s, %s, %s)', row)
# #
# # mydatabase.commit()
#

answer = 1
while answer:
    print('1. Enter the instructor ID and I will provide you with the name of the instructor, '
          'affiliated department and the location of that department.')
    print('2. Enter the department name and I will provide you with the location, budget and names of all instructors '
          'that work for the department.')
    print('3. Insert a record about a new instructor.')
    print("4. Delete a record of an instructor.")
    print("5. Exit")
    answer = input("Please make a selection: ")
    while answer < "0" or answer > "5":
        answer = input("Invalid selection has been made! Please select again: ")
    if answer == "1":
        print(1)
        myresult = []
        if len(myresult) == 0:
            print("This ID does not exist in the database.")
        YID = input("Enter the Instructors ID number: ")

        mycursor.execute("select count(*) from instructor where ID = '" + YID + "'")
        myresult = mycursor.fetchall()
    #
    #     # print(myresult)
    #
    #     if myresult == 0:
    #         print("This ID does not exist in the database.")
    #     else:
    #         mycursor.execute(
    #             "SELECT name, dept_name, location FROM instructor NATURAL JOIN department WHERE ID = '" + YID + "'")
    #         result = mycursor.fetchall()
    #         x = 0
    #         for x in result:
    #             print('\n'.join(x))
    elif answer == "2":
        print(2)
    #     department = input("Enter the department name: ")
    #
    #     query = 'select location, budget from department where dept_name = '" + department + "'"'
    #     print(query.format())
    #
    #
    #
    elif answer == "3":
        print(3)
    #     UserID = input("Enter the instructors ID: ")
    #     UserName = str(input("Enter the instructors name: "))
    #     UserDept = str(input("Enter the affiliated department name: "))
    #
    #     # query = "Select department.UserDept from department where department.UserDept='" + UserDept + '"'
    #     #
    #     # numrows = mycursor.execute(query)
    #     # if numrows > 0:
    #     #     query = "Select instructor.UserID from instructor where instructor.UserID='" + UserID + '"'
    #     #     numrows = mycursor.execute(query)
    #     #     if numrows > 0:
    #     #         print("The instructor already exists in the database.")
    #     #     else:
    #     #         query = "insert into instructor (ID,name,dept_name) values (%s, %s, %s)"
    #     checkdept = "select count(*) from department where dept_name = '" + UserDept + '"'
    #     checkid = "select count(*) from instructor where ID = '" + UserID + '"'
    #     mycursor.execute(checkdept)
    #     mycursor.execute(checkid)
    #     mydatabase.commit()
    #     print(checkdept)
    #     print(checkid)
    #     # if checkdept == 0:
    #     #     print("This department doesn't exist in the database.")
    #     # if checkid == 1:
    #     #     print("This ID record already exists in the database.")
    #     # else:
    #     #     sql = "insert into instructor (id,name,dept_name) values (%s, %s, %s)"
    #     #     val = (UserID,UserName,UserDept)
    #     #     mycursor.execute(sql,val)
    #     #     mydatabase.commit()
    #     #     print(mycursor.rowcount, "record inserted.")
    #
    elif answer == "4":
        print(4)
    #     instructorid = input("Enter the instructor ID: ")
    #
    #     sql = "delete from instructor where ID = %s"
    #     adr = (instructorid,)
    #     mycursor.execute(sql, adr)
    #     mydatabase.commit()
    #     print("Instructor record successfully deleted.")
