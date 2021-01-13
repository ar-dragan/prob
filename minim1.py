with open("numere.txt","r") as f:
    a=f.readline()
    b=f.readline()
if int(a)>int(b):
    x=b
elif int(b)>int(a):
    x=a
else:
    x="Sunt numere egale"
with open("minim.txt","w") as f: 
    f.write(x)