# Nazwane argumenty w funckji

def showData(string, number):
    print(string + str(number))

showData(string = "Liczba: ", number = 10) # Liczba 10
showData(number = 10, string = "Liczba: ") # Liczba 10



# Nazywane argumenty z wartościami domyślnymi w funkcji

def printUser(name, country = "unknow", email = "default@example.com"):
    print("User: " + name + " from country: " + country + " and email: " + email)

printUser(country = "UK", name = "Ania")
