#/usr/bin/env python3

delim = "#" * 20

class MyDualException(KeyError, ValueError):
    #used to raise 2 exceptions at once
    pass

def f(x):
    print("working on function f")
    raise MyDualException(x)
    print("done working on f")

try:
    print("hello from try")
    f(10)
    print("goodbye from try")
except KeyError:
    print("caught KeyError")

print(delim)

try:
    f(10)
except ValueError:
    print("checking if f throws ValueError")

print(delim)

try:
    f()
except (LookupError, ValueError) as e:
    print("Yippeee")
    print("the args are", e.args)
except TypeError:
    print("Found a type error as not calling f with arg")
    try:
        f(10)
    except KeyError as e:
        print("this is a nested exception.", e.args)
finally:
    print("this runs always as it is under finally")

print(delim)
print(delim)

try:
    l = [1, 2, 3]
    g = l[1]
except IndexError as e:
    print("got into IndexError. Not handling it")
    print("e args -->", e.args)
else:
    print("no exception was raised. Peaceful!!")

print(delim)
#LBYL Look before you leap
import os

f = open("tmp.txt", "w")
f.write("0 to 9\n")
f.write(str(list(range(10))))
f.close()

f = open("tmp.txt", "r")

while True:
    try:
        print(next(f))
    except StopIteration as e:
        print(e.args)
        f.close()
        break

if os.path.exists("tmp.txt"):
    print("removing tmp.txt LBYL Method")
    os.remove("tmp.txt")

print(delim)

#EAFP Easy to ask for forgiveness than permission
try:
    print("removing tmp.txt. Not checking if it exists beforhand")
    os.remove("tmp.txt")
except OSError:
    pass

print(delim)
'''
if 1:
    print("hello")
    errcode = f(10)
    print("errcode = ", errcode)
    if errcode:
        goto(handlers)
    print("goodby")

handlers:
    if errcode:
        if isinstance(errcode, LookupError) or isinstance(errcode, IndexError):
            print("Yippee!")
        elif isinstance(errcode, KeyError):
            print("caught keyerror")
        elif isinstance(errcode, IndexError):
            print("caught IndexError bu not handling it")
            raise
    else:
        print("No error")

'''


print("--- for else demo ---")
l = [3,3,4]
print("l --> ", l)

for i in l:
    print(i)
else:
    print("else is always executed after the iteration")

print(delim)

print("--- try else demo ---")
try:
    print("trying to get l[len(l)]")
    l[len(l)]
except StopIteration as e:
    print(e)
except IndexError:
    print("catching index error")
else:
    print("Handled on StopIteration lets see if we get it")
    print("we get this error if no exception are raised or caught")

finally:
    print("this(finally) is always executed")

print(delim)
try:
    print("trying to get l[len(l) - 1] which is valid")
    l[len(l) - 1]
except StopIteration as e:
    print(e)
except IndexError:
    print("catching index error")
else:
    print("Handled on StopIteration lets see if we get it")
    print("inside else")
    print("we get this error if no exception are raised or caught")
finally:
    print("this(finally) is always executed")
print(delim)
