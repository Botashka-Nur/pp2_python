#Example 1
x = "great"

def myfunc():
  print("World is " + x)

myfunc()


#Example 2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Fanta is " + x)


#Example 3 
def myfunc():
  global x
  x = "Hard"

myfunc()

print("C++ is " + x)


#Example 4
x = "High"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)