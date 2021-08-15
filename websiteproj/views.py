from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import User_of_ocean as User
import time
# Create your views here.
import pymysql
from . import userconf #Credentials for MYSQL

today = date.today()
today = str(today)
'''
a = pymysql.connect(host="localhost", user=userconf.username, password=userconf.password)
mycur = a.cursor()

dbname, tablename = "loginusers", "userinfo"
try:
    mycur.execute(f"CREATE DATABASE {dbname}")
except:
    pass
a.close()
'''
dbname, tablename = "loginusers1", "websiteproj_user_of_ocean" #Using models database name and table.
'''
userdb = pymysql.connect(host="localhost", user="MYSQL", password = "sqlpassword", db=dbname)
mycur = userdb.cursor()
try:
    mycur.execute(f"CREATE TABLE {tablename}\
                  ( uname varchar(100) NOT NULL PRIMARY KEY,\
                    name varchar(100) NOT NULL,\
                    dob date NOT NULL,\
                    password varchar(100) NOT NULL)")
except:
    pass
'''
# Change all lines where mysql connection is used to how they need to implemented using models. In the models define methods to get the job done.
def home(request):
    return render(request=request, template_name="LoginorReg.html")

def registeruser(request):
    return render(request=request, template_name="Register.html", context={"today":today})

def usercollector(request):
    """
    url: /register.
    This function collects user info and saves it in the database after registration.
    """
    username = request.POST["uname"]
    password = request.POST["pass"]
    name = request.POST["name"]
    date = request.POST["date"]
    insert_query = User.objects.create(uname = username, name=name, password=password, dob=date)
    #insert_str = f"INSERT INTO userinfo VALUES ('{username}', '{name}', '{date}', '{password}')"
    try:    
        insert_query.save() #inserting the user to database.
        #mycur.execute(insert_str)
    except:
        error = "The username already exists. Please give a different username."
        return render(request = request, template_name="error1.html", context={"error":error} )
    #userdb.commit()
    print("Done")
    return render(request=request, template_name="result.html", context={"user":name})
    
    
def passwebsite(request):
    """
    This function checks whether any user exists if the user chooses the login option. If there is no users, it is pointless to login. Hence, this function throws an error if there are no users.
    """
    password = "none"
    try:
        #this block of the code is for changing the password if user had forgotten it.
        value = request.POST["route"]
        if value=="1":
            uname = request.POST["uname"]
            password = request.POST["pass"]
            update_query = User.objects.filter(uname=uname).update(password=password)
            for objects in update_query:
                objects.save()
            #update_qry = f'UPDATE {tablename} SET password = "{password}" WHERE uname="{uname}"'
            #mycur.execute(update_qry)
            #userdb.commit()  # mycur = userdb.cursor()
    except:
        error = "No created accounts exist on the database, please go back and register. \U0001f600"
        all_entries = User.objects.all()
        if(all_entries.exists() == False):
            return render(request=request, template_name="error1.html", context={"error":error})
    '''
    mycur.execute(f"SELECT * FROM {tablename}")
    tverfiy = mycur.fetchall();
    verify = len(tverfiy)
    if(verify==0):
       #return render(request=request, template_name="error1.html", context={"error":error})
    '''
    return render(request = request, template_name="login.html")

def verifier(request):
    '''
    Verifies user password and user and directs accordingly.
    '''
    username = request.POST["uname"]
    password = request.POST["pass"]
    error1, error2 = "The username doesn't exist", "The password doesn't match."
    password_and_name = User.objects.filter(uname = username)
    if(password_and_name.exists() == False):
        return render(request = request, template_name="error1.html", context={"error":error1})
    for value_list in password_and_name:
        name, true_password = value_list.name, value_list.password
    if(true_password!=password):
        return render(request = request, template_name="error1.html", context={"error":error2})
    #check_str = f"SELECT password, name FROM userinfo WHERE uname='{username}'"
    #mycur.execute(check_str)
    #a = tuple(mycur.fetchall())
    #if(len(a)==0): #Only one row has this username. If username doesn't exist, len is zero.
        #return render(request = request, template_name="error1.html", context={"error":error})
    #name, trupass = a[0][1], a[0][0]
    #if(trupass != password):
        #error = "The password doesn't match."
        #return render(request = request, template_name="error1.html", context={"error":error})
    
    return render(request = request, template_name="result.html", context={"user":name})

def changepass1(request):
    return render(request=request, template_name="newpass1.html", context={"today":today})

def changepass2(request):
    uname = request.POST["uname"]
    dob = request.POST["date"]
    error1 = "The username doesn't exist"
    error2 = "Date of birth doesn't match"
    dob_query = User.objects.filter(uname=uname)
    truedob = list(dob_query.values_list('dob', flat=True))
    if(dob_query.exists()==False):
        return render(request = request, template_name="error1.html", context={"error":error1})
    else:
        if(str(truedob[0]) != dob):
            return render(request = request, template_name="error1.html", context={"error":error2})
    #check_str = f"SELECT dob FROM userinfo WHERE uname='{uname}'"
    #mycur.execute(check_str)
    
    #a = tuple(mycur.fetchall())
    #if(len(a)==0):
       # return render(request = request, template_name="error1.html", context={"error":error1})
    #else:
       # if(str(dob) != str(a[0][0])):
        #    return render(request = request, template_name="error1.html", context={"error":error2})

    return render(request = request, template_name="newpass2.html", context={"uname":uname})
