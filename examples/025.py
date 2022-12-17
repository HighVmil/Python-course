# for - pętla

listData = [1,2,3,4] # iteracja listy
for v in listData:
    print(v)


tupleData = ("one", "two", "three") # iteracja krotki
for v in tupleData:
    print(v)


setData = {3,2,1} # iteracja zbioru
for v in setData:
    print(v)


strData = "Hello" # iteracja Stringa
for v in strData:
    print(v)


# iteracja słownika
dictionaryData = { "Ola" : "ola@example.com", "Ania" : "ania@example.com" }
for v in dictionaryData:
    print(v) # wyświetlanie kluczy słownika


# iteracja słownika, pokazanie wartości
dictionaryData = { "Ola" : "ola@example", "Ania" : "ania@example.com" }
for v in dictionaryData:
    print( dictionaryData[v] ) # wyświetlanie wartości słownika


#iteracja słownika
dictionaryData = { "Ola" : "ola@example", "Ania" : "ania@example.com" }
for key, value in dictionaryData.items():
    print(key, " : ", value) # klucz i wartość


# iteracja słownika
dictionaryData = { "Ola" : "ola@example", "Ania" : "ania@example.com" }
for key in dictionaryData.keys():
    print( key ) # wyświetlanie klucza


# iteracja słownika
dictionaryData = { "Ola" : "ola@example", "Ania" : "ania@example.com" }
for value in dictionaryData.values():
    print( value ) # wyświetlanie wartości


# iteracja słownika
dictionaryData = { "Ola" : "ola@example", "Ania" : "ania@example.com" }
for value in dictionaryData.values():
    print( value ) # wyświetlanie wartości
else:
    print( "for loop ended" )