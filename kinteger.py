sum = 0
l=[]
n = int(input("Enter a number"))
k = int(input("Enter a number"))
for i in range(n):
    g = int(input("Enter %d  element"%(i)))
    l.append(g)
for i in range(k):
    sum=sum+l[i]
print(sum)
