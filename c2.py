class Cat:

    # init is constructor  fixed name 
    def __init__(self, name, age, breed):      #self refers to class itself and other three are parameters  
        #Syntax for making instance_variable
        # self.<required attribute> = <parameter passed in init function>
        self.name = name 
        self.age = age
        self.breed = breed 

cat1 = Cat('Soni', 3, 'Persian')     #Making obj and passing values for each cat 
cat2 = Cat('Mia', 2, 'Siamese')
cat3 = Cat('Molly', 4, 'Egyptian Mau')

print(cat1.name, cat1.age, cat1.breed)
print(cat2.name, cat2.age, cat2.breed)
print(cat3.name, cat3.age, cat3.breed)