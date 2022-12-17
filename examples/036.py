# Wyrażenie lambda

sum = lambda a,b: a + b

print( sum(10,5) ) # 15
print( sum(4,3) ) # 7



# Zwrócona jest funkcja lambda, która zapamięta wartość n

def genFunc(n):
    return lambda a: a * n

doubler = genFunc(2) # w doubler jest lambda z n o wartości 2

print( doubler(5) ) # 10
print( doubler(7) ) # 14

tripler = genFunc(3)
print( tripler(2) ) # 6
print( tripler(3) ) # 9



# Wyrażenia lambda z map()

listData = [1,2,3,4,5]

result = map( lambda x: x * 2, listData )
print( list(result) ) # [2, 4, 6, 8, 10]

print(list(map(lambda x: x*3, [1, 2, 3, 4]))) # [3, 6, 9, 12]



# Wyrażenia lambda z filter()

listData = ["Ola", "Włodzimierz", "Kasia", "Izydor"]

# filtruje imiona, wybiera te które mają mniej niż 6 liter
result = filter(lambda x : len(x) <= 5, listData) # Output: [2, 4, 6]

print(list(result)) # ['Ola', 'Kasia']



# Wyrażenie lambda z reduce()

# Funkcja reduce redukuje sekwencję do pojedyńczej wartości:

from functools import reduce # import funkcji reduce

numSum = reduce((lambda x, y: x + y), [1, 2, 3, 4, 5])
print("Suma liczb:", numSum)