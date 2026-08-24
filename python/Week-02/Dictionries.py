# =========================
# DICTIONARIES
# =========================

# Creating a dictionary

student = {
    "name": "Siddhant",
    "age": 20,
    "branch": "CSE(AIML)"
}


# Accessing values

print(student["name"])
print(student["age"])
print(student["branch"])


# Adding a new key-value pair

student["city"] = "Kolhapur"

print(student)


# Updating a value

student["age"] = 21

print(student)


# Removing an item

student.pop("city")

print(student)


# Length

print(len(student))


# Membership

print("age" in student)
print("city" in student)
print("Siddhant" in student)


# keys()

print(student.keys())


# values()

print(student.values())


# items()

print(student.items())


# Loop through keys

for key in student:
    print(key)


# Loop through values

for value in student.values():
    print(value)


# Loop through keys and values

for key, value in student.items():
    print(key, value)


# Accessing values using keys inside a loop

for key in student:
    print(key, ":", student[key])


# Loop + condition

for key in student:
    if key == "age":
        print(student[key])


# Checking multiple keys

for key in student:
    if key == "name" or key == "city":
        print(student[key])

