a=int(input("=>"))
b=bool=True
c=int=1
d=""
while b==True:
    if a>c:
        c=c*2
    else:
        b=False
if a<c:
    c=c/2
if a%2==0:
    b=True
else:
    b=False
while a!=0:
    if a>=c:
        a=a-c
        d=d+"1"
        if c!=1:
            c=c/2
    else:
        d=d+"0"
        if c!=1:
            c=c/2
while c!=1:
    d=d+"0"
    c=c/2
if b==True:
    d=d+"0"
print(d)