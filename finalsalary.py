# Write a program to find the Final Salary of an employee.

name=str(input("Enter Employee name  = "))
bsal=float(input("Enter the base salary = "))

if bsal > 100000:
    da=float(bsal*0.035)
    hra=float(bsal*0.091)
elif bsal > 80000:
    da=float(bsal*0.032)
    hra=float(bsal*0.090)
elif bsal > 60000:
    da=float(bsal*0.028)
    hra=float(bsal*0.090)
elif bsal > 50000:
    da=float(bsal*0.025)
    hra=float(bsal*0.080)
elif bsal > 40000:
    da=float(bsal*0.025)
    hra=float(bsal*0.077)
elif bsal > 30000:
    da=float(bsal*0.022)
    hra=float(bsal*0.080)
elif bsal > 20000:
    da=float(bsal*0.022)
    hra=float(bsal*0.070)
else:
    da=float(bsal*0.022)
    hra=float(bsal*0.060)

fsal = bsal + da + hra

print("************************************")
print("Employee Name = ", name)
print("Base Salary = ",bsal)
print("Your D.A. is =", da)
print("Your H.R.A. is =",hra)
print("Your Final Salary is =",fsal)
print("************************************")
