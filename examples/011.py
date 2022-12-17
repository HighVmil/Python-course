# Konwersja typów - tuple() oraz list()

# Konwersja na krotkę
listData = [1, 2, 3, 4]

tupleData = tuple(listData) # z listy na krotkę
print(type(tupleData)) # <class'tuple'>

# Konwersja na listę
tuple2 = ("Ola", "Adam")
newList = list(tuple2) # krotka  na listę
print(type(newList)) # <class 'list'>



# Konwersje typów - set() oraz dict()

# Konwersja na set (nieuporządkowany zbiór unikalnyh wartości)
listData = [1, 2, 3, 1, 2, 5, 6, 7]
setData = set(listData) # list na set
print(type(setData)) # <class 'set'>
print(setData) # {1, 2, 3, 5, 6, 7}

frozensetData = frozenset(listData) # list na frozenset
print(type(frozensetData)) # <class 'frozenset'>

# Konwersja na słownik:
tupleData = (("Adam", "adam@example.com"), ("Ola", "ola@example.com"))
dictData = dict(tupleData) # krotki na słownik
print(type(dictData)) # <class 'dict'>
print(dictData) # v{'Adam': 'adam@example.com', 'Ola': 'ola@example.com'}
print(dictData["Ola"]) # ola@example.com