import time
import math
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


  # Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "hello world"
		return jsonify({'data': data})


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/method1/<int:num1>/<int:num2>', methods = ['GET'])
def disp1(num1,num2):
  primes,timeel,length=method1(num1,num2)
  return jsonify({'data': primes,"elapsed":timeel,"length":length,"method":"method-1"})

@app.route('/method2/<int:num1>/<int:num2>', methods = ['GET'])
def disp2(num1,num2):
  primes,timeel,length=method2(num1,num2)
  return jsonify({'data': primes,"elapsed":timeel,"length":length,"method":"method-2"})

@app.route('/method3/<int:num1>/<int:num2>', methods = ['GET'])
def disp3(num1,num2):
  primes,timeel,length=method3(num1,num2)
  return jsonify({'data': primes,"elapsed":timeel,"length":length,"method":"method-3"})


# driver function
if __name__ == '__main__':

	app.run(debug = True)
