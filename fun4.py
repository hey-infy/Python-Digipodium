#Variable Arguements

def mean(*numbers):
    if not numbers:     #not means if numbers does not exist or no value 
        return None
    return sum(numbers)/len(numbers)

print(mean(1,2,3,4))
print(mean(1,22,54,23,77,87,2,4,6,34))
print(mean())
