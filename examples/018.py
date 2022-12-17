# Operatory logiczne - and

print( True and True ) # zwraca True
print( True and False ) # zwraca False
print( False and False ) # zwraca False

print( 8 > 3 and 3 == 3 ) # True bo obie strony zwracają True
print( 4 >= 4 and 1 >= 10 ) # False
print( 10 == 5 and 3 < 1 ) # False

if 5 == 5 and 10 > 4:
    print("true bo oba warunki spełnione")



# Operatory logiczne - or

print( True or True) # True
print( True or False ) # True
print( False or False ) # False

print( 10 > 1 or 7 == 7 ) # True
print( 3 < 5 or 1 > 3 ) # True
print( 10 == 11 or 2 < 1 ) # False

if "Ania" == "Ania" or 10 == 1:
    print("Ania to Ania")



# Operatory logiczne - not

print( not True ) # False
print( not False ) # True

print( not ( 10 == 10) ) # False
print( not ( 4 < 1) ) # True
print( not ( 5 == 5 and 3 > 1) ) # False

taskCompleted = False # zadanie nie było skończone

if not taskCompleted:
    print("Zadanie nie zostało wykonane")