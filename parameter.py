def countNumber(a):
	a += 1
	print(a)

def changeList(a):
	for i in range(len(a)):
		a[i] += 1
	print(a)
	
# in python string, number and tuple are unchangeable
a = 1;
countNumber(a)
print a

# in python list and dict are changeable
mylist = [1,2,3]
changeList(mylist)
print mylist

