from random import randint, choice

x = randint(1, 9)
y = randint(1, 9)
op = choice(["+", "-", "*", "/"])
r = randint(1, 18)

sum_ = x + y
minus = x - y
product = x * y
remain = x // y

print("*" * 10)
print(x, op, y, "=", r, sep=" ")
print("*" * 10)

if sum_ == r:
    correct = True
elif minus == r:
    correct = True
elif product == r:
    correct = True
elif remain == r:
    correct = True
else:
    correct = False

choice_ = input("(T/F)?: ").upper()

if correct is True:
    if choice_ == "T":
        print("Hell yeah")
    elif choice_ == "F":
        print("Wrong")
    else:
        print("Invalid input")

else:
    if choice_ == "F":
        print("Hell yeah")
    elif choice_ == "T":
        print("Wrong")
    else:
        print("Invalid input")
