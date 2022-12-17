# Praca z krotkami

tup1 = (0,1) + (2,3) + (4,) # konkatenacja
print(tup1) # (0, 1, 2, 3, 4)
print( type(tup1) ) # <class 'tuple'>

print( (1,2) * 3 ) # (1, 2, 1, 2, 1, 2)
print( 4 in tup1 ) # True
print( len(tup1) ) # 5

print( tup1[2] ) # 2
print( tup1[2:5] ) # zakres (2,3,4)

# tup1[3] = 4 # błąd 'tuple' object does not support item assignment
# del tup1[2] # błąd 'tuple' object dosen't support item deletion

for x in tup1:
    print(x)

print( min(tup1) ) # 0
print( max(tup1) ) # 4
print( tuple( [3,4,5] ) ) # lista na krotkę