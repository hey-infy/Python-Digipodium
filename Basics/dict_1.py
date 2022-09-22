#Basic syntax of dictionary
#my_dict = {1: 'Apple',2: 'Banana'}


val_dict = {
    "Employee" : "Rajendra Singh" , "Age" : 30 , "Experience" : 10 
    , "Dept" : "Accounts" , "Designation" : "System Officer" , "Salary" : 600000,
    "team_size" : 7
}

#displaying a dictionary
print(val_dict)

#retreive data from dict
ans = val_dict["Designation"]     #my_dict["Key of value to be printed"]
print(ans)
#or
print(val_dict["Salary"])
print(val_dict["Experience"])     

#Adding Data inside Dict
val_dict["Company"] = "ACME.inc"          
print(val_dict)

from pprint import pp

pp(val_dict)       #pp function stands for Pretty print shows dict in a good look 