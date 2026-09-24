#student information

name= input("enter your full name: ")
email= input("enter your email: ")
address= input("enter your address: ")
hobby= input("enter your hobby: ")

# strip

name= name.strip()
email= email.strip()
address= address.strip()
hobby= hobby.strip()

print("\nSTUDENT INFORMATION-")
print("Name: ", name)
print("Email: ", email)
print("Address: ", address)
print("Hobby: ", hobby)

# length

print("\nLENGTH-")
print("Name length: ", len(name))
print("Email length: ", len(email))
print("Address length: ", len(address))
print("Hobby length: ", len(hobby))

# uppercase

print("\nUPPERCASE-")
print("Name: ", name.upper())
print("Email: ", email.upper())
print("Address: ", address.upper())
print("Hobby: ", hobby.upper())

# lowercase

print("\nLOWERCASE-")
print("Name: ", name.lower())
print("Email: ", email.lower())
print("Address: ", address.lower())
print("Hobby: ", hobby.lower())

# capitalize

print("\nUPPERCASE-")
print("Name: ", name.capitalize())
print("Address: ", address.capitalize())
print("Hobby: ", hobby.capitalize())
