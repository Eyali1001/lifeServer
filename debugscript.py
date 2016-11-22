import requests

a = input("make doctor? y/n")
addr = "http://127.0.0.1:5000/"
if a=='y':
	requests.post(addr+"signup",data={'t':'d','u':'doc1','p':'1234','b': '0'})
	print("doc1 1234")
names = ['debug1','debug2','debug3']

for i in range(3):
	requests.post(addr+"signup",data={'t':'p','u':names[i],'p':'1234','b':0,'a':16,'g':'m'})
	requests.post(addr,data={'u':names[i],'d':'sick','c':'general'})
	
print ("patients added.")
print ("debug1,debug2,debug 3 all passwords are 1234")
	