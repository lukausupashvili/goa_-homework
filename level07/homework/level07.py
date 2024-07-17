user_input = input("შეიყვანეთ მონაცემთა ტიპი (string, integer, float, boolean): ")

types = ["string", "integer", "float", "boolean"]


result = "<class '{}'>".format(user_input) if user_input in types else "უცნობი მონაცემთა ტიპი"

print(result)






