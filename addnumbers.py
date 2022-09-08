sum=0
while True:
    num=input("Enter a number:")
    if num.isnumeric():
        sum+=int(num)
    else:
        break

print("Total ans = ",sum)
