# Operatory tożsamości (identity operators) - is, is not

a = [1,2,3,4,5]
b = [1,2,3,4,5]

print( a is b ) # False
print( a is a ) # True
print( b is b ) # True

print( a is not b ) # True
print( a is not a ) # False