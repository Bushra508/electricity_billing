import mysql.connector
from decimal import *
try:
    m = mysql.connector.connect(host="localhost", user="root", password="&Bushra.S.583", database="electric_bill")
    cursor = m.cursor()
except mysql.connector.Error as err:
    print(f"Error: Unable to connect and create cursor: {err}")
    exit(1)

from datetime import date
def details():
    global date1,total_bill,kwh,rpu
    date1=input("Enter date (YYYY-MM-DD)").strip()
    total_bill=Decimal(input("enter total bill_"))
    kwh=Decimal(input("enter billed units_"))
    rpu=total_bill/kwh

    try:
        command="insert into details (date,billed_unit,total_bill,rate_per_unit) values (%s,%s,%s,%s)"
        cursor.execute(command,(date1,kwh,total_bill,rpu))
        m.commit()
        print("Details inserted!\n")
    except:
        print("Error: Unable to insert details")

def motor():
    global bill_pp_motor
    
    m_reading=Decimal(input("enter the meter reading_"))
    cursor.execute("select max(reading) from motor;")
    max2=cursor.fetchall()
    
    bill_pp_motor=((m_reading-max2[0][0])*rpu)/3
    command="insert into motor (date, reading,bill_per_person) value (%s,%s,%s)"
    
    try:
        cursor.execute(command,(date1,m_reading,bill_pp_motor))
        m.commit()
        print("Details inserted!\n")
    except:
        print("Error: Unable to insert details")

def insertfloor():
    fl=input("floor number_").strip()
    fl="floor"+fl
    value=Decimal(input("enter the meter reading_"))
    
    sql1="select max(reading) from "+fl+";"
    cursor.execute(sql1)
    max1=cursor.fetchall()
    bill=((value-max1[0][0])*rpu)+bill_pp_motor
    
    command="insert into "+fl+"(date, reading,bill) value (%s,%s,%s)"
    try:
        cursor.execute(command,(date1,value,bill))
        m.commit()
        print("Details inserted!\n")
    except:
        print("Error: Unable to insert details")
    """
    command="insert into"+fl+"(bill) value (%s)"
    try:
        cursor.execute(command,(bill,))
        m.commit()
        print("Details inserted!\n")
    except:
        print("Error: Unable to insert details")"""
    
def groundfloor():
    cursor.execute("select bill from floor1 where date=(select max(date)from floor1);")
    fl1=cursor.fetchall()
    cursor.execute("select bill from floor2 where date=(select max(date)from floor2);")
    fl2=cursor.fetchall()
    bill=total_bill-(fl1[0][0]+fl2[0][0]) 
    sql="insert into floor0 values (%s,%s)"
    
    try:
        cursor.execute(sql,(date1,bill))
        m.commit()
        print("Details inserted for ground floor!\n")
    except:
        print("Error: Unable to insert details")
        
    print ("The bill for this month for each floor is:\nFloor1= ",fl1[0][0],"\nFloor2= ",fl2[0][0],"\nGround Floor =",bill)
    
details()
motor()
insertfloor()
insertfloor()
groundfloor()



m.commit()
print("done")
m.close()