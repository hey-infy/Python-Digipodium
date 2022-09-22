books = ['AtomicHabits','MyEXPWithTruths','RichDadPoorDad','TheMonkWhoSoldHisFerrari']

#Add in list
books.append('The Final Empire')
books.append('Three mistakes of my life')
books.append('You can win')
books.append("Wings of Fire")

print(books)

#enumerate function
print('idx \t | \t Book')     # \t guves 4 blank spaces
for i,b in enumerate(books):
    print(f'{i}\t | \t {b}')

print()
#Update value in the list 
books[6] = "The well of Ascension"
books[-1] = "God of Wars"
books[2] = "Legion"
print('idx \t | \t Book')
for i,b in enumerate(books):
    print(f'{i}\t | \t {b}')

print()
#insert data at specific index 
#insert increases the list elements
books.insert(3,'Legion : Skin Deep')
books.insert(5,'Zodiacs')

print('idx \t | \t Book') 
for i,b in enumerate(books):
    print(f'{i}\t | \t {b}')

print()
#remove data from list
books.remove('Legion')
books.pop(3)             #pop(index_number) is used to remove items from index number & this value can be stored in a variable. 

print('idx \t | \t Book') 
for i,b in enumerate(books):
    print(f'{i}\t | \t {b}')
print()

#extend() used to add a new list to existing lists not adding of lists.
fruits = ['apple','banana','cherry','guava']
dry_fruits = ['almonds','cashew','walnut']
fruits.extend(dry_fruits)
print(fruits)
print(dry_fruits)

#example 2 of extend
x = [1,2,3,2,3,1,2,3,1,2,3,2,1,1,3,3]
y = [54,48,68,24,65,10,27,66]
z = [12,45,78,67,11]

print("Adding x to y ")
x.extend(y)
print(x)
print("Adding x to z ")
x.extend(z)
print(x)
print("Adding y to z ")
y.extend(z)
print(y)

