import mysql.connector

logged_in = False
connection = mysql.connector.connect(user = "root", database = "bank", password = "Arfrfkcmc06")
answer = ""
cursor = connection.cursor()
def deposit(name, amount):
    money = ("Select balance From user_data WHERE User_name = " + name)
    cursor.execute(money)
    
while True:
    info = ("SELECT User_name, Password FROM user_data")

    usernames = []

    passwords = []

    cursor.execute(info)

    for item in cursor:
        usernames.append(item[0])
        passwords.append(item[1])


    print("Welcom to the bank of (name)")
    if answer != "L": 
        answer = input("L for login, S for signup:\n")

    username = ""

    password = ""

    new_sign_in = False

    while not logged_in:

        if answer == "L":
            print("login")
            username = input("username: ")
            
            if username not in usernames:
                print("username incorrect")
                answer = input("L for login, S for signup:\n")
                continue
            if username in usernames:
                password = input("password: ")
                if password == passwords[usernames.index(username)]:
                    logged_in = True
                    break
                print("password incorrect")
                continue
        else:
            print("sign up")
            username = input("username: ")
            password = input("password: ")
            print("your username is " + username + " and password is " + password)
            username = "\"" + username + "\""
            password = "\"" + password + "\""
            user = ("INSERT INTO user_data(User_name, Password, balance) VALUES(" + username + ", " + password + ", 0 )")
            cursor.execute(user)
            connection.commit()
            answer = "L"
            new_sign_in = True
            break

    if new_sign_in: 
        continue
        

            
            
    print("logged in")
    print("welcome " + username)
    answer = ""

    while answer != "logout":
        print("what would you like to do")
        print("options:\ndeposit    withdraw    loans    send    logout")
        answer = input()

    break



connection.close()