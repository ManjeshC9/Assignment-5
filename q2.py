number=int(input("enter a number:"))
n=int(input("enter the range:"))
lists=[]
for i in range(1,n+1):
    if i%number==0:
        lists.append(i)
print(lists)
