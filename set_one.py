print("1. Hello, World!")
print("Hello, World!")
print("\n")


num = 50
numFloat = 3.14
str = "Hello!"
isTrue = True
List = [1, 2, "world", False]
Tuple = (1, 4, 10, 100)
Dist = {"key1" : "hi", "key2": 78}
Sets = {78, True, 1.2, "sets"}

print("2. Data Type Play")
print(type(num), "value:", num)
print(type(numFloat), "value:", numFloat)
print(type(str), "value:", str)
print(type(isTrue), "value:", isTrue)
print(type(List), "value:", List)
print(type(Tuple), "value:", Tuple)
print(type(Dist), "value:", Dist)
print(type(Sets), "value:", Sets)
print("\n")


print("3. List Operations")
opr = [ 7, 8, 9, 10, 1, 2, 3, 4, 5, 6]
print("List:", opr)
opr.append(11)
print("after add:", opr)
opr.remove(6)
print("after deleting 6:", opr)
opr.sort()
print("after sort:", opr)
print("\n")


print("4. Sum and Average")
value = input("Enter num with space: ")
value = value.strip().split(" ")
sum = 0
count = 0
for num in value:
    sum += int(num)
    count += 1

print(sum, sum/count)
print("\n")


print("5. String Reversal")
str =  input("Enter String: ")
print(str[::-1])
print("\n")


print("6. Count Vowels")
str = input("Enter String: ")
count = 0
for char in str:
    if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        count += 1
    
print("Total Vowels:", count)
print("\n")

print("7. Prime Number")
num = int(input("Num: "))
if(num == 1):
    print("1 is not prime number")
else:
    flag = False
    for i in range(2, int(num/2)):
        if(num%i == 0):
            flag = True
            break
    if(flag): 
        print(num, "is not prime number")
    else:
        print(num, "is a prime number")
print("\n")


print("8. Factorial Calculation")
num = int(input("Num: "))
fact = 1
for i in range(1, num+1):
    fact = fact*i

print("Factorial:", fact)
print("\n")


print("9. Fibonacci Sequence:")
num = int(input("Num: "))
fib = [0, 1]
for i in range(3, num+1):
    fib.append(fib[-1] + fib[-2])

print("Fibonacci Sequence:",fib)
print("\n")


print("10. List Comprehension")
comp = []
for i in range(1, 11):
    comp.append(i*i)
print("List Comprehension:",comp)
print("\n")

