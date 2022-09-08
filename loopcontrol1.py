#Continue Statement in for Loop
x=[1,2,3,0,4,5,0,7,0,9]
for i in x:
    if i==0:
        continue
    print(i)

#Continue Statement in While Loop

i = 1
while i<=5:
    data=input("Enter the Data:")
    if len(data) == 0:
        continue
    print(f"You have entered  value of size {len(data)}")
    i+=1
