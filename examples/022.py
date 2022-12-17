# if - instrukja warunkowa do podejmowania decyzji w programie

number = 10

if number > 6:
    print("number większe od 6")
    print("też się wyświetli jeśli number > 6")

if number == 2:
    print("number równe 2")



# if - bloki kodu oraz wcięcia

num = 12
if num > 5:
    print( str(num) + " większe od 5" )
    # instruke if można zafnieżdżać
    if num >= 10:
        print( str(num) + " większe też od 10" )
        if num > 20:
            print( str(num) + " większe też od 20")
    print("Ostatnie wcięcie instrukcji if")

print("Informacja niezależna od bloku kodu if")



# elif - jeśli instrukcja if nie spełnia warunku uruchomi kolejną po elif

num = 7

if num == 7:
    print("num jest 7")
elif num == 10:
    print("num jest 10")


num = 10

if num == 7:
    print("num jest 7")
elif num == 10:
    print("num jest 10")


num = 20

if num ==7:
    print("num jest 7")
elif num == 10:
    print("num jest 10")
elif num == 12:
    print("num jest 12")
elif num == 14:
    print("num jest 14")
elif num >= 15:
    print(" num jest większe równe 15")



# else - jeśli if oraz elif nie spełniają warunku to uruchomiony zostanie kod po else

a = 10
b = 5

if a == b:
    print("a równe b")
elif a < b:
    print("a < b")
else:
    print(" a > b")

# warto również wspomnieć, że można zapisać
# w jednej linijce kod do wykonania if
if a > b: print("a większe od b")