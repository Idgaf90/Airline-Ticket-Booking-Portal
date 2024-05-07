from pymysql import *  
import sys  
host='127.0.0.1'  
user='root'  
password=''  
import os  
import platform  
import datetime  
global z  
global cust  
global s  
mydb=connect(host,user,password,database='hotel')  mycursor=mydb.cursor()  
print("WELCOME TO OUR AIRLINE TICKET BOOKING WEBSITE")  def registercust():  
 global cust  
 L=[]  
 name=input("Enter name: ")  
 L.append(name)  
 addr=input("Enter address: ")  
 L.append(addr)  
 jr_date=input("Enter date of journey: ")  
 L.append(jr_date)  
 source=input("Enter source: ")  
 L.append(source) 
2.  
 destination=input("Enter destination: ")  
 L.append(destination)  
 cust=(L)  
 sql="insert into pdata(custname,addr,jr_date,source,destination)values(%s,%s,%s,%s,%s)"   mycursor.execute(sql,cust)  
 mydb.commit()  
registercust()  
def classtypeview():  
 ch=int(input("Do you want to see class type available\nEnter 1 for yes : "))   if ch==1:  
 sql="select * from classtype"  
 mycursor.execute(sql)  
 rows=mycursor.fetchall()  
 for x in rows:  
 print(x)  
  
classtypeview()  
def ticketprice():  
 x=int(input("Enter your choice please->"))  
 n=int(input("No of passenger:"))  
 if(x==1):  
 print("You have opted First class")  
 s=6000*n  
 elif(x==2):  
 print("You have opted Business class")  
 s=4000*n 
3.  
 elif(x==3):  
 print("You have opted Economy class")  
 s=2000*n  
 else:  
 print("Please choose a class type")  
 print("Your room rent is = Rs.",s,"\n")  
ticketprice()  
def menuview():  
 print("Do you want to see menu available : Enter 1 for yes : ")   ch=int(input("Enter your choice:"))  
 if ch==1:  
 sql="select * from food"  
 mycursor.execute(sql)  
 rows=mycursor.fetchall()  
 for x in rows:  
 print(x)  
def orderitem():  
 global s  
 ch=int(input("Do you want to see menu available : Enter 1 for yes : "))   if ch==1:  
 sql="select * from food"  
 mycursor.execute(sql)  
 rows=mycursor.fetchall()  
 for x in rows:  
 print(x)  
 d=int(input("Would you like to purchase from above list \nEnter your choice: ")) 
4.  
 if(d==1):  
 print("You have successfully ordered tea")   a=int(input("Enter quantity : "))  
 s=10*a  
 print("Your amount for tea is : Rs.",s,"\n")   elif(d==2):  
 print("You have successfully ordered coffee")   a=int(input("Enter quantity : "))  
 s=10*a  
 print("Your amount for coffee is : Rs.",s,"\n")   elif(d==3):  
 print("You have successfully ordered Cold drink")   a=int(input("Enter quantity : "))  
 s=20*a  
 print("Your amount for Cold drink is : Rs.",s,"\n")   elif(d==4):  
 print("You have successfully ordered samosa")   a=int(input("Enter quantity : "))  
 s=10*a  
 print("Your amount for samosa is : Rs.",s,"\n")   elif(d==5):  
 print("You have successfully ordered sandwich")   a=int(input("Enter quantity : "))  
 s=50*a  
 print("Your amount for sandwich is : Rs.",s,"\n")   elif(d==6): 
5.  
 print("You have successfully ordered dhokla")   a=int(input("Enter quantity : "))  
 s=30*a  
 print("Your amount for dhokla is : Rs.",s,"\n")   elif(d==7):  
 print("You have successfully ordered kachori")   a=int(input("Enter quantity : "))  
 s=10*a  
 print("Your amount kachori is : Rs.",s,"\n")   elif(d==8):  
 print("You have successfully ordered milk")   a=int(input("Enter quantity : "))  
 s=20*a  
 print("Your amount for milk is : Rs.",s,"\n")   elif(d==9):  
 print("You have successfully ordered noodles")   a=int(input("Enter quantity : "))  
 s=50*a  
 print("Your amount for noodles is : Rs.",s,"\n")   elif(d==10):  
 print("You have successfully ordered pasta")   a=int(input("Enter quantity : "))  
 s=50*a  
 print("Your amount for pasta is : Rs.",s,"\n")   else:  
 print("please enter your choice from the menu") 
6.  
 return s  
orderitem()  
def lugagebill():  
 global z  
 ch=int(input("Do you want to see rate for luggage\nEnter 1 for yes : "))   if ch==1:  
 sql="select * from lugage"  
 mycursor.execute(sql)  
 rows=mycursor.fetchall()  
 for x in rows:  
 print(x)  
 y=int(input("Enter your weight of extra luggage->"))  
 z=y*1000  
 print("Your luggage bill is : Rs.",z,"\n")  
 return z  
lugagebill()  
def lb():  
 print(z)  
def res():  
 print(s)  
def ticketamount():  
 print("Customer details : ",cust)  
 print("Luggage bill is :")  
 lb()  
 print("Food bill is :")  
 res() 
7.  
ticketamount()  
def menuset():  
 userinput=1  
 while userinput<8 and userinput>0:  
 print("Enter 1: To update customer data")   print("Enter 2: To see class types")  
 print("Enter 3: To update class type")  
 print("Enter 4: For viewing food menu")  
 print("Enter 5: To update ordered food items")   print("Enter 6: To update Luggage weight")   print("Enter 7: For complete amount")  
 print("Enter 8: For exit")  
 try:  
 userinput=int(input("Please select an above option : "))   except ValueError:  
 exit("\n hi that's not a number")  
 if(userinput==1):  
 registercust()  
 elif(userinput==2):  
 classtypeview()  
 elif(userinput==3):  
 classtypeview()  
 ticketprice()  
 elif(userinput==4):  
 menuview()  
 elif(userinput==5): 
8.  
 orderitem()  
 elif(userinput==6):  
 lugagebill()  
 elif(userinput==7):  
 ticketamount()  
 elif(userinput==8):  
 break  
menuset()  
print("The Boarding pass will be sent prior journey date\n\n\n")  print("THANKS FOR BOOKING WITH US HAPPY JOURNEY")  def runagain():  
 runagn=input("\n want to run again y/n:")  
 while(runagn.lower()=='y'):  
 if(platform.system()=="windows"):  
 print(os.system('cls'))  
 else:  
 print(os.system('clear'))  
 runagn=input("\n want to run again y/n:")  
 menuset()  
runagain() 
