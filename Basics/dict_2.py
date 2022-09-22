from pprint import pp

movies = {}    #blank dict

movies['Top Gun : Maverik'] = 8.3
movies['Avengers: Infinity war'] = 8.5
movies['Star wars'] = 7.0

pp(movies)

#Loop in dict 
print("Movies")
for item in movies:
    print(item)

# to print value of keys 
print("Values")
for key in movies:
    print(movies[key])

print("Key & Values")
for key in movies:
    print(key, movies[key])


print("Key and value using dict.items() method")
for k,v in movies.items():      #here items is a functiuon that fetches each item in a dict to proceed 
    print(k,v)


#Taking a user input 
for i in range(3):
    name = input("Enter the movie name = ")     #Entering keys
    rating = float(input("Enter the rating = "))      #entering values 
    movies[name] = rating                           #Making key-value pair 

print("Using dict.items() method ")
for k,v in movies.items():
    print(k ,v)