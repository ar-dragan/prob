with open("globulet.txt", 'r') as f:
    x=f.readline()
x = int(x)
r = x+3
a = r+x -2
g = x+r+a
with open("bradut.txt", "w") as f2:
    f2.write(str(g))