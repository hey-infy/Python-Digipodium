for i in range(1,50,7):
    print(i, end=' -- ')



#Reverse looping

for x in range(50,1,-2):
    print(x, end=' ')

print()

#Enumerate function

list1=['apple','samsung','Xiaomi','Realme','Blackberry']
for i in enumerate(list1):
    print(i)

print()

#zip fucntion
list1=['apple','samsung','Xiaomi','Realme','Blackberry']
list2=[100,200,300,400,500]

for x,y in zip(list1,list2):
    print(x," -> ",y)
