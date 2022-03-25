import sqlite3

from prettytable import PrettyTable

connection = sqlite3.connect("employee.db")

table_list = connection.execute("select name from sqlite_master where type='table' and name='employee'").fetchall()

if table_list != []:
    print("table already exsist")

else:
    connection.execute(''' create table employee(
                       Id integer primary key autoincrement,
                       empcode integer,
                       name text,
                       phone integer,
                       email text,
                       designation text,
                       salary integer,
                       companyname text                    
    )''')

print("Table created!")

while True:
    print("select an option from the given menu")
    print("1. Add the  employees:")
    print("2. View all employees:")
    print("3. Search an employee using employee name:")
    print("4. Update an employee details with employee code:")
    print("5. Delete an employee using employee code:")
    print("6. Display all the details of employees whose salary is greater than 50000:")
    print("7. Display the count of total number of employees in the company:")
    print("8. Display all the employee details in alphabetical order, within the specific salary range:")
    print("9. Display all the employees data, whose salary is less than the average salary of all the employees:")
    print("10. exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        getempcode = input("Enter the employee code:")
        getname = input("Enter the employee name:")
        getphone = input("Enter the phone number:")
        getemail = input("Enter the email id:")
        getdesignation = input("Enter the designation:")
        getsalary = input("Enter the salary:")
        getcompanyname= input("Enter the company name:")

        connection.execute(
         "insert into employee(empcode, name, phone, email, designation, salary, companyname) values("+getempcode+", '" + getname + "'," + getphone + ",'" + getemail + "','" + getdesignation + "'," + getsalary + ",'" + getcompanyname + "')")
        connection.commit()
        print("Employee details added successfully!")

    elif choice == 2:
        result = connection.execute("select * from employee")
        table = PrettyTable(
            ["Id", "empcode", "name", "phone", "email", "designation", "salary", "companyname"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
            print(table)


    elif choice == 3:
        getname = input("Enter the employee name to be searched:")
        result = connection.execute("select * from employee  where name='"+getname+"'")

        table = PrettyTable(
            ["Id", "empcode", "name", "phone", "email", "designation", "salary", "companyname" ])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
            print(table)

    elif choice == 4:
        getempcode = input("Enter the employee code:")
        getname = input("Enter the employee name:")
        getphone = input("Enter the phone number:")
        getemail = input("Enter the email id:")
        getdesignation = input("Enter the designation:")
        getsalary = input("Enter the salary:")
        getcompanyname = input("Enter the company name:")

        result = connection.execute(
            "update employee set empcode = "+getempcode+", name = '"+getname+"', phone = " +getphone+", email = '"+getemail+"', designation = '"+getdesignation+"', salary = "+getsalary+", companyname = '"+getcompanyname+"'  where empcode= "+getempcode+" ")
        connection.commit()

        print("Employee Data Updated Successfully!")

        result = connection.execute(" select * from employee where empcode ="+getempcode+" ")

        print("Data Updated Successfully!")

        table = PrettyTable(
            ["Id", "empcode", "name", "phone", "email", "designation", "salary", "companyname"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
            print(table)

    elif choice == 5:

        getempcode = input("Enter the employee code: ")

        connection.execute("delete from employee where empcode =" +getempcode)
        connection.commit()

        print("Data deleted successfully")

        result = connection.execute("select * from employee")

        print("Data updated!")

        table = PrettyTable(
            ["Id", "empcode", "name", "phone", "email", "designation", "salary", "companyname" ])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
            print(table)

    elif choice == 6:

        result = connection.execute("select * from employee where salary>50000")

        table = PrettyTable(
            ["Id", "empcode", "name", "phone", "email", "designation", "salary", "companyname"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
            print(table)

    elif choice == 7:

        result = connection.execute("select count(*) as name from employee")
        for i in result:
            print("Total number of employees in the company: =", i[0])

    elif choice ==8:
        lower_range = input("Enter the lower range:")
        higher_range = input("Enter the higher range:")
        result = connection.execute("select * from employee where salary between "+lower_range+" AND "+higher_range+" order by salary asc")

        table = PrettyTable(
            ["Id", "empcode", "name", "phone", "email", "designation", "salary", "companyname"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
            print(table)

    elif choice == 9:

        result = connection.execute("select * from employee where salary<(select avg(salary) as salary from employee)")

        table = PrettyTable(
            ["Id", "empcode", "name", "phone", "email", "designation", "salary", "companyname"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
            print(table)

    elif choice == 10:
        break

    else:
        print("invalid choice")