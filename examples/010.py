# Konwersje typów - int()

floatNum = 12.3
print(type(floatNum)) # <class "float'>

intNum = int(floatNum) # konwersja float na int
print(intNum) # 12
print(type(intNum)) # <class 'int'>

x = int(5) # 5
y = int("32") # 32
print(type(y)) # <class 'int'>



# Konwersje typów - float()

intNum = 20
print(type(intNum)) # <class 'int'>

floatNum = float(intNum) # konwersja int na float
print(floatNum) # 20
print(type(floatNum)) # <class 'floats'>

f = float("76.789") # 76.789
print(f)
print(type(f)) # <class 'float>

# zła liczba w łańcuchu powoduje błąd
# float("123,23") # ValieErrpr: cloud not convert string to float: '123,34'



# Konwersje typóww - str()

str1 = str(intNum) # konwersja int na łańcuch znaków
print(str1) # 20
print(type(intNum)) # <class 'str'>

str2 = str(45.456)
print(str2)
print(type(str2)) # <class 'str'>

print("Rok  ma " + str(365) + " dni.") # Rok ma 365 dni.

# Błąd! TypeError: can only concatenate str (not "int") to str
# print("Rok ma" + 365 + "dni.")