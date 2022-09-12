# to count the number of times each alphabet has appeared in a file 

from helper import read
data = read('pride_n_prejudice.txt')
from string import ascii_lowercase

for letter in ascii_lowercase:
    counter = data.count(letter)
    print(f'{letter} found {counter} times')

#WAP to find the most occuring alphabet and its frequency