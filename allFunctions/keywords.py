# we can declare a global variable by using a glabal keyword within the function
# nonlocal keyword is used within the nested function to access the parent keyword
a = 10
b = 20
def demo():
    a = 11
    print(a)
    def demo2():
        nonlocal a
        print(a)
    demo2()
    
print(a)
demo()
