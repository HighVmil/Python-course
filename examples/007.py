# Tuples - krotki

data = ("one", "two", "three")
print(type(data)) # <class 'tuple'>
print(data) # ('one', 'two', 'three')

cars = "GMC", "Pontiac", "Ford";
print(type(cars)) # <class 'tuple'>

names = ()
print(type(names)) # <class 'tuple'>

fighters = ("F16",) # Krotka zawierająca jeden elementu musi mieć po nim przecinek, oznacza to, że checemy utworzyć krotkę, a nie ciąg znaków
print(type(fighters)) # <class 'tuple'>

data = ("one", "two", "three", "four", "five", "six")

print(data [1]) # two
print(data[1:4]) # 'two', 'three', 'four'
print(data[-1]) # six
print(data[-5]) # two

print(data[4:]) # ('five', 'six',) od czwartego elementu
print(data[::2]) # ('one', 'three', 'five') co drugi element

multiTuple = ((1, 2, 3,), data) # krotka wieowymiarowa, dwie krotki w jednej
print(multiTuple[0][1]) # 2

# data = ("one", "two", "three")
# data[1] = "test" # TypeError: 'tuple' object does not support item assignment

num1 = (1, 2, 3)
numbers = num1 + (4, 5, 6)
print(numbers)

print(10 in (5, 10, 15)) # True
for v in (1, 2, 3): print(v)

data = (1, 2, 3, 4)
print(data) # (1, 2, 3, 4)

# del data - skasowanie krotki za pomocą słowa kluczowego del
# print(data) # błąd!

# newData = (10, 20, 30)
# del newData[0] - wyskakuje błąd, próba skasowania elementu w krotce spowoduje błąd, gdyż jest niemutowalna 

numbers = (10, 20, 30, 40)
print(len(numbers)) # 4

names = tuple(("Asia", "Ania", "Amelia"))
print(type(names)) # <class 'tuple'>
print(names) # ('Asia', 'Ania', 'Amelia')

nums = (1, 2, 3) # wartości krotki, można wielokrotnie powtarzać
print(nums * 4) # (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)