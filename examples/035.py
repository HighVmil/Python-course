# Scope zasięg zmiennych - zmienne lokalne

number = 20

def printNumber():
    print(number) # dostęp do zmiennej globalnej, ponieważ nie ma takiej w funkcji
    string = "test" # zadeklarowana zmienna lokalna
    print(string)

printNumber()
# id(string) # brak dostępu do string, bo jest zmienną lokalną funkcji



# Scope zasięg zmiennych - zmienne globalne

number = 12 # zmienna globalna

print(number) # 12

if number > 0:
    print(number) # instrukcja if ma dostęp do zmiennej globalnej

def printNum():
    print(number) # funkcja ma dostęp do globalnej zmiennej



# Scope zasięg zmiennych - zmienne lokalne przesłaniające globalne

number = 20

def printNumber():
    number = 6 # deklaracja zmiennej lokalnej o tej samej nazwie przesłania globalną
    print("number: ", number) # odwołanie po number odnosi się do lokalnej zmiennej

printNumber()



# Scope zasięg zmiennych - arguemnty przesłaniające globalne

string = "Hello"

def printData(string) :
    print(2, string) # zmienna jako argument przesłania globalną o tej samej nazwie

print(1, string) # 1 Hello
printData("Test")



# Scope zasięg zmiennych - wywołanie funkcji w funkcji

string = "Hello"

def showInfo() :
    print(3, string) # Uwaga, odwołanie do zmiennej globalnej!: 3, Hello

def printData():
    string = "Test" # zmienna lokalna przesłania globalną
    print(2, string) # 2, Test
    showInfo() # wywołanie funkcji showInfo()

print(1, string) # Hello
printData()



# Scope zasięg zmiennych - definicja i wywołanie funkcji w funkcji

firstNum = 9

def test():
    firstNum = 1
    print("test() firstNum:", firstNum)
    def bar():
        print("bar() firstNum:", firstNum)
    bar()
    print("end test()")

print("global firstNum:", firstNum)
test()



# Scope zasięg zmiennych - słowo kluczowe global pozwalające na zmianę zmiennej globalnej

number = 20

def printNumber():
    # nie modyfikujemy globalnej tylko
    # tworzymy lokalną zimienną
    number = 33 # nie zmieni globalnej
    print("doNumber(): ", number)

printNumber()
print("global number", number)


number = 20

def printNumber():
    global number   # number wskazuje
                    # na globalną
    number = 33     # modyfikacja
                    #globalnej!
    print("doNumber(): ", number)

printNumber()
print("global number", number)



# Instrukcja if - nie definiuje zasięgu, podobnie jak pętle i try / except

strint = "Hello"

if 1 == 1:
    print(1, string) # Hello
    if 2 == 2:
        string = "Test" # zmiana globalnego string
        print(2, string) # 2, Test
        if( 3 == 3):
            print(3, string) # 3, Test

print(4, string) # 4 Test



# instrukcja if - nie definiuje zasięgu, podobnie jak pętle i try / except

string = "Hello"

def testFunc():
    string = "Local Hi"
    if 1 == 1:
        print(1, string) # 1 Local Hi
        if 2 == 2:
            string = "Test" # zmiana string wewnątrz funkcji! 
            print(2, string) # 2 Test
            if( 3 == 3):
                print(3, string) # 3 Test
    print(4, string) # 4 Test

testFunc()
print(5, string) # 5 Hello



# Instrukcja if - nie definiuje zasięgu, podobnie jak pętle i try / except

if 1 == 1:
    data = "some data" # zdefiniowanie zmiennej, tutaj globalnej

print(data) # some data

if 2 == 1:
    info = 10

# print(info) # błąd name info is not defined