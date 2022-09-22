
#Create a string and print it 
string_1 = str(input("Enter the string = "))
print(string_1)

#Enter a string and print its length 
string_2 = str(input("Enter the string = "))
print(string_2)
print(len(string_2))

#Print last word of string using slicing
string_3 = str(input("Enter the string = "))
word = string_3.split()
print(word[-1])

#Print each character of string in a new line 
string_4 = str(input("Enter the string = "))
for i in string_4:
    print(i)

#Print a given string in reverse
string_5 = str(input("Enter the string = "))
print(string_5[::-1])

#Print a given string in uppercase
string_6 = str(input("Enter the string = "))
print("The string in uppercase is = ",string_6.upper())

#Print a given string in lowercase
string_7 = str(input("Enter the string = "))
print("The string in lowercase is = ",string_7.lower())

#Join a given list by the spaces and print it 
words = ['Python','is','easy','to','learn']
joined = "".join(words)
print(joined)

#Print a multiline string using python 


#String move to new line 
t = 'to move to a new line \n is used.'
print(repr(t))


#Print a variable wth text
x = int(input("Enter a value = "))
print("The variable is", x)

#Concatenate the given strings
s1 = "Python"
s2 = "is"
s3 = "great"
print(s1 ,s2 ,s3)

#print # 20 times without loop
print("#"*20)

#Print numbers from 1 to 9 with a dot in vertical lines 
for i in range (1,10):
    print(str(i) + ".")

#User input string print each char in vertical lines 
str_1 = str(input("Enter the string = "))
for i in str_1:
    print(i)

#User input str and check if it ends with "?"
str_x = str(input("Enter the string = "))
if str_x[-1] == "?":
    print("Statement ends with ?")
else:
    print("Not ending with ?")

#User enter str and count appearance of e 
str_a = str(input("Enter the string = "))
count = 0
for i in str_a:
    if i == 'e' or i == "E":
        count+=1
print("E has appeared = ",count, "Times")

#Check is user input is a number 
var = input("Enter a value = ")
if var.isnumeric():
    print("It is a number")
else:
    print("Not a number")

#Remove extra space at beg and end 
text = '    this is not a good string     '
clean = text.strip()
print(clean)

#WAP to print found if any uppercase alphabet letter in user input string
str_l = str(input("Enter the string = "))
for i in str_l:
    if i.isupper():
        print("Uppercase found")

#WAP to get all the individual string names in a list
names = 'Joe , David , Mark , Tom , Chris , Robert'
x = names.split()
print("The names are = ", x)

#ADD aye to the end of each word in a string and print result 
text = 'this is some text'
t = []
y = text.split()
for i in y:
    x = i + 'aye'
    t.append(x)
joined_txt = " ".join(t)
print(joined_txt)

#WAP to check if string contains fyi in it
strn = str(input("Enter the string = "))
if 'fyi' in strn:
    print("FYI is found in string")
else:
    print("FYI not found")

#Program to print only alphabets in a string
text = '%p34@y!*-*!t68h#&on404'
from string import punctuation
for p in punctuation:
    text=text.replace(p,'')
for i in text:
    if i.isnumeric():
        text=text.replace(i,'')
print(text)

#WAP to find avg ord length in a para 
para = "This is a paragraph which is written just for the purpose of providing content to let the average word"
l = len(para)
print("Total length of para = ",l)
y = para.split()
a= len(y)
print("Total number of words in the paragraph = ",a)
print("Average length per word in given paragraph is = ",l/a)
