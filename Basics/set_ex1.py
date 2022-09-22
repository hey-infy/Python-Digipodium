
#making a set 
my_set = {1,2,3,4,2,3,1,5,8,6,7}     #will not show repeating values 
print(my_set)

#set from list
list_x = [1,2,3,4,5,6]
m_set = set(list_x)
print(m_set)
print(type(m_set))


#error due to mutable entry
myy_set = {1,2,[3,4]}     #unhachable type list error


#Creating empty set 
a = set()   #use of set function for blank set 
print(type(a))

#modify set 
my_set = {1,2}
print("Original set was = ",my_set)

#Adding element
my_set.add(2)      #add funtion to add 1 value at a time 
print("After adding 2 to it = ",my_set)

#Add multiple values 
my_set.update([2,3,4,5,6])    #update function add multiple values (can be list, set, tuple or comma separated) 
print("After updating multiple values = ",my_set)

#Add multiple values from diffrent entities
my_set.update([3,8,9],{1,6,10,45})
print("Final set is = ",my_set)


#Removing item from set 
#Using discard and remove function

n_set = {1,2,3,4,5,6}
print(n_set)

#removal by discard function 
n_set.discard(4)
print(n_set)

#removal by remove function (same as discard) but if element not present program crash
n_set.remove(6)
print(n_set)

#pop function (removes random element)
n_set.pop()
print(n_set)

#clear function     to clean entire set at once 
n_set.clear()
print(n_set)



