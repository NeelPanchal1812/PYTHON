from functools import*
l=[1,2,3,4,5,6]
# s=[]
# for i in l:
#     if i%2==0:
#         s.append(i)
# print(max(s))

# even=[i for i in l if i%2==0]
# odd=[i for i in l if i%2!=0]
# print(even)
# print(max(even))
# print(odd)
# print(max(odd))
# l[0],l[-1]=l[-1],l[0]
# print(l)
# sum=reduce(lambda x,y:x+y,l)
# add=list(map(lambda x:x+10,l))
# fil=list(filter(lambda x:x>2,l))
# rev=l[::-1]
# print(sum)
# print(add)
# print(fil)
# print(rev)


# a={1:1,2:4}
# b={1:5,3:7}
# a.update(b)
# print(a)

# l=[-1,-5,-9,-3,2,-6,7,9,3,4,1]
# possum=list(filter(lambda x:x>0,l))
# possum.sort(reverse=True)
# negsum=list(filter(lambda x:x<0,l))
# print(sum(possum))
# print(sum(negsum))
# print(possum+negsum)


# L=[13,19,28,38,39,57,93]
# div=list(filter(lambda x:x % 19==0 or x %13 == 0,L))
# print(div) 

# t=[4,6,6,4,2,2,4,8,5,8]
# l={}
# for i in t:
#     l.setdefault(i,[]).append(i)
# sort=sorted(l.items(),key=lambda x:len(x[1]),reverse=True)
# result=(dict(sort))
# print(result)


# t=[4,6,6,4,2,2,4,8,5,8]
# d={}
# for i in t:
#     d.setdefault(i,[]).append(i)
# sort=sorted(d.items(),key=lambda x:len(x[1]),reverse=True)
# print(dict(sort))

# t=[4,6,6,4,2,2,4,8,5,8]
# dic={}
# for i in t:
#     dic.setdefault(i,[]).append(i)
# sor=sorted(dic.items(),key=lambda x:len(x[1]),reverse=True)
# print(dict(sor))


