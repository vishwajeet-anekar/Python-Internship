# If-else statement
num = int(input("Enter a number: "))

if num >= 0:
    print("The number is positive")
else:
    print("The number is negative")

# For loop
#list using for loop
a = []
inp2 = input('Numbers')
demo = inp2.split()
for i in demo:
    a.append(int(i))
print(a)

# list comprehension
l1 = []
inp1 = input('enter any number')
l1 = [int(element) for element in inp1.split()] 
print(l1)

# list compr with filter
ans = [demo for demo in l1 if demo % 2 ==0]
print(ans)


for i in range(1, 6):
    print(i)

# While loop
i = 1
while i <= 5:
    print(i)
    i += 1

# Break statement
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Continue statement
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Pass statement
for i in range(1, 6):
    pass
    print(i)

#printing tables from 2 -4 
for i in range(2,5):
    for j in range(1,11):
        print(i, "*" ,j,"=" ,i*j)
        
for i in range(2,5):
    for j in range(1,11):
        if i == j:
            break #continue
        print(i, "*" ,j,"=" ,i*j)