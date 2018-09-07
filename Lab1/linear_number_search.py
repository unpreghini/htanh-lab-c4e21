numbers = [1, 3, -9, 2, 7, 10, -22]

n = int(input("Please enter your number: "))


for index, number in enumerate(numbers):
    if n == number:
        print("Found", number, "at", index)
        break

else:
    print("Your number cannot be located")
