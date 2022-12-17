# Informacje przekazywane do funkcji - parametr czy argumenty?

# Parametr to zmienna wewnątrz nawiasów okrągłych w definicji funkcji, poniżej w definicji funkcji sum są dwa parametry a oraz b

def sum(a, b):
    return a + b


# Argument to wartość przesłana do funkcji, gdy jest wywołana, poniżej 10 oraz 5 to właśnie przesłane arguemnty:

sum(10, 5) # da 15



# Przekazywanie wartości do funkcji w postaci parametrów - mutable vs immutable

# Niemutowalne

f = 3.2 # niemutowalne
addr1 = id(f)

f = f + 2.5
addr2 = id(f)

print(addr1)
print(addr2)
print(addr1 == addr2)


# Mutowalne

listData = ['a','b'] # mutowalne
addr1 = id(listData)

listData += ['c','d']
addr2 = id(listData)

print(addr1)
print(addr2)
print(addr1 == addr2) # True!



# Niemutowalny

def addToStr( string ):
    string += "!"
    print( "addToStr() string jako:" + string )

string = "Hello"

addToStr(string)
addToStr(string)
addToStr(string)

print("oryginalny: " + string)



# Mutowalny

def addToList( someList ):
    someList.append(4)

listData = [2]

addToList(listData)
addToList(listData)
addToList(listData)

print("ostateczna lista: " + str(listData) )



# Lista jest mutowalna, ale co jeśli wewnątrz funkcji przypiszemy do niej nową listę?

def addToList( someList ):
    print("someList przed zmianą: " + str(someList))
    someList = [30,40,50]
    print("someList po zmianie: " + str(someList))

listData = [2]

# przypisanie nowej listy w funkcji
# nie zmienia listData!
addToList(listData)

print("ostateczna lista: " + str(listData) )