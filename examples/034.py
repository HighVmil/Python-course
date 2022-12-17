# Ograniczenie sposobu przekazywania danych do funkcji - programista za pomocą / oraz * może 
# określić dopuszczalne sposoby przekazywania argumentów do funkcji

def printData(string, number = 10, /):
    print(string, number);

printData("Test", 5) # działa prawidłowo, argumenty pozycyjne: Test 5

# printData(string = "Test", number = 11) # błąd nie można używać argumentów nazwanych



def printData(*, string, number = 10):
    print(string, number);

printData(string = "Test", number = 11) # działa prawidłowo: Test 11

# printData("Test", 5) # błąd, oba mają być przekazane jako nazwane



# parametry po gwiazdce muszą być przekazane jako arguemnty nazwane
# parametry przed gwiazdką mogą być przekazane jako nazwane albo pozycjyjne
def printData(float, bool, *, string, number = 10):
    print(float, bool, string, number);

printData(12.5, bool = True, string = "Test", number = 11) # 12.5 True Test 11
printData(float = 12.5, bool = False, number = 11, string = "Test") # 12.5 False Test 11
printData(20.3, False, number = 11, string = "Test") # 20.3 False Test 11