#Wap to enter 5 names in list from user and print each in reverse order 
#Wap to print fibonacci series using the list 
#Wap to generate a new list that contains square of each number from existing list x=[2,3,4,5]
#WAP to generate a list from existing list of numbers containing only odd numbers 
#WAP to generate a new list by adding 2 list elementwise 


#Ans 3
list_1 = []
list_2 = []
r = int(input("Enter the range of the list ="))
for i in range (r):
    var = int(input("Enter the list elements = "))
    list_1.append(var)
    s = var**2
    list_2.append(s)
print(list_2)


#Ans4
list_3 = []
list_4 = []
r = int(input("Enter the range of the list ="))
for i in range (r):
    var = int(input("Enter the list elements = "))
    list_3.append(var)
for j in list_3:
    if j%2!=0:
        list_4.append(j)

print(list_4)


#Ans1
list_x = []
list_y = []
x=int(input("Enter the range = "))
for i in range(x):
    var=str(input("Enter the name = "))
    list_x.append(var)
for j in list_x:
    txt = j[::-1]
    list_y.append(txt)
print(list_y)


#Ans5 
list_x = []
list_y = []
list_s = []
x=int(input("Enter the range for first list = "))
y=int(input("Enter the range for second list = "))
z=x
for i in range(x):
    var=int(input("Enter the element for 1 = "))
    list_x.append(var)

for j in range(y):
    vra=int(input("Enter the element for 2 = "))
    list_y.append(vra)

for p in range(z):
    vr = list_x[p]+list_y[p]
    list_s.append(vr)

print(list_x)
print(list_y)
print(list_s)

#Ans 2
list_f = [0,1]
for i in range(15):
    list_f.append(fib[-1]+fib[-2])
print(list_f)
