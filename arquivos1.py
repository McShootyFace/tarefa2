x =[]
f= open("\\Users\\Raphael\\Downloads\\codigous\\pithun\\hey.txt","r+")
for i in range(11):
    x.append(int(f.readline()))
f.close
x.sort()
f= open("\\Users\\Raphael\\Downloads\\codigous\\pithun\\heey.txt","w+")
f.writelines(str(x))
f.close