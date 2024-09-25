# Variable are not statically typed in python
# You can assign a value to it in the beginning
x = "Hey, I am string"
print(x)
print(type(x))
# and then change its values in the later half to a different data type
x = 10
print(x)
print(type(x))


# You can compare python objects, and it is weird for example
y = [1,2,3,4,5]
z = [1,2,3,4,5]
print("Are these values same", y == z)


## Python naturally convert the data type to have more precision
num_1 = 123
num_2 = 1.23

num_3 = num_1+num_2
print(num_3,type(num_3))

## Exceptions
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass
## Correct order for the except clause
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
## Changing the order for the except clause
for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")
