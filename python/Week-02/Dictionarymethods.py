# DICTIONARY METHODS - TODAY'S PRACTICE


# 1. get()

student = {
    "name": "Siddhant",
    "age": 21,
    "branch": "CSE(AIML)"
}

print(student.get("name"))
print(student.get("city"))
print(student.get("city", "Not Available"))



# 2. update()

student.update({
    "age": 22,
    "city": "Kolhapur",
    "semester": 5
})

print(student)


# 3. pop()

student = {
    "name": "Rahul",
    "age": 20,
    "branch": "CSE"
}

removed = student.pop("branch")

print(removed)
print(student)


# pop() with default value

student = {
    "name": "Siddhant",
    "age": 21
}

removed_city = student.pop("city", "Not Found")

print(removed_city)
print(student)


# 4. popitem()

student = {
    "name": "Siddhant",
    "age": 21,
    "branch": "CSE(AIML)"
}

removed = student.popitem()

print(removed)
print(student)


# 5. clear()

student = {
    "name": "Rahul",
    "age": 20
}

student.clear()

print(student)


# 6. setdefault()

student = {
    "name": "Siddhant",
    "age": 21
}

student.setdefault("city", "Kolhapur")
student.setdefault("age", 25)

print(student)


# 7. copy()

student = {
    "name": "Siddhant",
    "age": 21,
    "branch": "CSE(AIML)"
}

student2 = student.copy()

student2["age"] = 25

print(student)
print(student2)


# 8. fromkeys()

s = ["name", "age", "city", "branch"]

s1 = dict.fromkeys(s, "Not Available")

print(s1)


# 9. Mixed Dictionary Practice


student = {
    "name": "Siddhant",
    "age": 21,
    "branch": "CSE(AIML)"
}

print(student.get("name"))

student.update({
    "city": "kolhapur"
})

student.setdefault("age", 25)

student2 = student.copy()

student2["age"] = 25

print(student)
print(student2)


# 10. Mixed Challenge


student = {
    "name": "Siddhant",
    "age": 21,
    "branch": "CSE(AIML)"
}

student.update({
    "city": "kolhapur"
})

print(student.get("branch"))

student.setdefault("age", 25)

student2 = student.copy()

student2["age"] = 25

student2.pop("city")

print(student)
print(student2)