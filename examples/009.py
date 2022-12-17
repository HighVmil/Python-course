# Set - zestaw to nieuporządkowany zbiór unikalnych wartości

set = {0, 4, 8, 12, 16}
set.add(20)
print(set) # {0, 16, 4, 20, 8, 12}

set.add(20) # wartość już jest, więc pominięta
set.add(24)
set.discard(8) # skasowanie wartości 8
print(set) # {o, 16, 4, 20, 24, 12}

# interowanie elementów w zestawie
for value in set:
    print(value)



# Frozenset - niemutowalny zestaw to nieuporządkowany zbiór unikalnyh wartości

set = {0, 4, 8, 12, 16}
set.add(20)

frozen = frozenset(set)
print(frozen) # {0, 16, 4, 20, 8, 12}

#frozen.add(24) # błąd! nie ma add ()

# interowanie elementów w zestawie
for value in frozen:
    print(value)