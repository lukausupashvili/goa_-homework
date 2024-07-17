# ცვლადი, რომელშიც შენახულია string ტიპის მნიშვნელობა, რომელიც არ არის რიცხვი
my_string = "123abc"

# ვცდილობთ string-ის გადაქცევას integer-ად
try:
    my_integer = int(my_string)
    print(my_integer)  # თუ გადაკეთება წარმატებულია, ბეჭდავს მნიშვნელობას
except ValueError:
    print("ეს string-ი ვერ გადაკეთდება integer-ად, რადგან ის შეიცავს არარიცხვობრივ სიმბოლოებს")


    String: სტრინგი არის ტექსტური მონაცემი, რომელიც შეიცავს სიმბოლოების მონაცემებს. მაგალითად, "Hello, World!" არის string.

Integer: ინტეჯერი არის მთელი რიცხვი, რომელიც არ შეიცავს წილადებს. მაგალითად, 123 არის integer.

Float: ფლოათი არის რიცხვი, რომელიც შეიცავს წილადებს (დეციმალებებს). მაგალითად, 3.14 არის float.

მაგალითები:


# ეს არის string-ი
my_string = "Hello, World!"
print(type(my_string))  

Integer:
# ეს არის integer
my_integer = 123
print(type(my_integer))   

Float:
# ეს არის float
my_float = 3.14
print(type(my_float))  # <class 'float'>
ახსნა:
#String: "Hello, World!" არის ტექსტური მონაცემი, რომელიც შეიცავს სიმბოლოების მონაცემებს.
#Integer: 123 არის მთელი რიცხვი, რომელიც არ შეიცავს წილადებს.
#Float: 3.14 არის რიცხვი, რომელიც შეიცავს წილადებს.





