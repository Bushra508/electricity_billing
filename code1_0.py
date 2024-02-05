import mysql.connector

try:
    m = mysql.connector.connect(host="localhost", user="root", password="&Bushra.S.583", database="login_info")
    cursor = m.cursor()
except mysql.connector.Error as err:
    print(f"Error: Unable to connect and create cursor: {err}")
    exit(1)


def signup(id1,password):
    sql="insert into auth values (%s,%s)"
    values=(id1,password)
    cursor.execute(sql,values)
    m.commit()
    
def login(id1,password):
    value=(id1,password)
    sql="select * from auth where id = %s and password = %s"
    cursor.execute(sql,value);
    L = cursor.fetchall()
    if len(L)==0:
        print("ID not found")
           
    else:
        for i in L:
            if i[1]==password:
                print("Successfully logged in!")
                break
            else:
                print("Not the correct password")

def main():
    print("Welcome to our portal!\n")
    while True:
        choice=input("would you like to login or signup?_").strip().lower()
        id1=input("Enter the ID_")
        password=input("Enter the password_")
        if choice=='login':
            login(id1,password)
            break
        elif choice=='signup':
            signup(id1,password)
            break

main()

m.commit()
cursor.close()
m.close()
