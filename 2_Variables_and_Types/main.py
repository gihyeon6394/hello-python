## Numbers

myint = 7
print(myint)

myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

## Strings

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
mystring = "Don't worry about apostrophes"
print(mystring)

one = 1
two = 2
three = one + two
print(three)

karina = "karina"
isBeautiful = "is Beautiful"
karinaIsBeautiful = karina + " " + isBeautiful
print(karinaIsBeautiful)

karina, minzi = "karina", "minzi"
print(karina, minzi)

# TypeError: can only concatenate str (not "int") to str
# print(karina + one + "  " + minzi + two)

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
