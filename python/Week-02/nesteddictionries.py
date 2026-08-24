# Nested Dictionary

students = {
    "student1": {
        "name": "Siddhant",
        "age": 22,
        "branch": "CSE(AIML)"
    },
    "student2": {
        "name": "Rahul",
        "age": 20,
        "branch": "CSE"
    }
}


# Accessing nested values

print(students["student1"]["age"])
print(students["student2"]["branch"])


# Updating nested value

students["student1"]["age"] = 22

print(students["student1"]["age"])


# Adding a new nested key

students["student1"]["city"] = "Kolhapur"

print(students["student1"])


# Removing a nested key

students["student2"].pop("branch")

print(students["student2"])


# Looping through nested dictionary

for i in students:
    print(students[i]["name"])


# Printing name and age

for i in students:
    print(students[i]["name"], ":", students[i]["age"])


# Nested dictionary with condition

for i in students:
    if students[i]["age"] > 21:
        print(students[i]["name"])


# Nested dictionary with condition and multiple values

students = {
    "student1": {
        "name": "Siddhant",
        "age": 22,
        "branch": "CSE(AIML)"
    },
    "student2": {
        "name": "Rahul",
        "age": 20,
        "branch": "CSE"
    },
    "student3": {
        "name": "Amit",
        "age": 24,
        "branch": "IT"
    }
}


for i in students:
    if students[i]["age"] >= 21:
        print(f'Name: {students[i]["name"]}\nBranch: {students[i]["branch"]}\n')