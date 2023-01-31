thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset.add("banana")
thisset.discard("banana")
print(thisset)

thisset.add("banana")
x = thisset.pop()
print(x)
print(thisset)
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)