# Typ danych w Python

info = 10
print(type(info)) # <class 'int' > - inforamcje o type danych integer - liczba całkowita

info = "Hello"
print(type(info)) # <class 'str'> inforamcje o typie danych string - ciąg znaków



# Liczby całkowite, zmiennoprzecinkowe, zespolone

# Liczba całkowita, dodatnia lub ujemna bez części dziesiętnej, może być to dowolnie duża liczba
number = 10 # liczba całkowita
print(type(number)) # <class 'int'>


# Liczba zmiennoprzecinkowa tzw. float, to liczba rzeczywista czyli ma część całkowitą i ułamkową po kropce
x = 3.14 # liczba zmiennoprzecinkowa
print(type(x)) # <class 'float'> informacje o typie danych float - liczba zmiennoprzecinkowa


# Liczba zespolona (complex) będąca sumą części rzeczywistej oraz urojonej (oznacza dodatnią literę "j"), obie przechowywane jako liczby float
complexNum = 10 + 3j
print(type(complexNum)) # <class 'complex'> informacje o typie danych complex - liczby zespolone