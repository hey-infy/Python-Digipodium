
#Default Parameter 
def total(a, b=3, c=0):
    return a+b+c

print(total(10,6,78))     # a.k.a Positional parameter b/c arguement position in calling refers to position in parameter 
print(total(a=5))
print(total(a=100,b=50))       #better way to tell which value for which parameter a.k.a  named parameter 
print(total(a=123,b=45,c=88))
