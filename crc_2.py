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
print(rem)
