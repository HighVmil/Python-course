# Praca na łańcuchach znaków

print( "Hello " + "World!" ) # konkatenacja Hello World!

# powtórzenie HelloHello
print( "Hello" * 2 )

string = "Hello"
print( string[1] ) # e
print( string[1:3] ) # zakres: el
print( "o" in string ) # True
print( "x" not in string ) # True

multiLine = ''' line 1
line 2
''' # tekst w wielu linikach

print( "some text".capitalize() ) # Some text
print( "ok ok ok".count("ok") ) # zalicza ilość ok: 3

# wycentrowanie tekstu do 10 znaków z *
# ***tekst***
print( "test".center(10, "*") )

print( "Hello world".endswith("world") ) # True
print("Hello World".startswith("Hel")) # True

# wyszukaj łańcuch, -1 jeśli nie ma lub pozycja w str
print( "Ala ma kota".find("ma") ) # ma jest pod 4 znakiem
print( "Ala ma kota".find("test") ) # -1 bo nie ma
# rfind() wyszukuje od końca
print( "Ola ma psa, Ola ma kota".rfind("Ola") ) # 12



# Praca na łańcuchach znaków

# likwiduje białe znaki od lewej
print( "\n \t   Test".lstrip() ) # "Test "
print( " Test \n \t ".rstrip() ) # " Test"

# kasuje białe znaki po obu stronach
print( " \n \t Test \n \t ".strip() ) # "Test"

# zamienia wystąpienie w łańcuchu na inny
# Kasia ma kota, Kasia ma psa.
print( " Ola ma kota, Ola ma psa.".replace("Ola", "Kasia") )

# wyszukuje od końca
print( "Ola ma psa, Ola makota".rfind("Ola") ) # 12

print("Hello World".startswith("Hel")) # True



# Praca na łańcuchach znaków

print( "1256346".isalnum() ) # True, łańcuch jest liczbą całkowitą
print( "1256346".isalpha() ) # False
print( "Test".isalpha() ) # True, łańcuch z znakami alfabetu
print( "Test 2".isalpha() ) # False, bo liczba

print( "test".islower() ) # True, bo małe litery
print( " \t ".isspace() ) # True, bo tylko białe znaki
print( "HELLO".isupper() ) # True, bo tylko wielkie litery

# łączymy łańcuchy w jeden string separatorem
print( "-".join( ["Ola", "Ania"] ) ) # Ola-Ania

print( len("str length") ) # 10
print( "HELLO World".lower() ) # hello world
print( "HELLO World".upper() ) # HELLO WORLD
print( "HELLO world!".swapcase() ) # hello WORLD!