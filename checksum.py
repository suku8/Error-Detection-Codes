n=input("Enter the data to be transmitted :")
l=[]
for i in range(len(n)//2):
    t=n[(i*2):(i*2)+2]
    l.append(t)
summ=0
for i in l:
    summ+=int(i,16)
b=bin(summ)
bi=b[2:len(b)]
bi=bi.replace('1','x')
bi=bi.replace('0','1')
bi=bi.replace('x','0')
bi=int(bi,2)+int('1',2)
print("Checksum value is",bi)
