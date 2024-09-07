s={10,20,30}
for a in s:
    print(a)

# print(s[2]) # error: set does not support indexing


s = {10,20,30}
s.add(40)
print(s)

l=[10,20,30,40,20]

s=set(l)
print(s)
s.add(50)
print(s)
s.pop()
print(s)
s.remove(50)
print(s)
s.discard(50)
print(s)
# s.clear()
# print(s)
s.update(l)
print(l)

