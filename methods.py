# start = int (input("Enter the starting range:"))
# end = int (input("Enter the end range: "))
import sys
import time
import math
start  = int(sys.argv[1])
end = int(sys.argv[2])
print ("Prime numbers in the range", start, "to", end)
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
print(method2(start,end))
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
print(method3(start,end))