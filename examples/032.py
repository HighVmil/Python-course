# Funkcje bezargumentowe - nie przyjmują argumentów

def printSomething():
    print("Some infromation!")

printSomething()
printSomething()
printSomething()



# Funkcje z argumentami - wymagają kolejności przekazanych argumentów

def showData(string, number):
    print(string + str(number))

# Łańcuch "Liczba: " będzie dostępny w funkcji jako zmienna string
# Liczba 10 będzie dostępna w funkcji jako zmienna number
showData("Liczba: ", 10) 

# gdy przekażemy dane w złej kolejności
# to zwykle skończy się to błędem
# showData(10, "Liczba: ") # błąd



# Domyślne wartości argumentów funkcji

def printUser(name, country = "unknow", email = "default@example.com"):
    print( "User: " + name + " from country: " + country + " and email: " + email)

printUser("Adam", "Poland", "adam@example.com") # nadpisane domyślne wartości

printUser("Ola") # wartości domyślne będą użyte w funkcji