#import all the necassry libraries 
import csv
import hashlib
import smtplib
from email.mime.text import MIMEText
from random import randint
true=True
# check if the username is in the csv file
def username_validility(username):
    with open("usernames.csv",newline="") as database:
        reader= csv.reader(database)
        for row in reader:
            if row[0] == username:
                return True
        return False
def email_validility(email):
    with open("usernames.csv",newline="") as database:
        reader= csv.reader(database)
        for row in reader:
            if row[2] == email:
                return True
# write username email and password to the csv file
def write_username_password(username,password,email):
    with open("usernames.csv","a",newline="") as database:
        writer = csv.writer(database) 
        writer.writerow( [username,password,email])
#check if password is correct
def correct_password_email(username,password,email):
    with open("usernames.csv",newline="") as database:
        reader= csv.reader(database)
        for row in reader: 
            if row[0] == username:
                if row[1]==password:
                    if row[2] == email:
                        return True
# send the user a verification code 
def verify_email(email,code):
    code_string=str(code)
    sender_email = "tbay.transfers@gmail.com"
    receiver_email = email
    subject = "verification code for tbay"
    body = (code_string)

    msg = MIMEText(body)
    msg["subject"]= subject
    msg["from"]= sender_email
    msg["To"]= receiver_email
    
    smtp_server = "smtp.gmail.com"
    port = 587
    password = "kyog qtse wcqp vcxy "

    server = smtplib.SMTP(smtp_server, port)
    server.starttls()

    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_email, msg.as_string())


    server.quit()

    print("Email sent successfully!")



#gets the user to login or sign up untill sucessful 
sign_up=True
login_or_sign=input("login or sign up")
if login_or_sign== ("sign up"):
    while sign_up==True:
        sign_up=False
        new_user_name=input("enter a user name")
        new_email= input (" enter your email")
        verification_code=randint(1000,9999)
        if username_validility(new_user_name)==True:
            print("username already in use")
            sign_up=True
        elif email_validility(new_email)==True:
            print("email alredy in use please login") 
            sign_up=True
        elif true==True:
            password=input("enter a password")
            verify_email(new_email,verification_code)
            users_code=input ("enter your verification code")
            int(users_code)

            byteVar= password.encode()
            hashed_password=(hashlib.sha256(byteVar).hexdigest())
            write_username_password(new_user_name,hashed_password,new_email )
        elif int(users_code) != verification_code:
            print("invalid verification code")
            sign_up=True

elif login_or_sign==("login"):
    user_name=input("enter a username")
    if username_validility(user_name)==True:
        password=input("enter your password")
        user_email= input("enter your email")
        byteVar= password.encode()
        hashed_password=(hashlib.sha256(byteVar).hexdigest())
    if correct_password_email(user_name,hashed_password,user_email)==True:
        print("logged in")


    
        
            
            

