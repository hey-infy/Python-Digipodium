from c3 import Calculator
from math import log

class SciCal(Calculator):    #This is inheritance
    
    def log(self):
        return log(self.x, self.y)
    
    def exp(self):
        return self.x ** self.y

    def mod(self):
        return self.x % self.y

    def root(self):
        return self.x ** (1/self.y)

task1 = SciCal(10,3)
print(task1.add())    #here all the functions from inherited class can also be called by object of new class 
print(task1.subtract())
print(task1.multiply())
print(task1.divide())
print(task1.log())
print(task1.exp())
print(task1.mod())
print(task1.root())