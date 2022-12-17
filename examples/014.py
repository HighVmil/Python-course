# Mutowalność vs niemutowalność

a = 1
b = 2

print( id(a) )
print(id(b) )
print( id(a) == id(b) ) # False, bo dwa różne miejsca w pamięci



# Mutowalność vs niemutowalność

a = 1
addr1 = id(a)

a += 1 #zwoększa a o 1
addr2 = id(a)

print(addr1)
print(addr2)
print(addr1 == addr2) # False



# Mutowalność vs niemutowalność

# 1 - Obiekty niemutowalne
f = 3.2
addr1 = id(f)

f = f + 2.5
addr2 = id(f)

print(addr1)
print(addr2)
print(addr1 == addr2)


# 2
s = "Hello"
addr1 = id(s)

s = s + "world!"
addr2 = id(s)

print(addr1)
print(addr2)
print(addr1 == addr2)


# 3
t = (0,1,2,3)
addr1 = id(t)

t = t + (4,5)
addr2 = id(t)

print(addr1)
print(addr2)
print(addr1 == addr2)



# Mutowalność vs niemutowalność

# 1 - Obiekty mutowalne
listData = ['a','b']
addr1 = id(listData)

listData += ['c','d']
addr2 = id(listData)

print(addr1)
print(addr2)
print(addr1 == addr2)


# 2
setData = {5,6}
addr1 = id(setData)

setData.add(7)
print(setData)
addr2 = id(setData)

print(addr1)
print(addr2)
print(addr1 == addr2)


# 3
dictData = {"a":0, "b":1}
addr1 = id(dictData)

dictData["c"] = 2
print(dictData)
addr2 = id(dictData)

print(addr1)
print(addr2)
print(addr1 == addr2)