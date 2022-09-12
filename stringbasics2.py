from re import X
from tkinter import Y


a='shariq'
print(a[0])
print(a[2])
print(a[-1])
print(a[-3])

name= 'vijay Deenanath chauhan'
mena=name[6:-8]
print(mena)
fname= name[:5]
print(fname)
iname = name[-7:] 

# reverse the string
print(name [::-1])

print(name[:5][::-1])
print(name[::2])#vij

#ever odd ind char
print(name[1::2])

x=chr(65)
print(x)

x=chr(12365)
print(x)

x= chr(56789)
print(X)


for i in range(200,15000):
    print(i,chr(i))

y= ord ('A')
print(y)

y= ord ('a')
print(y)

w1='this'
w2='is'
w3='amazin'
msg=w1+w2+w3
print(msg)

a='apple'
b='juice'
ab=a+b
print(ab)
#odding space b/w string
msg=w1+' '+w2+' '+w3
print(msg)

word = 'Hi'
print(word*3) 

print('-'*25)
