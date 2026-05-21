num=int(input("Enter the number : "))
count=0
rev=0
qube=0
temp=num
while(num>0):
    dig=num%10
    rev=(rev*10)+dig
    qube=qube+(dig**3)
    count+=1
    num=num//10
ld=temp%10
fd=temp//(10**(count-1))
od=(temp%(10**(count-1)))//10
print("reverse no is : ",rev)
print("total count is: ",count)
print("sum of qube is :",qube)
print("last digit is:",ld)
print("first digit is :",fd)
print("middle digit is :",od)

