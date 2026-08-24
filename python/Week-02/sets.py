#creation of set
numbers={10,20,30,40,10,50}
print(numbers)
print(len(numbers))
#print(numbers[0])

#adding elements
number={10,20,30}
number.add(40)
print(number)

#set methods
numberss={10,20,30}
numberss.remove(20)
numberss.discard(50)
print(numberss)

#set looping and membership
numberrs={5,10,15,20,25}
for num in numberrs:
    print(num)
if 15 in numberrs:
    print("15 is present")

#set operations
#all
fruits={"Apple","banana","mango","apple"}
fruits.add("orange")
fruits.remove("banana")
print("mango" in fruits)
print(len(fruits))

#set operations
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print(A | B)
print(A & B)

A = {10, 20, 30, 40, 50}
B = {30, 40, 50, 60, 70}

print(A - B)
print(B - A)
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A ^ B)