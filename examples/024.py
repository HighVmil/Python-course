# while - pętla

number = 4

while number > 0:
    print(number)
    number = number - 1

print("Kod po pętli")



# while - pętla

num = 0
# pętla nieskończona
while( True ):
    print("Wprowadź w konsoli liczbę do dodania, exit aby zakończyć")
    strData = input() # odczyt danych od użytkownika
    if(strData == "exit"): break # wyjście z pętli jeśli spełniony warunek
    num += int(strData)
    print("Nowa wartość po dodaniu " + str(strData) + " jest " + str(num))

print("Ostateczna wartość po pętli: " + str(num))



# while - pętla z else

number = 0

while number < 3:
    print(number)
    number += 1
else:
    print("Warunek już jest niespełniony bo numer = " + str(number))