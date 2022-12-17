# Łańcuchy znaków

str = "Hello!"
print(str) # Hello!
print(type(str)) # <class 'str">


# Na łańcuchu można wykonywać pewne operacje:
print( str[0] ) # wybranie pojedyńczego znaku: H
print( str[1:4] ) # ell - wybranie znaków od do - wybiera znak nr 2, bo zaczyna sie liczenie od 0, ale nie liczy juz znaku nr 4, tylko do jednego przed
print( str * 3 ) # Hello!Hello!Hello! - powtórzenie łańcuchu 3 razy
print( str + "Everyone" ) # Hello! Everyone! - łączenie łańcuchów dzięki kombinacji +

print("Szkolenie Python'a") # W cudzysłowie można używać apostrofy lub odwrotnie



# Łańcuchy znaków w wielu liniach, bloki tekstu

str = """ Pewien tekst
Kontynuacja tekstu w nowej lini
i jeszcze jedna"""
print(str)

text = ''' Następny tekst
w apostrofach'''
print(text)



# Łańcuchy znaków - znaki nowej linii, tabulacja, znaki specjalne

# \n - znak nowej lini
# \t - znak tabulacji

str = "Pierwsza linia\nDruga linia \t oraz tabulacja \n trzecia linia"
print(str)


# Użycie backslasha czyli znaku ucieczki pozbawia specjalnego znaczenia znaku specjalnego, dzięki czemu staje się zwykłym znakiem:
text = "Używanie cudzysłowu w łańcuchu znaków jest \"możliwe\" stosując ukośnik "
print(text)