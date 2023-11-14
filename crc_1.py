def xor(d,g,n):
    x=""
    for i in range(n):
        if((d[i]=='0') and (g[i]=='0')):
            x+='0'
        elif((d[i]=='0') and (g[i]=='1')):
            x+='1'
        elif((d[i]=='1') and (g[i]=='0')):
            x+='1'
        elif((d[i]=='1') and (g[i]=='1')):
            x+='0'
    return x

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
    s=xor(idp,gp,ngp)
    ind=s.index('1')
    rem=s[ind::]
    l=ngp-len(rem)
    kl=k+l
    idp=rem+dp[k:kl]
    k=kl
    if(kl==ndp):
        break
print(rem)
    
    
    
