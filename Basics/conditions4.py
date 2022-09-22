email = input("Enter the mail id =>")

if '@' in email:
    if len(email)>= 11:
        if '.com' in email or '.in' in email:
            print("Valid email")
        else: 
            print("Visit godaddy")
    else:
        print("Invalid length")
else: 
    print("recheck @")
