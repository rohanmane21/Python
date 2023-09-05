# creating an empty list
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())
	lst.append(ele)
print("List:",lst)
sum =0
for i in range(0,n):
	if lst[i]%2==0:
		sum=sum+lst[i]
print(sum)
