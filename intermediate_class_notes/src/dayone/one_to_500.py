#!/usr/bin/env python3

s = 'hello'
delim = "#" * 20

#print id of s (memory address of s)
#"id" is unique among simultaneously existing objects
print(id(s))

#hex represenation of id
print(hex(id(s)))


#make copy of first 3 letters of s
t = s[:3]
print(t)

#make a copy of s
t = s[:]
print(t)

print(hex(id(t)))

print(id(s) == id(t))


intern_dict = {}

def myintern(s):
    if s in intern_dict:
        return intern_dict[s]
    intern_dict[s] = s
    return s

s = 'hello'
t = s[:3] + s[3:]

#s is not t
print(s is t)

u = myintern(s)

#u is s as we are interning
print (u is s)

#string operations don't intern because it will slow them down


print(delim)
print("s[:] is s -->")
print(s[:] is s)
print("for strings it is true because we instern")
print(delim)

s = [10, 20, 30]
print(" s -->")
print(s)
t = s[:]
print("making t as copy of list s")
print("t -->")
print(t)

s.append(40)
print(delim)
print(delim)

import os
print("os.listdir('notes') -->")
print(os.listdir('notes'))
print("reading  from notes/hamlet.txt -->")
f = open('notes/hamlet.txt')
print(f.readline())
print(f.readline())
f.close()

print(delim)
print(delim)
print(delim)

def f(x):
    global y
    y += 1
    return x + y
y = 10
print(f(100))
print(f(200))

y = 10
a,b = f(100), f(200)
#a = 112 b = 212
print(a,b)

y = 10
b, a = f(200), f(100)
#a = 211 b = 112
print(a,b)

print(delim)
print(delim)

os = ['mac', 'windows', 'linux', 'solaris']
users = ['tom', 'sue', 'mary']

print("using range and indexing -->")
for i in range(len(os)):
    print(os[i])

print(delim)

print("using exact element -->")
for s in os:
    print(s)

print(delim)

print("using range -->")
for i in range(len(os)):
    print(i, '-->', os[i])

print(delim)

print("using enumerate -->")
for i,s in enumerate(os):
    print(i, '-->', s)

print(delim)
print(delim)

minsize = min(len(os), len(users))

print("zip using range and minsize -->")
for i in range(minsize):
    print(users[i], '-->', os[i])

print(delim)

print("zip using zip function -->")

for s, n in zip(users, os):
    print(s, '-->', n)
print(delim)
