import sqlite3 
import time 
import math
from flask import Flask, request, jsonify, render_template

def method1(start,end):
  lis = []
  timeS = time.time()
  for i in range(start,end+1,1):
    for j in range(2,i,1):
      if i%j==0:
        break
    else:
      if i != 1:
        lis.append(i)
  timeE = time.time()
  return lis,(timeE-timeS)*1000,len(lis)
def method2(start,end):
  lis = []
  timeS = time.time()
  for i in range(start,end+1,1):
    for j in range(2,(i//2)+1,1):
      if i%j==0:
        break
    else:
      if i != 1:
        lis.append(i)
  timeE = time.time()
  return lis,(timeE-timeS)*1000,len(lis)
def method3(start,end):
  lis = []
  timeS = time.time()
  for i in range(start,end+1,1):
    for j in range(2,int(math.sqrt(i))+1,1):
      if i%j==0:
        break
    else:
      if i != 1:
        lis.append(i)
  timeE = time.time()
  return lis,(timeE-timeS)*1000,len(lis)


app = Flask(__name__)

con=sqlite3.connect("primenum.db")
@app.route("/method1/<int:num1>/<int:num2>",methods = ["GET"])  
def disp1(num1,num2):  
    try:  
        timestamp = time.time()
        rang= num1+"-"+num2
        data,elapsed,length = method1(num1,num2)
        method = "method-1" 
        cur = con.cursor()  
        cur.execute("INSERT into Primenum (Data,Timestamp,Range,ElapseTime,Method,Length) values (?,?,?,?,?,?)",(data,timestamp,rang,elapsed,method,length))  
        con.commit()  
        msg = "Data Successfully Added"  
    except:  
        con.rollback()  
        msg = "We can not add the data to the list"  
    finally:  
        return jsonify({'data': data,"elapsed":elapsed,"length":length,"method":"method-1"}) 

@app.route("/method2/<int:num1>/<int:num2>",methods = ["GET"])  
def disp2(num1,num2):   
    try: 
        timestamp = time.time()
        rang= num1+"-"+num2 
        data,elapsed,length = method2(num1,num2)
        method = "method-2" 
        cur = con.cursor()  
        cur.execute("INSERT into Primenum (Data,Timestamp,Range,ElapseTime,Method,Length) values (?,?,?,?,?,?)",(data,timestamp,rang,elapsed,method,length))  
        con.commit()  
        msg = "Data Successfully Added"  
    except:  
        con.rollback()  
        msg = "We can not add the data to the list"  
    finally:  
        return jsonify({'data': data,"elapsed":elapsed,"length":length,"method":"method-2"}) 

@app.route("/method3/<int:num1>/<int:num2>",methods = ["GET"])  
def disp3(num1,num2):    
    try:
        timestamp = time.time()
        rang= num1+"-"+num2   
        data,elapsed,length = method3(num1,num2)
        method = "method-3" 
        cur = con.cursor()  
        cur.execute("INSERT into Primenum (Data,Timestamp,Range,ElapseTime,Method,Length) values (?,?,?,?,?,?)",(data,timestamp,rang,elapsed,method,length))  
        con.commit()  
        msg = "Data Successfully Added"  
    except:  
        con.rollback()  
        msg = "We can not add the data to the list"  
    finally:  
        return jsonify({'data': data,"elapsed":elapsed,"length":length,"method":"method-3"}) 


@app.route("/view")  
def view():  
    con = sqlite3.connect("primenum.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Primenumgenerator")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)  

# driver function
if __name__ == '__main__':

	app.run(debug = True)
