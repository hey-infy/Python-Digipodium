#Union operation 

a = {1,2,3,4,5}
b = {4,5,6,7,8,9}
 
print(a | b)           #  | is union symbol  OR  print(a.union(b))     #by union function

#Intersection operation
x = {1,2,3,4,5}
y = {4,5,6,7,8,9}

print(x & y)          #    & is intersection symbol  OR  print(x.intersection(y))    #by intersction fucntion 

#Set diffrence
l = {1,2,3,4,5}
m = {4,5,6,7,8,9}
 
print(l - m)           #  - is diffrence symbol  OR  print(l.diffrence(m))     #by diffrence function
print(m -l)

#Symmetric diffrence : opposite of intersection
A = {1,2,3,4,5}
B = {4,5,6,7,8,9}

print(A ^ B)          #    ^ is sym. diff. symbol  OR  print(A.symmetric_diffrence(B))    #by symmetric_diffrence fucntion 
