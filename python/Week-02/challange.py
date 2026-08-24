# DICTIONARY  CHALLENGE


# Challenge 1

student = {
    "name": "Siddhant",
    "age": 21,
    "branch": "CSE(AIML)"
}

student.update({
    "city": "Kolhapur"
})

print(student["branch"])

student2 = student.copy()

student2["age"] = 25

student2.pop("city")

print(student)
print(student2)


# Challenge 2 — Nested Dictionary

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

        print(
            f"name:{students[i]['name']}\n"
            f"Branch:{students[i]['branch']}\n"
        )


# Challenge 3 — Find Highest Age

h_a = 0

for i in students:

    if students[i]["age"] > h_a:

        h_a = students[i]["age"]


for i in students:

    if students[i]["age"] == h_a:

        print(students[i]["name"], students[i]["age"])


# Challenge 4 — Count Students Age 22

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
    },

    "student4": {
        "name": "Rohit",
        "age": 22,
        "branch": "CSE(AIML)"
    }
}

count = 0

for i in students:

    if students[i]["age"] == 22:

        count += 1

print(count)


# Challenge 5 — Find CSE(AIML) Students

for i in students:

    if students[i]["branch"] == "CSE(AIML)":

        print(students[i]["name"])


# Challenge 6 — Count CSE(AIML) Students
# Age >= 21


count = 0

for i in students:

    if students[i]["branch"] == "CSE(AIML)" and students[i]["age"] >= 21:

        count = count + 1

print(count)