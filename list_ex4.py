#WAP to take 10 inputs from user in a list  

list1 = []
x = int(input('Enter the number of elements in list = '))
be=0

for i in range(0,x):
    be=input("Enter the element = ")
    list1.append(be)

print("The balues entered are = ")
print(list1)

#WAP to get inputs from user and find sum mean median mode of the data (int type only)