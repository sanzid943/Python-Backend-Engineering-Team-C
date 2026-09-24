temperature = float(input("Enter temperature: "))

if temperature < 15:
    print("Cold")
elif temperature <= 30:
    print("Normal")
else:
    print("Hot")