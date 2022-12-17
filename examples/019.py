# Operatory przynależności - in, not in

data = [1,2,3,4,5,6]

# zwraca true jeśli element jest w liście
print( 0 in data ) # False
print( 5 in data ) # True

print( "Ola" in ("Ania", "Ola", "Kasia") ) # True

# not in zwraca true jeśli nie ma elementu w sekwencji danych
print( 12 not in data ) # True
print( 2 not in data) # False