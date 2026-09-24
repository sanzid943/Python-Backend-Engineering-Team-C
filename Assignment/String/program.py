#student information

name= input("enter your full name: ")
student_id= input("Enter your student ID: ")
age= input("Enter your age: ")
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

print("\nCAPITALIZE-")
print("Name: ", name.capitalize())
print("Address: ", address.capitalize())
print("Hobby: ", hobby.capitalize())

# title

print("\nTITLE-")
print("Name: ", name.title())
print("Address: ", address.title())

# replace

print("\nREPLACE-")

new_address= address.replace("Dhaka", "Rajshahi")
print("New address: ", new_address)

# find

print("\nFIND-")

position= email.find("@")
print("@ position: ", position)


# count

print("\nCOUNT-")
print("Number of 'a' in name: ", name.lower().count("a"))


# starts with

print("\nSTARTS WITH-")

if name.lower().startswith("m"):
    print("Your name starts with M")

else:
    print("Your name doesn't start with M")


# ends with

print("\nENDS WITH-")

if email.lower().endswith(".com"):
    print("This is a .com email")

else:
    print("This is not a .com email")


# in operator

print("\nSEARCH-")

if "python" in hobby.lower():
    print("you like python")

else:
    print("python is not mentioned in your hobby")


# split

print("\nSPLIT-")

name_parts= name.split()
print("name parts: ", name_parts)
print("number of name parts: ", len(name_parts))


# string indexing

print("\nINDEXING-")

if len(name)> 0:
    print("first character: ", name[0])
    print("last character: ", name[-1])


# slicing

print("\nSLICING-")

if len(name)>= 3:
    print("first 3 character: ", name[:3])
    print("last 3 character: ", name[-3:])


# reverse

print("\nREVERSE-")
print("Reverse name: ", name[::-1])

# is alpha

print("\nCHARACTER CHECK-")

if name.replace(" ","").isalpha():
    print("name contains only letters")

else:
    print("name contains numbers or special characters")


# is digit

print("\nAGE CHECK-")

if age.isdigit():
    print("age contains only numbers")

else:
    print("invalid age")


# isalnum

print("\nID CHECK-")

if student_id.isalnum():
    print("student ID is valid")

else:
    print("student ID contains special characters")