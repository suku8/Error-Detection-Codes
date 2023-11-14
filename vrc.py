n=input("Enter the data to be transmitted :")
l=[]
li=[]
for i in range(len(n)//2):
    t=n[(i*2):(i*2)+2]
    l.append(t)
for i in l:
    b=bin(int(i,16))
    bi=b.replace("0b","")
    li.append(bi)
l=[]
for i in li:
    while(True):
        if(len(i)!=8):
            i='0'+i
        else:
            l.append(i)
            break
vrc=[]
for i in range(8):
    summ=""
    for j in range(len(l)):
        summ=summ+l[j][i]
    if(summ.count('1')%2==0):
        t='0'
        vrc.append(t)
    else:
        t='1'
        vrc.append(t)
h=hex(int("".join(vrc),2))
print("VRC value in hexadecimal is",h[2:len(h)],"\nVRC value in binary is","".join(vrc))
