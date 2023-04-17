import mysql.connector

connection = mysql.connector.connect(user = "root", database = "bank", password = "Arfrfkcmc06")

cursor = connection.cursor()


info = ("SELECT User_name, Password FROM user_data")

usernames = []

passwords = []

cursor.execute(info)

for item in cursor:
    usernames.append(item[0])
    passwords.append(item[1])

logged_in = False

print("Welcom to the bank of (name)")

answer = input("L for login, S for signup:\n")

username = ""

password = ""

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
            print("password incorrect")
            continue
    else:
        print("sign up")
        username = input("username: ")
        password = input("password: ")
        print("your username is " + username + " and password is " + password)
        username = "\"" + username + "\""
        password = "\"" + password + "\""
        user = "INSERT INTO user_data(User_name, Password, balance) VALUES(" + username + ", " + password + ", 0 )"
        user = (user)
        cursor.execute(user)
        connection.commit()
        answer = "L"
        continue
    

        
        
print("logged in")
answer = "q"

while answer != "q":
    print("what would you like to do")
    print("options:\ndeposit    withdraw    loans   send\ntype q to quit")
    answer = input()



connection.close()