def firstFn(a):
    def secondFn(b):
        print(a)
        print(b)
        return a + b
    return secondFn

cl1 = firstFn(7)
cl2 = cl1(8)

print(cl1)
print(cl2)