#Tuple creation 
subjects=("Python","Big Data","ANN","MLT","Cloud Computing")
print(f"First Subject:{subjects[0]}")
print(f"last Subject:{subjects[-1]}")
print(f"Total Subjects:{len(subjects)}")
print(subjects[1:4])

#tuple unpacking
student=("Siddhant",20,"CSE(AIML)",7)
name,age,branch,fav_no=student
print(f"Name:{name}")
print(f"Age:{age}")
print(f"Branch:{branch}")
print(f"Favourite Number:{fav_no}")

# Tuple indexing, slicing, count and index

student = ("Siddhant", 20, "CSE(AIML)", 7, "Python")

print(student[1])
print(student[-1])
print(student[1:4])
print(len(student))

name, age, branch, fav_no, language = student

print(name)
print(language)

print(student.count("Python"))
print(student.index("CSE(AIML)"))

# Tuple immutability
numbers = (10, 20, 30)

# numbers[1] = 50   # TypeError: tuples cannot be modified


# Single-element tuple
single = (10,)

print(type(single))