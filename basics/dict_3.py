import helper as h
from string import punctuation

data = h.read('basics/pride_n_prejudice.txt')
print(len(data))

#Remove the punctuation
for p in punctuation:
    data = data.replace(p,'')

#Splitting into words and remove empty spaces 
words = [ word.strip() for word in data.lower().split()]      #first lower() -> split() -> strip()  will work

print("Total Words found : ",len(words))
print("Unique Words found : ",len(set(words)))

#create a dict
wc = {}
for word in words:
    if word in wc:
        wc[word] += 1
    else:
        wc[word] = 1

#sorting the dict
wc = sorted(wc.items(), key=lambda x:x[1], reverse = True)        #lambda function 

#Print top 10 occuring words 
for i in range(10):
    print(wc[i])