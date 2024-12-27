#import all the necessary libraries 
import csv
import hashlib
import smtplib
from email.mime.text import MIMEText
from random import randint
import sqlite3
global cursor
# Connect to SQLite database 
conn = sqlite3.connect("tbay.db")
cursor = conn.cursor()


# check if the username is in the user  file
def username_validility(username):
    query = "SELECT EXISTS(SELECT 1 FROM users WHERE username = ?)S"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    return(result[0])

def email_validility(email):
    query = "SELECT EXISTS(SELECT 1 FROM users WHERE email = ?) "
    cursor.execute(query, (email,))
    result = cursor.fetchone()
    return(result[0])
    
# write username email and password to the users table in the .db file
def write_username_password(username,password,email):
#retrieve last id 
    cursor.execute("SELECT id FROM users order by id DESC LIMIT 1 ")
    last_id_row = cursor.fetchone()
    if last_id_row:  
        last_id = int(last_id_row[0])  
        new_id = last_id + 1
    else:
        new_id = 1 
#insert Entry into users 
    cursor.execute("INSERT INTO users (id, username,password,email) VALUES (?,?,?,?)",
                   (new_id, username, password,email))
    conn.commit()
#check if password username and email correct
def correct_password_email(username,password,email):
    query = "SELECT EXISTS(SELECT 1 FROM users WHERE username = ?) "
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if result[0]==1:
        query = "SELECT password FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        result=cursor.fetchone()
        if result[0]==password:
            query = "SELECT email FROM users WHERE username = ?"
            cursor.execute(query, (username,))
            result=cursor.fetchone()
            if result[0]==email:
                return(True)
            else:
                print("incorrect email")
        else:
            print("incorrect password ")
    else:
        print("That user does not exist ")

        



# send the user a verification code 
def verify_email(email,code):
    code_string=str(code)
    sender_email = "tbay.transfers@gmail.com"
    receiver_email = email
    subject = "verification code for tbay"
    body = (code_string)
#create the contents of the email
    msg = MIMEText(body)
    msg["subject"]= subject
    msg["from"]= sender_email
    msg["To"]= receiver_email
#establish the connection to the server 
    smtp_server = "smtp.gmail.com"
    port = 587
    password = "kyog qtse wcqp vcxy "

    server = smtplib.SMTP(smtp_server, port)
    server.starttls()

    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_email, msg.as_string())

    server.quit()

    print("Email sent successfully!")



#gets the user to login or sign up until successful 
sign_up=True
while sign_up==True:
    login_or_sign=input("login or sign up")
    if login_or_sign== ("sign up"):
        sign_up=False
        new_user_name=input("enter a user name")
        new_email= input (" enter your email")
        verification_code=randint(1000,9999)
        if username_validility(new_user_name)==1:
            print("username already in use")
            sign_up=True
        elif email_validility(new_email)==1:
            print("email already in use please login") 
            sign_up=True
        else:
            password=input("enter a password")
            verify_email(new_email,verification_code)
            users_code=input ("enter your verification code")
            
            if int(users_code) == verification_code: 
                byteVar= password.encode()
                hashed_password=(hashlib.sha256(byteVar).hexdigest())
                write_username_password(new_user_name,hashed_password,new_email )
                print("done")
            elif int(users_code) != verification_code:
                print("invalid verification code")
                sign_up=True

    elif login_or_sign==("login"):
        user_name=input("enter a username")
        password=input("enter your password")
        user_email= input("enter your email")
        byteVar= password.encode()
        hashed_password=(hashlib.sha256(byteVar).hexdigest())
        if correct_password_email(user_name,hashed_password,user_email)==True:
            print("logged in")


    
        
            
            

