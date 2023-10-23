n=6
p=3
A=[7, 11, 33, 5 ]
a=0
b=0
c=0
for i in A:
    if i>a and a>b and i%p!=0:
        c=a
    if i%p!=0 and i>a:
        a=i
    if i%p!=0 and i>b and i!=a:
        b=i
    if c>b and c!=a:
        b=c
print(a*b