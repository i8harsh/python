def compose (functions):
def inner():
arg for f in reversed(functions):
arg = f(arg)
return arg
return inner
#Define three functions
def square (x):
return x*2
def increment (x):
return x + 1
def half (x):
return x / 2
