def parity():
    print("Parity")
    n=input("Enter the data to be transmitted :")
    c=int(input("1.Even parity\n2.Odd parity\nEnter your choice :"))
    cnt=n.count("1")
    if(c==1):
        if(cnt%2==0):
            print("Parity bit is 0")
        else:
            print("Parity bit is 1")
    elif(c==2):
        if(cnt%2==0):
            print("Parity bit is 1")
        else:
            print("Parity bit is 0")
    else:
        print("Sorry! You entered wrong choice")
        
def checksum():
    print("Checksum")
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
    d=int(bi,2)+int('1',2)
    h=hex(d)
    bi=bin(d)
    print("Checksum value in hexadecimal is",h[2:len(h)],"\nChecksum value in binary is",bi[2:len(bi)])

def lrc():
    print("LRC")
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
    h=hex(int(s,2))
    print("LRC value in hexadecimal is",h[2:len(h)],"\nLRC value in binary is",s)
    
def vrc():
    print("VRC")
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

def crc():
    print("CRC")
    dp=input("Enter data polynomial :")
    gp=input("Enter generator polynomial :")
    ngp=len(gp)
    zeros=""
    for i in range(ngp):
        zeros+='0'
    dp+=zeros
    ndp=len(dp)
    idp=dp[0:ngp]
    k=ngp
    global rem
    for i in range(ndp):
        s=bin(int(idp,base=2)^int(gp,base=2))
        ind=s.index('1')
        rem=s[ind::]
        l=ngp-len(rem)
        kl=k+l
        idp=rem+dp[k:kl]
        k=kl
        if(kl==ndp):
            break
    h=hex(int(rem,2))
    print("CRC value in hexadecimal is",h[2:len(h)],"\nCRC value in binary is",rem)

while(1):
    ch=int(input("1-Parity\n2-Checksum\n3-LRC\n4-VRC\n5-CRC\n0-EXIT\nEnter your choice :"))
    print("-"*20)
    if(ch==1):
        parity()
        print("-"*20)
    elif(ch==2):
        checksum()
        print("-"*20)
    elif(ch==3):
        lrc()
        print("-"*20)
    elif(ch==4):
        vrc()
        print("-"*20)
    elif(ch==5):
        crc()
        print("-"*20)
    else:
        print("-"*20)
        break
    
    
