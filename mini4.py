with open("numere.txt", 'r') as f:
    x=f.readline()
x = int(x)

def num(v, filename):
    i = 0
    for i in range(10):
        i+=1
        l = str(x*i)
        filename.write(f'{x} * {i} = {l} \n')
with open("file_out.txt", 'w') as f2:
    num(x, f2)