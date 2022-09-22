'''
#WAP to take 10 inputs from user in a list  

list1 = []
x = int(input('Enter the number of elements in list = '))
be=0

for i in range(0,x):
    be=input("Enter the element = ")
    list1.append(be)

print("The Values entered are = ")
print(list1)
'''

#WAP to get inputs from user and find sum mean median mode of the data (int type only)

list_1 = []
sum=0
r = int(input("Enter the range for list = "))

for i in range (r):
    var = int(input("Enter the list elements = "))
    list_1.append(var)
    sum+=var

x = int(len(list_1))

#Mean of list
mean = sum/x

#Mode of list 
freq = 0
f_var = ""
for i in list_1:
    counter = list_1.count(i)
    if freq<counter:
        freq = counter
        f_var = i 

#Median of list
list_1.sort()
print("Sorted list is = ",list_1)
if x % 2 == 0:
    med1 = list_1[int(x/2)]
    med2 = list_1[int((x/2)+1)]
    med = (med1+ med2)/2
else: 
    med = list_1[int((x+1)/2)]

print("Sum of elements of list is = ",sum)
print("Mean of elements is = ", mean)
print("Mode of the given list is = ",f_var)
print("Median of given list = ", med)