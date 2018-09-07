numbers = [1, 3, -9, 2, 7, 10, -22]

n = int(input("Enter your number: "))

if n in numbers:
    found_index = numbers.index(n)
    print("Found", n, "at", found_index)
else:
    print("Not Found")
