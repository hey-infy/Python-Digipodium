from datetime import date
from sqlite3 import Date
from helper import read

data= read('pride_n_prejudice.txt')

print(len(data))
newdata = data[3:53]
print(newdata)


#formating fuction
'''     
lower
upper
swapcasse
capitalize
title
casefold
ljust
rjust
center
'''
print('lower=>',newdata.lower())
print('upper=>',newdata.upper())
print('swapcase=>',newdata.swapcase())
print('capitalise=>',newdata.capitalize())
print('title=>',newdata.title())
print('casefold=>',newdata.casefold())

word='hello'
spacing=20

ljust = word.ljust(spacing,'*')
print(ljust)

rjust = word.rjust(spacing,'-')
print(rjust)

cen = word.center(spacing,'$')
print(cen)


#Validation function 

w="HELLO"
print(w.isupper())
print(newdata.islower())
print(newdata.isalpha())
print(newdata.isnumeric())
print(newdata.isalnum())

#utility fucntion

# find ()
''' find ("abcdxyz")  returns the index number of first character of the word,
 only returns the index of word used first (if word is repeated)''' 
id=newdata.find("Pride")
print(f'Pride was found at index = {id}')

# index ()
'''also works as find (), if used in a para, returns the index of word only once where it is first used.'''
idx=data.index("Pride")
print(f'Pride was found at index = {idx}')

# count ()
IN_count=data.count(' in ')       # ( in ) counts only IN but (in) counts even if in comes in any word like ringing, singing
in_count=data.count('in')
print(f'IN occurs {IN_count} times as individual word')
print(f'IN occurs {in_count} times in total')
