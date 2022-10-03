class Dog:        #Class definition 
    breed = 'Labrador'
    age = 3
    name = 'Scooby-Doo'

dog1 = Dog()      #object instantiation of class
dog1.name = 'Sheru'
dog1.age = 5
dog1.breed = 'German Shepherd'

dog2 = Dog()      #another object of class for new data 
dog2.name = 'Airtel Vala Kutta'
dog2.age = 8
dog2.breed = 'Pug'

dog3 = Dog()
dog3.name = 'Tejinder'
dog3.age = 6
dog3.breed = 'Great Dayne'

print(dog1.name, dog1.age, dog1.breed)
print(dog2.name, dog2.age, dog2.breed)
print(dog3.name, dog3.age, dog3.breed)