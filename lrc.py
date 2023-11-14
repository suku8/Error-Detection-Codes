n=input("Enter the data to be transmitted :")
l=[]
for i in range(len(n)//2):
    t=n[(i*2):(i*2)+2]
    l.append(t)
s=""
for i in l:
    t=bin(int(i,16))
    if(t.count('1')%2==0):
        s=s+'0'
    else:
        s=s+'1'
print("LRC value is",s)
