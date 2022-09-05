'''professional way to code condition4
In this apprach the problems are aways checked first and informed to the users initially
and is also better in terms of CP 
'''
email = input("Enter the mail id =>")
if '@' not in email:
    print("@ kahan hai ?")
elif len(email) < 11:
    print("length not valid !")
elif '.com' not in email and '.org' not in email: 
    print("Invalid statement !!")
else:
    print("Valid Email, ab niklo yahan se.")