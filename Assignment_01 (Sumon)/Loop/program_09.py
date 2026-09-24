number = int(input("Enter a positive integer: "))

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial:", factorial)