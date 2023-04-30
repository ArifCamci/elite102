import mysql.connector


logged_in = False
connection = mysql.connector.connect(user = "root", database = "bank", password = "Arfrfkcmc06")
answer = ""
cursor = connection.cursor()

def deposit(name, amount):
    
    sql = "UPDATE user_data SET balance = balance + %s WHERE User_name = %s"
    val = (amount, name)
    cursor.execute(sql, val)
    connection.commit()

    print("\nadded " + str(amount) + " to your balance")
    input()
    

def withdraw(user_name, amount):


    sql = "UPDATE user_data SET balance = balance - %s WHERE User_name = %s"
    val = (amount, user_name)
    cursor.execute(sql, val)

    # Commit the changes to the database
    connection.commit()

    # Print a message to indicate the withdrawal was successful
    print(f"\nWithdrew {amount} from {user_name}'s account balance.")
    input()

def display_balance(user_name):
    sql = "SELECT balance FROM user_data WHERE User_name = %s"
    val = (user_name,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    balance = result[0]
    print(f"\n{user_name}'s account balance is {balance}.\n")
    input("")

def transfer_balance(source_name, dest_name, amount):
    try:
        sql = "UPDATE user_data SET balance = balance - %s WHERE User_name = %s"
        val = (amount, source_name)
        cursor.execute(sql, val)
        sql = "UPDATE user_data SET balance = balance + %s WHERE User_name = %s"
        val = (amount, dest_name)
        cursor.execute(sql, val)
        connection.commit()
        print(f"\nTransferred {amount} from {source_name}'s account to {dest_name}'s account.")
    except:
        print("\nthe username given isnt in our system\n")
        input()


while True:
    info = ("SELECT User_name, Password FROM user_data")

    usernames = []

    passwords = []

    cursor.execute(info)

    for item in cursor:
        usernames.append(item[0])
        passwords.append(item[1])


    print("Welcome to the bank of (name)")
    input()
    if answer != "L": 
        answer = input("L for login, S for signup: ")

    username = ""

    password = ""

    

    while not logged_in:

        if answer == "L":
            print("login:\n")
            username = input("username: ")
            
            if username not in usernames:
                print("username incorrect")
                input()
                answer = input("L for login, S for signup:\n")
                continue
            if username in usernames:
                password = input("password: ")
                if password == passwords[usernames.index(username)]:
                    logged_in = True
                    break
                print("password incorrect")
                input()
                continue
        else:
            print("sign up")
            input()
            username = input("username: ")
            password = input("password: ")
            print("your username is " + username + " and password is " + password)
            input()
            new_username = "\"" + username + "\""
            new_password = "\"" + password + "\""
            user = ("INSERT INTO user_data(User_name, Password, balance) VALUES(" + new_username + ", " + new_password + ", 0 )")
            cursor.execute(user)
            connection.commit()
            answer = "L"
            break

    
        

            
            
    print("logged in\n")
    print("welcome " + username)
    input()
    answer = ""

    while answer != "logout":
        print("\nwhat would you like to do")
        print("options:\ndeposit    withdraw   send    view balance    logout")
        answer = input()
        if answer == "deposit":
            x = int(input("enter amount you want deposited: "))
            deposit(username, x)
        elif answer == "withdraw":
            x = int(input("enter the amount you want withdrawn: "))
            withdraw(username, x)
        elif answer == "view balance":
            display_balance(username)
        elif answer == "send":
            y = input("what is the account name of the person you want to send to: ")
            x = int(input("how much do you want to send: "))
            transfer_balance(username, y, x)
        elif answer == "logout":
            logged_in = False
            print("you have been logged out")
            answer = input("would you want to leave the app or continue using: (leave or continue) ")
            break
    if answer == "leave":
        break
    
    



connection.close()