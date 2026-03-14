import sqlite3

API_KEY = "sk_test_1234567890abcdef"   # ❌ Hardcoded secret

def login(user_id, password):
    # ❌ SQL Injection vulnerability
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id = " + user_id + " AND password = '" + password + "'"
    cursor.execute(query)

    result = cursor.fetchone()

    if result:
        print("Login successful")
    else:
        print("Login failed")


def process_payment(amount):
    # ❌ Bad error handling
    try:
        total = amount * 1.18
        print("Processing payment:", total)
    except:
        pass


def long_function():
    # ❌ Code smell: unnecessarily long function
    a=1
    b=2
    c=3
    d=4
    e=5
    f=6
    g=7
    h=8
    i=9
    j=10
    print(a,b,c,d,e,f,g,h,i,j)


user_input = input("Enter user id: ")
password = input("Enter password: ")

login(user_input, password)
process_payment(100)
long_function()
