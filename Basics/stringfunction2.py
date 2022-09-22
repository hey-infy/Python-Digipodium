
#Split()
msg = "We Will be seeing the horizon very soon"

words = msg.split()
print(words)

words=msg.split("e")     #splitting from in between the sentence , it will not show the splitting aplhabet
print(words)

#replace()

words=msg.replace(' ','🦐')
print(words)

#join()
path = ['i','am','ironman']
content = "->".join(path)
print(content)

#strip()
name = "     tony       stark     "
clean_name = name.strip()
print(clean_name)
print(len(name), len(clean_name))

#WAP to find frequency of all the vowels in the file 
from helper import read
data = read('pride_n_prejudice.txt')
from string import ascii_lowercase

for letter in ascii_lowercase:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        counter = data.count(letter)
        print(f'{letter} found {counter} times')

#WAP to remove all the punctuations from the string 
# strn = 'he@#ll%o!@&*(!@wo!2r,l!d)'
'''
strn = 'he@#ll$o!@&*(!@wo!2r,l!d)'
for i in strn:
    if i in '!@#$%^&':
        words=strn.replace(i,'X')
        print(words)
'''
strn = 'he@#ll$o!@&*(!@wo!2r,l!d)'
from string import punctuation
for p in punctuation:
    strn=strn.replace(p,'')
print(strn)