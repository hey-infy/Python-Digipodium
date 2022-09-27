from random import randint           #from library_name import Function_name

'''
#Non parametrized non-returning function

#Example 1
def hello():            #defining the function 
    print('HOLA AMIGOS')
    print('Say HI')
    print('👋🏻👋🏻👋🏻')
hello()      #calling the function


#Example 2  
def roll_dice():
    dices = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
    print(" => ",dices[randint(0,5)])       #generate random op from list dices 

roll_dice()



#Function Returning Value

#Example 1 
def getsalary():
    val = int(input("Enter the salary = "))
    fine = 0.09
    last = val * fine
    return last

x = getsalary()
print("Your Final Salary is = ",x) 

'''

#Parametrised Function 

def word_count(msg):
    words = msg.split()
    return len(words)

print(word_count("I Am IRONMAN"))