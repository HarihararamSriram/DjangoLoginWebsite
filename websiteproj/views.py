from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import time
# Create your views here.
import pymysql
from . import userconf #Credentials for MYSQL

today = date.today()
today = str(today)

a = pymysql.connect(host="localhost", user=userconf.username, password=userconf.password)
mycur = a.cursor()
dbname, tablename = "loginusers", "userinfo"
try:
    mycur.execute(f"CREATE DATABASE {dbname}")
except:
    pass
a.close()
userdb = pymysql.connect(host="localhost", user="MYSQL", password = "sqlpassword", db=dbname)
mycur = userdb.cursor()
try:
    mycur.execute(f"CREATE TABLE {tablename}\
                  ( uname varchar(100) NOT NULL PRIMARY KEY,\
                    name varchar(100) NOT NULL,\
                    dob date,\
                    password varchar(100) NOT NULL)")
except:
    pass

def home(request):
    return render(request=request, template_name="LoginorReg.html")

def registeruser(request):
    return render(request=request, template_name="Register.html", context={"today":today})

def usercollector(request):
    username = request.POST["uname"]
    password = request.POST["pass"]
    name = request.POST["name"]
    date = request.POST["date"]
    insert_str = f"INSERT INTO userinfo VALUES ('{username}', '{name}', '{date}', '{password}')"
    try:    
        mycur.execute(insert_str)
    except:
        error = "The username already exists. Please give a different username."
        return render(request = request, template_name="error1.html", context={"error":error} )
    userdb.commit()
    print("Done")
    return render(request=request, template_name="result.html", context={"user":name})
    
    
def passwebsite(request):
    password = "none"
    try:
        value = request.POST["route"]
        if value=="1":
            uname = request.POST["uname"]
            password = request.POST["pass"]
            update_qry = f'UPDATE {tablename} SET password = "{password}" WHERE uname="{uname}"'
            mycur.execute(update_qry)
            userdb.commit()  # mycur = userdb.cursor()
    except:
        pass
    error = "No created accounts exist on the database, please go back and register. \U0001f600"
    mycur.execute(f"SELECT * FROM {tablename}")
    tverfiy = mycur.fetchall();
    verify = len(tverfiy)
    if(verify==0):
        return render(request=request, template_name="error1.html", context={"error":error})
    return render(request = request, template_name="login.html")

def verifier(request):
    '''
    Verifies user password and user and directs accordingly.
    '''
    username = request.POST["uname"]
    password = request.POST["pass"]
    check_str = f"SELECT password, name FROM userinfo WHERE uname='{username}'"
    mycur.execute(check_str)
    error = "The username doesn't exist"
    a = tuple(mycur.fetchall())
    if(len(a)==0): #Only one row has this username. If username doesn't exist, len is zero.
        return render(request = request, template_name="error1.html", context={"error":error})
    name, trupass = a[0][1], a[0][0]
    if(trupass != password):
        error = "The password doesn't match."
        return render(request = request, template_name="error1.html", context={"error":error})
    
    return render(request = request, template_name="result.html", context={"user":name})

def changepass1(request):
    return render(request=request, template_name="newpass1.html", context={"today":today})

def changepass2(request):
    uname = request.POST["uname"]
    dob = request.POST["date"]
    check_str = f"SELECT dob FROM userinfo WHERE uname='{uname}'"
    mycur.execute(check_str)
    error1 = "The username doesn't exist"
    error2 = "Date of birth doesn't match"
    a = tuple(mycur.fetchall())
    if(len(a)==0):
        return render(request = request, template_name="error1.html", context={"error":error1})
    else:
        if(str(dob) != str(a[0][0])):
            return render(request = request, template_name="error1.html", context={"error":error2})

    return render(request = request, template_name="newpass2.html", context={"uname":uname})
