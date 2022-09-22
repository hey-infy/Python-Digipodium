#Tuple functions


#Count ()
x=(1,2,3,1,2,3,1,2,1,3,2,3,1,3,2,1,2)

print('3 occurs =',x.count(3))
print('5 occurs =',x.count(5))
print('1 occurs =',x.count(1))

#Index ()
y=(34,76,88,45,13,23,34)
print('34 is at = ',y.index(34,1),'place')    #When same number multiple times only first time index is printed but for second index
print('45 is at = ',y.index(45),'place')       #y.index(SRCH_ELEMENT,start value)
print('13 is at = ',y.index(13),'place')

