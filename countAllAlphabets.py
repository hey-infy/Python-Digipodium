# to count the number of times each alphabet has appeared in a file 

from helper import read
data = read('pride_n_prejudice.txt')
from string import ascii_lowercase

for letter in ascii_lowercase:
    counter = data.count(letter)
    print(f'{letter} found {counter} times')
    
#WAP to find the most occuring alphabet and its frequency
freq=0               #storing the frequencies of alphabets
freq_letter=""       #storing the character 
for letter in ascii_lowercase:       
    counter = data.count(letter)
    print(f'{letter} found {counter} times')
    if freq<counter:   #checks the value of freq of each character with previous one to store the greatest value for comparision
        freq=counter   #if succeding value is greater then freq will have greater value 
        freq_letter=letter  
print(f'Most occuring is {freq_letter} found {freq} times')