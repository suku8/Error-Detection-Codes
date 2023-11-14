n=input("Enter the data to be transmitted :")
c=int(input("Enter your choice\n1.Even parity\n2.Odd parity\n"))
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
