with open("numar.txt","r") as f:
    n=f.readline()
for i in range(1,11):
    x=str(i)+"*"+n+"="+str(i*int(n))
    with open("inmultire.txt","a") as f:
        f.write(x)
        f.write("\n")