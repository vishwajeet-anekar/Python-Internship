# from functools import reduce
# def func1(x):
#     return x **2
# demo = [10,11,1,2,3,4,5,6,7]
# l1 = []
# for i in demo:
#     l1.append(func1(i))
# print(l1)

# map is used to apply a function to all items in a list
# ans = list(map(lambda a : a**2 ,demo))
# print(ans)

# def a (**kwargs):
#     return ' '.join(kwargs.values())

# print(a(name='vishwajeet', age='22', city='pune'))
# def a (n):
#     return n> 4
# ans2 = list(filter(a,demo))
# print(ans2)


# ans3 = list(filter(lambda x : x%2==0,demo))
# print(ans3)

# ans4 = reduce(lambda x,y:x+y , demo)
# print(ans4)


#global vs Local
# l1 = []
# inp1 = input('enter any number')
# l1 = [int(element) for element in inp1.split()] 
# print(l1)

# ans = [demo for demo in l1 if demo % 2==0]
# print(ans)

# a = []
# inp2 = input('Numbers')
# demo = inp2.split()
# for i in demo:
#     a.append(int(i))
# print(a)

# for i in range(2,5):
#     for j in range(1,11):
#         if i == j:
#             break
#         print(i, "*" ,j,"=" ,i*j)
# #mehtod to accept int in the list

# n = list(map(int,input('Numbers:- ').split()))
# print(n)

# ans = []
# n1 = input('D')
# ans = [int(d) for d in n1.split()]
# print(ans)

demo ={
    'name' : 'vishwajeet',
    'class': 'MCA',
    'Id' : 1001
}

print(demo)

print(demo.keys())
print(demo.values())

demo['occupation']='Software Dev'
print(demo)

del demo['occupation']
print(demo)
