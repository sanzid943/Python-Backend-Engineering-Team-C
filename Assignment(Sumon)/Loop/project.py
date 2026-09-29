# Number Analyzer

number = int(input("Enter a positive integer: "))

# Print numbers from 1 to number
print("\nNumbers from 1 to", number)

for i in range(1, number + 1):
    print(i)

# Print even numbers
print("\nEven numbers:")

for i in range(1, number + 1):
    if i % 2 == 0:
        print(i)

# Print odd numbers
print("\nOdd numbers:")

for i in range(1, number + 1):
    if i % 2 != 0:
        print(i)

# Calculate sum of all numbers
total = 0

for i in range(1, number + 1):
    total = total + i

print("\nSum of all numbers:", total)

# Calculate sum of even numbers
even_sum = 0

for i in range(1, number + 1):
    if i % 2 == 0:
        even_sum = even_sum + i

print("Sum of even numbers:", even_sum)

# Calculate sum of odd numbers
odd_sum = 0

for i in range(1, number + 1):
    if i % 2 != 0:
        odd_sum = odd_sum + i

print("Sum of odd numbers:", odd_sum)

# Calculate factorial
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial:", factorial)

# Multiplication table
print("\nMultiplication table:")

for i in range(1, 11):
    print(number, "x", i, "=", number * i)