from flask import Flask, render_template, request
from flask import Flask, render_template, json, request
#from flask_mysqldb import MySQL

import pymysql
import sys
import pymysql.cursors
from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, request
from flask import flash

from flask import Flask, session, redirect, url_for, escape, request
#from settings import PROJECT_ROOT
import os

#import mysql.connector
app = Flask(__name__)



connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='Todolist',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/About',methods = ['POST', 'GET'])
def About():
    return render_template("About.html")


@app.route('/login',methods = ['POST', 'GET'])
def login():
    return render_template("Login.html")

@app.route('/Adminlogin',methods = ['POST', 'GET'])
def Adminlogin():
    return render_template("Adminlogin.html")

@app.route('/Contact',methods = ['POST', 'GET'])
def Contact():
    return render_template("Contact.html")

@app.route('/Adminhome',methods = ['POST', 'GET'])
def Adminhome():
    return render_template("Adminhome.html")


@app.route('/Userhome',methods = ['POST', 'GET'])
def Userhome():
    return render_template("Userhome.html")

@app.route('/useradmin',methods = ['POST', 'GET'])
def useradmin():
    try:
        connection = pymysql.connect(host='localhost',
                                                 user='root',
                                                 password='',
                                                 db='Todolist',
                                                 charset='utf8mb4',
                                                 cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "select * from usertbl"
            cursor.execute(sql)
            data = cursor.fetchall()
    except Exception as e:
            print(str(e))
    finally:
            connection.close()
    return render_template("Viewuseradmin.html",data=data)


@app.route('/Viewuser',methods = ['POST', 'GET'])
def Viewuser():
    try:
        connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='Todolist',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "select * from usertbl where Uid='"+session['username']+"'"
            cursor.execute(sql)
            data = cursor.fetchall()
    except Exception as e:
        print(str(e))
    finally:
        connection.close()
    return render_template("Viewuser.html",data=data)



@app.route('/useradmina',methods = ['POST', 'GET'])
def useradmina():
    try:
        connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='todolist',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "select * from usertbl"
            cursor.execute(sql)
            data = cursor.fetchall()
    except Exception as e:
        print(str(e))
    finally:
        connection.close()
    return render_template("Viewuseradmin.html",data=data)


@app.route('/clientpage',methods = ['POST', 'GET'])
def clientpage():     
    return render_template("Addclient.html")

@app.route('/addlistpage',methods = ['POST', 'GET'])
def addlistpage():
    try:
        connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='Todolist',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "select * from dailylist where uid='"+session['username']+"'"
            cursor.execute(sql)
            data = cursor.fetchall()
    except Exception as e:
        print(str(e))
    finally:
        connection.close()      
    return render_template("AddList.html",data=data)

@app.route('/addpillspage',methods = ['POST', 'GET'])
def addpillspage():
    try:
        connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='Todolist',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "select * from pills where Uid='"+session['username']+"'"
            cursor.execute(sql)
            data = cursor.fetchall()
    except Exception as e:
        print(str(e))
    finally:
        connection.close()        
    return render_template("AddPills.html",data=data)

@app.route('/Viewrequest',methods = ['POST', 'GET'])
def Viewrequest():
    try:
        connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='Todolist',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "select * from request"
            cursor.execute(sql)
            data = cursor.fetchall()
    except Exception as e:
        print(str(e))
    finally:
        connection.close()
        #return render_template("Viewrequest.html",data=data)    
    return render_template("Viewrequest.html",data=data)


@app.route('/usigninclick1', methods=['POST', 'GET'])
def usigninclick1():
    if request.method == 'POST':
        try:
            p1 = request.form["Uid"]
            p2 = request.form["Pwd"]

            # validate the received values
            if p1 and p2:
                connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='Todolist',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    # Read a single record
                    sql = "select * from usertbl where Uid=%s and Pwd=%s"
                    cursor.execute(sql, (p1, p2))
                    res = cursor.fetchall()
                    if len(res) == 1:
                        connection.commit()
                        connection.close()
                        session['username']=p1
                        return render_template('Userhome.html',username=session['username'])

                    else:
                        error = "Invalid login"
                        connection.commit()
                        connection.close()
                        return "Invalid login"


        except Exception as e:
            return json.dumps({'error': str(e)})


@app.route('/asigninclick', methods=['POST', 'GET'])
def asigninclick():
    if request.method == 'POST':
        try:
            p1 = request.form["Uid"]
            p2 = request.form["Pwd"]

            # validate the received values
            if p1 and p2:
                connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='Todolist',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    # Read a single record
                 
                    sql = "select * from admin where Userid=%s and Pwd=%s"
                    cursor.execute(sql, (p1, p2))
                    res = cursor.fetchall()
                    if len(res) == 1:
                        connection.commit()
                        connection.close()
                        session['username']=p1
                        return render_template('Adminhome.html')

                    else:
                        error = "Invalid login"
                        connection.commit()
                        connection.close()
                        return "Invalid login"


        except Exception as e:
            return json.dumps({'error': str(e)})
        

@app.route('/addclient', methods=['POST', 'GET'])
def addclient():
        try:
            if request.method == 'POST':
                p1 = request.form["fname"]
                p2= request.form["uid"]
                p3= request.form["pwd"]
                p4= request.form["emailid"]
                p5= request.form["addr"]
                p6 = request.form["mob"]
               
                # validate the received values
                if p2 and p3:

                    try:
                        connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='Todolist',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
                        with connection.cursor() as cursor:                        
                            # _hashed_password = generate_password_hash(pwd)
                            # Read a single record
                            sql = "INSERT INTO usertbl VALUES (null,%s, %s, %s, %s, %s, %s)"
                            cursor.execute(sql, (p1, p2, p3, p4, p5, p6))
                            connection.commit()                            
                    except Exception as e:
                        print(str(e))
                        echo (str(e))
                    finally:
                        connection.close()
                        return "Saved successfully."
                        return render_template("Addclient.html")
                else:
                    return json.dumps({'html': '<span>Enter the required fields</span>'})

        except Exception as e:
            return json.dumps({'error': str(e)})

        #finally:
            # cursor.close()
            return render_template("Addclient.html")
        


@app.route('/adeleteuser/<int:id>',methods = ['POST', 'GET'])
def adeleteuser(id):
    try:
       if request.method == 'GET':
          # validate the received values
          
            try:
                
                connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='Todolist',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    # Read a single record
                    sql = "delete from client where id=%s"
                    cursor.execute(sql, (id))
                    connection.commit()
                    sql = "select * from usertbl"
                    cursor.execute(sql)
                    data = cursor.fetchall()
                    return render_template("Addclient.html", data=data)
            except Exception as e:
                print(str(e))
                return  json.dumps({'error': str(e)})
            finally:
                #connection.close()
                return render_template("Addclient.html", data=data)
                #return "Update successfully done."
            #data = cursor.fetchall(

    except Exception as e:
       return json.dumps({'error': str(e)})

@app.route('/addlist', methods=['POST', 'GET'])
def addcase():
        try:
            if request.method == 'POST':
                p1 = request.form["t1"]
                p2= request.form["t2"]
                p3= request.form["t3"]
                p4= request.form["t4"]              
               
                # validate the received values
                if p1 and p2:

                    try:
                        with connection.cursor() as cursor:
                            # _hashed_password = generate_password_hash(pwd)
                            # Read a single record
                            sql = "INSERT INTO dailylist VALUES (null,%s, %s, %s, %s)"
                            cursor.execute(sql, (p1, p2, p3, p4))
                            connection.commit()
                            sql = "select * from dailylist where uid='"+session['username']+"'"
                            cursor.execute(sql)
                            data = cursor.fetchall()
                    except Exception as e:
                        print(str(e))
                    finally:
                        connection.close()
                        return "Saved successfully."
                    data = cursor.fetchall()

                else:
                    return json.dumps({'html': '<span>Enter the required fields</span>'})

        except Exception as e:
            return json.dumps({'error': str(e)})

        finally:
            # cursor.close()
            return render_template("AddList.html", data=data)
        #connection.close()


@app.route('/udeletelist/<int:id>',methods = ['POST', 'GET'])
def udeletelist(id):
    try:
       if request.method == 'GET':
          # validate the received values
          
            try:
                
                connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='Todolist',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    # Read a single record
                    sql = "delete from dailylist where id=%s"
                    cursor.execute(sql, (id))
                    connection.commit()
                    sql = "select * from dailylist"
                    cursor.execute(sql)
                    data = cursor.fetchall()
                    return render_template("AddList.html", data=data)
            except Exception as e:
                print(str(e))
                return  json.dumps({'error': str(e)})
            finally:
                #connection.close()
                return render_template("AddList.html", data=data)
                #return "Update successfully done."
            #data = cursor.fetchall(

    except Exception as e:
       return json.dumps({'error': str(e)})
   
  
@app.route('/deletepills/<int:id>',methods = ['POST', 'GET'])
def deletejudgment(id):
    try:
       if request.method == 'GET':
          # validate the received values
          
            try:
                
                connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='Todolist',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
                with connection.cursor() as cursor:
                    # Read a single record
                    sql = "delete from pills where id=%s"
                    cursor.execute(sql, (id))
                    connection.commit()
                    sql = "select * from pills where Uid='"+session['username']+"'"
                    cursor.execute(sql)
                    data = cursor.fetchall()
                    return render_template("AddPills.html", data=data)
            except Exception as e:
                print(str(e))
                return  json.dumps({'error': str(e)})
            finally:
                #connection.close()
                return render_template("AddPills.html", data=data)
                #return "Update successfully done."
            #data = cursor.fetchall(

    except Exception as e:
       return json.dumps({'error': str(e)})
   

@app.route('/addpills', methods=['POST', 'GET'])
def addpills():
        try:
            if request.method == 'POST':
                p1= request.form["t1"]
                p2= request.form["t2"]
                p3= request.form["t3"]
                p4= request.form["t4"]
              
                # validate the received values
                if p1 and p2:
                    try:
                        connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='',
                                             db='Todolist',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor)
                        with connection.cursor() as cursor:
                            # _hashed_password = generate_password_hash(pwd)
                            # Read a single record
                            sql = "INSERT INTO pills VALUES (null,%s, %s, %s, %s)"
                            cursor.execute(sql, (p1, p2, p3, p4))
                            connection.commit()
                            sql = "select * from pills where Uid='"+session['username']+"'"
                            cursor.execute(sql)
                            data = cursor.fetchall()
                    except Exception as e:
                        print(str(e))
                    finally:
                        connection.close()
                        return "Saved successfully."
                    data = cursor.fetchall()

                else:
                    return json.dumps({'html': '<span>Enter the required fields</span>'})

        except Exception as e:
            return json.dumps({'error': str(e)})

        finally:
            # cursor.close()
            return render_template("AddPills.html", data=data)
        connection.close()
   
    
@app.route('/astatus/<int:id>', methods=['POST', 'GET'])
def astatus(id):
    #now = datetime.datetime.now()
    return render_template("Updatestatus.html",id=id)
   
    
@app.route('/updatestatus', methods=['POST', 'GET'])
def updatestatus():
        try:
            if request.method == 'POST':
                p1= request.form["t1"]
                p2= request.form["t2"]
               
                # validate the received values
                if p1 and p2:

                    try:
                        with connection.cursor() as cursor:
                            # _hashed_password = generate_password_hash(pwd)
                            # Read a single record    
                            sql = "update request set Status=%s where id=%s"
                            cursor.execute(sql, (p2,p1))
                            connection.commit()      
                    except Exception as e:
                        return json.dumps({'error': str(e)})
                    finally:                        
                        return redirect(url_for('Viewrequest'))        
                else:
                    return json.dumps({'html': '<span>Enter the required fields</span>'})

        except Exception as e:
            return json.dumps({'error': str(e)})

        finally:
            # cursor.close()
            #return render_template("Viewrequest.html", data=data)
            return redirect(url_for('Viewrequest'))
        #connection.close()
   

if __name__ == '__main__':
   app.secret_key = "sadfsdfdfssdfadsfsdfsd"
   app.run(port=5001)