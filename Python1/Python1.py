import random

print("Hello World!") #This is a comment

#This is a comment
if 5 > 2:
    print("Five is greater than two!")

"""
This is a comment
written in
more than just one line
"""

#Variables are containers for storing data values.
x = 5
y = "John"
print(x)
print(y)

"""
Variables do not need to be declared with any particular type, 
and can even change type after they have been set.
"""
a = 4       # x is of type int
a = "Sally" # x is now of type str
print(a)

"""
Casting
If you want to specify the data type of a variable, 
this can be done with casting.
"""
b = str(3)    # x will be '3'
c = int(3)    # y will be 3
d = float(3)  # z will be 3.0

e = 5
f = "John"
print(type(e))
print(type(f))

g = "John"
# is the same as
g = 'John'

#Case-Sensitive
a1 = 4
A1 = "Sally"
#A1 will not overwrite a1

#Multi Words Variable Names
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print(type(fruits))

#Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

"""
In the following,
notice the space character after "Python " and "is ", 
without them the result would be "Pythonisawesome".
"""
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Global Variables
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#Data Types
x = 1j
print(x)
print(type(x))

x = ("apple", "banana", "cherry")
print(x)
print(type(x)) 

x = range(6)
print(x)
print(type(x))

x = {"name" : "John", "age" : 36}
print(x)
print(type(x))

x = {"apple", "banana", "cherry"}
print(x)
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

x = True
print(x)
print(type(x))

x = b"Hello"
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))

x = None
print(x)
print(type(x))

#Numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

c = complex(x,y)
print(c)

print(random.randrange(1, 10))

#Use " or ' in the following
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))
print(a.split(" "))

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

