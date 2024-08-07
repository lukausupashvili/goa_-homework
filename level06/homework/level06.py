my_name = "ლუკა"  

print(my_Name)  

# ახსნა:
# ზემო ხაზზე (print(my_Name)) მცდარია, რადგან 'my_Name' არ არის განსაზღვრული.
# Python გარჩევს ასოებს შორის, ამიტომ 'my_name' და 'my_Name' ითვლება სხვადასხვა ცვლადებად.
# როცა ვცდილობთ 'my_Name'-ის დაბეჭდვას, Python გამოიტანს NameError შეცდომას, რადგან ის ვერ იპოვის ასეთ ცვლადს



variable = 10  
Variable = 20  
VARIABLE = 30  


print(variable)  
print(Variable)  
print(VARIABLE)  



credit = 100  
CREDIT = 200  
Credit = 300  


print(credit)  
print(CREDIT)  
print(Credit)  


my_variable = "First Value"  

my_variable = "Second Value"  

print(my_variable)  

# ახსნა:
# Python-ში, როცა ცვლადი ერთხელ განისაზღვრება და შემდეგ მიენიჭება ახალი მნიშვნელობა, 
# ძველი მნიშვნელობა იცვლება და ცვლადი ინახავს ახალ მნიშვნელობას.
# ამიტომ, დაბეჭდვისას 'my_variable' გამოიტანს მეორე მნიშვნელობას "Second Value", 
# რადგან ეს არის ბოლო მინიჭებული მნიშვნელობა.

