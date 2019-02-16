print("raju")
a=5
print(a,"is of type",type(a))
a=1+2j
print(a,"is complex number:",isinstance(a,complex))
a=10
b=20
list=[10,20,30,40]
if(a  in list):
    print("a is in given list")
else:
    print("a is not in given list")
a=10
if(a>=20):
    print("true")
elif(a>=10):
        print("checking second condition")
else:
    print("all conditions are false")
for a in range(1,101):
 if a%3==0 and a%5==0:
        print("cricbuzz")
 elif (a%3==0):
    print("cric")
 elif (a%5==0):
    print("buzz")
 else:
    print(a)
r=0
for a in range (1,11):
    r=r+a
print('r',r)
