#Break Statement in while loop 
while True:
    price = int(input("Enter price of item:"))
    if price<0:
        break
    print(f'You entered {price} amount')

#this program runs infinitely unless we use a negative input to break the loop and execution


#Difference Between break and continue in example below

x=[1,2,3,4,-3,5,8,48,99]
for i in x:
    if i<0:
        break
    print(i)

x=[1,2,3,4,-3,5,8,48,99]
for i in x:
    if i<0:
        continue
    print(i)