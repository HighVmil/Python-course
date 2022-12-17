# Praca z słownikami

data = { "name" : "Kasia", "city" : "Waw" }
print( data["name"] ) # pobranie elementu z key name, Kasia
data["name"] = "Ola" # modyfikacja elementu

emailKey = "email"
data[emailKey] = "ola@example.com"
print(data) # {'name' : 'Ola', 'city' : 'Waw', 'email' : 'ola@example.com'}

del data["city"] # skasowanie elementu
print(data) # {'name' : 'Ola', 'email' : 'ola@example.com'}

data.clear() # skaowanie wszystkich elementów
print(data) # {}

data = { "name" : "Ola", "city" : "Waw" }
print( len(data) ) # długość słownika: 2 elementy



# Praca z słownikami

data = { "name" : "Kasia", "city" : "Waw" }
copy = data.copy() # tworzy płytką kopie słownika
print(copy) # {'name' : 'Kasia', 'city' : 'Waw'}

# tworzy słownik z podanymi kluczami, wartości jako None
# {'name' : None, 'email' : None, 'country' : None}
print(data.fromkeys( ("name", "email", "country") ))

# zwraca istniejącą wartość klucza lub drugi argument
print( data.get("postal code", "DEFAULT") ) # DEFAULT

print( "name" in data ) # czy klucz jest w słowniku, True

print( data.keys() ) # zwraca listę kluczy: name, city
print( data.values() ) # zwraca listę wartości: Kasia, Waw