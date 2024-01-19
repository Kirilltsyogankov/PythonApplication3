#1
#for
from base64 import b16decode


r=0
for i in range(15):
    arv=float(input("Siseta {0}.arv".format(i+1)))
    if arv==int(arv):
        r+=1
print("Täisarvude aev on "+str(r))
#while tingimustega
r=0
i=0
while i<15:
    i+=1
    ar=float(input("Siseta {0}.arv ".format(i)))
    if arv==int(arv):
        r+=1
    if i==15: break
print("Täisarvude arv on "+str(r))

  


c=1
b=1
a=int(input())
for i in range(1,a,1):
    b+=1
    c+=b 
print(c)


c=1
b=1
a=int(input())
while True:
    b+=1
    c+=b 
    if b==a:
        break
print(c) 



c=1
b=1
a=int(input()) 
while a>b:
    b+=1
    c+=b 
print(c)


