num = int(input("Enter number ="))

match num:
    case 1:
        print(('Sunday'))
    case 2:
        print(('Monday'))
    case 3:
        print("Tuesday")
    case _:
        print("Invalid Data")
        