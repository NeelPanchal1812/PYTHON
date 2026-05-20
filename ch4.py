#PALINDROME 291
# s="NeelleeN"
# if s==s[::-1]:
#     print("palindrome")
# else:
#     print("not")


#LENGTH OF STRING 292
# s="NEEL PANCHAL"
# print(len(s))   ---->>> 12


#LENGTH OF STRING WITHOUT LEN FUNCTION 293
# l=0
# L=[]
# s="NEEL PANCHAL"
# for i in s:
#     l=l+1
#     L.append(i)
# print(L)
# print("len of String is",l)


#NEGATIVE INDEXING IN TUPLE 295
# T=(1,3,4,5,6,7)
# print(T[-1],T[-2],T[-3],T[-4],T[-5],T[-6])


#ROMOVE I TH CHARACTER 296
# s=input("enter the String :")
# i=int(input("ENter the index that remove :"))
# if i==0:
#     print(s[1:])
# elif i==-1:
#     print(s[:-1])
# else:
#     print(s[:i]+s[(i+1):])


#FIRST MIDDLE AND LAST CHARACTER 
# s=input("enter the String :")
# print(f" FIRST CHARACTER IS {s[0]} MIDDLE IS {s[1:-1]} LAST IS {s[-1]}")

#password check
# s=input("ENTER THE STRING :")
# u=l=space=dig=spec=0

# if len(s)>=8:
#     for i in s:
#         if i.isupper():
#             u=u+1
#         elif i.islower():
#             l=l+1
#         elif i.isdigit():
#             dig=dig+1
#         elif i.isspace():
#             space=space+1
#         elif i in "@#$":
#             spec=spec+1
#     print(f" UPPER IS : {u} LOWER IS : {l} DIGIT IS : {dig} SPECIAL CHAR IS : {spec}")
#     if u>=1 and l>=1 and dig>=1 and space==0 and spec>=1:
#         print("STRONG PASSWORD")
#     else:
#         print("UNSAFE") 


#MAX AND MIN ELEMENT IN TUPLE

# t=(1,2,3,4,5)
# print(max(t))


#JOIN

# s="NEEL PANCHAL"
# sp=s.split()
# d="-".join(sp)
# print(d)

#FIND ALL OCCURANCE
# s=input("ENTER THE STRING :").lower()
# sub=input("ENTER THE SUBSTRING :").lower()
# start=0
# while True:
#     pos=s.find(sub,start)
#     if pos==-1:
#         break
#     print(sub,"Found at",pos)
#     start=pos+1


#UPPER HALF
# s="neelpanchal"
# m=len(s)//2
# a=s[:m].upper()+s[m:]
# print(a)

#AVG AND SUM OF STRING
# s="1234567"
# su=0
# a=0
# for i in s:
#     su=su+int(i)
#     a=a+1
# print(f"SUM IS {su}")
# print(f"AVG IS {su/a}")


# s="NEEL PANCHAL HI HOE ARE YOU"
# sp=s.split()
# ans=[]

# for w in sp:

#     if len(w)%2==0:
#         ans.append(w)
# print(ans)
    

# s=input("ENTER THE STRING : ")
# shift=int(input("ENTER THE SHIFT :"))

# cipher=""
# for c in s:
#     if 'A'<=c<="Z":
#         cipher += chr((ord(c)-65+shift)%26+65)
#     elif 'a'<=c<='z':
#         cipher += chr((ord(c)-97+shift)%26+97)
#     else:
#         cipher+=c
# print(cipher)