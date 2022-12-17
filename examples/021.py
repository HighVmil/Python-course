# Operator konkatenacji - służy do łączenia łańcuchów znaków, list, zbiorów itd.

str = "Hello "
newStr = str + " World!"
print(newStr) # Hello World!

list1 = [1,2,3,4]

listData = list1 + [5,6]
print(listData) # [1, 2, 3, 4, 5, 6]

tuple1 = ("one", "two")
tuple2 = ("three",)
print(tuple1 + tuple2) # ('one', 'two', 'three')