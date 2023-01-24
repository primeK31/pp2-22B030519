x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() #output : Python is awesome; becouse x is global variable




x = "awesome"#global variab.

def myfunc():
  x = "fantastic"#local variab.
  print("Python is " + x)

myfunc() #outp. : Python is fantastic

print("Python is " + x) #outp.: Python is awesome
print("Python is " + x)



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
