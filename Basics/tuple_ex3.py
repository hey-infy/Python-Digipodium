
#Converting tuple - set - list (Interchangeably)

x = [1,2,3,4,5,4,5,6,7]
xt = tuple(x)     #list-tuple
xl = list(xt)     #tuple-list
xs = set(x)       #list-set
xl = list(xs)     #set-list
xs =set(xt)       #tuple-set
xt = tuple(xs)    #set-tuple

print(type(x))
print(type(xt))
print(type(xl))
print(type(xs))


#WAP to create a tuple by 10 inputs from user 
x=[]
r=int(input("Enter range = "))
for i in range(r):
    var = int(input("Enter the tuple elements = "))
    x.append(var)

t=tuple(x)
print(type(t))
print(t)
