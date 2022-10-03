class Calculator:
    
    #One and only Constructor in PYTHON 
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    #instance method (not a constructor):    
    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y
    
    def multiply(self):
        return self.x * self.y
    
    def divide(self):
        return self.x / self.y

