mov = ['Sholay','Baghban','DDLJ','IronMan','RRR','Inception','KungFuPanda','Sooryavansham','Batman']

#length of list 
print(len(mov))

#sort of elements 
mov.sort()
print(mov)

#reverse of list
mov.reverse()
print(mov)

print("First movie = ",mov[0])

print("Last movie = ",mov[-1])

print("First three = ",mov[:3])

print("All Movies except first three = ",mov[3:])

print("All even indexes = ",mov[::2])      #[start:end:gap]  for even gap of 2

