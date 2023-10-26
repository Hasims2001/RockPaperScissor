print("Problem 1: Print the following pattern")
for i in range(1, 6):
    temp = ""
    for j in range(1, i+1):
        temp += str(j) + " " 
    print(str(temp))
print("\n")


print("Problem 2: Display numbers from a list using loop")
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if(num%5 == 0 and num <= 150):
        print(num)
    if(num > 500):
        break
print("\n")


print("Problem 3: Append new string in the middle of a given string")
s1 = input("s1 string:")
s2 = input("s2 string:")
s1Len = 0
for char in s1:
    s1Len += 1

s1Len = int(s1Len/2)
s3 = ""
for char in s1:
    s1Len -= 1
    s3 += char
    if(s1Len == 0):
        for i in s2:
            s3 += i
    
print("New String: ", s3)
print("\n")


print("Problem 4: Arrange string characters such that lowercase letters should come first")
s = input("String:")
lower = ""
upper = ""
for char in s:
    if(char.islower()):
        lower += char
    else:
        upper += char
print(lower + upper)
print("\n")


print("Problem 5: Concatenate two lists index-wise")
list1 = input("List1 values with space:").strip().split(" ")
list2 = input("List2 values with space:").strip().split(" ")
lists = []
ind = 0
for i in list1:
    if(ind < len(list2)):
        lists.append(i + list2[ind])
        ind += 1
    else:
        lists.append(i)

for i in range(ind, len(list2)+1):
    if(i < len(list2)):
        lists.append(list2[i])

print("New List:", lists)
print("\n")


print("Problem 6: Concatenate two lists in the following order")
list1 = input("List1 values with space:").strip().split(" ")
list2 = input("List2 values with space:").strip().split(" ")
lists = []
for item in list1:
    for i in list2:
        lists.append(item + i)
print(lists)
print("\n")


print("Problem 7: Iterate both lists simultaneously")
list1 = input("List1 values with space:").strip().split(" ")
list2 = input("List2 values with space:").strip().split(" ")
ind = -1
for item in list1:
    print(item, list2[ind])
    ind -= 1

print("\n")


print("Problem 8: Initialize dictionary with default values")
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
dist = {}
for emp in employees:
    dist.update({ emp : defaults})
print(dist)
print("\n")


print("Problem 9: Create a dictionary by extracting the keys from a given dictionary")
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

#Keys to extract
keys = ["name", "salary"]
dist = {}
for i in keys:
    dist.update({i : sample_dict.get(i)})
print(dist)
print("\n")


print("Problem 10: Modify the tuple")
tuple1 = (11, [22, 33], 44, 55)
print(tuple1)
tuple1[1][0] = 222
print(tuple1)
print("\n")
