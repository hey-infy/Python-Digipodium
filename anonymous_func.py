#LAMBDA function and mapping function
nums = [1,2,3,4,5,6,7,8,9,23,12,54,65,25,78,32,87]
names = ['Tony Stark','Bruce Banner','Steve Rogers']

num_sqr = list(map(lambda i:i ** 2, nums))   #map each value from nums list to the function of squaring the value and list is wrtten to
print(num_sqr)                               #what for output we want ? 

num_eq1 = list(map(lambda i: i+4 * i**2, nums))
print(num_eq1)


first_names = tuple(map(lambda nm: nm.split()[0], names))    #split()[0] means split the name and fetch the first string
print(first_names)

last_names = tuple(map(lambda mn: mn.split()[-1], names))    
print(last_names)