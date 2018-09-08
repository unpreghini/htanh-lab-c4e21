x = int(input("x = "))
op = input("Operation(+, -, *, /): ")

if op == "+":
    y = int(input("y = "))
    print("*" * 10)
    print(x, "+", y, "=", x+y, sep=" ")
    print("*" * 10)

elif op == "-":
    y = int(input("y: "))
    print("*" * 10)
    print(x, "+", y, "=", x-y, sep=" ")
    print("*" * 10)

elif op == "*":
    y = int(input("y: "))
    print("*" * 10)
    print(x, "+", y, "=", x*y, sep=" ")
    print("*" * 10)

elif op == "/":
    y = int(input("y: "))
    print("*" * 10)
    print(x, "+", y, "=", x/y, sep=" ")
    print("*" * 10)

else:
    print("Invalid Operatior")
