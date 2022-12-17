# Definiowanie funkcji

a = 2
b = 4

def addNumbers(num1, num2):
    result = num1 + num2
    return result

c = addNumbers( a, b )
print(c) #6

d = addNumbers(c, 10)
print(d) #16



# Definiowanie funkcji - kolejne przykłady

def addNum(a,b):
    return a + b

def subNum(num1, num2):
    result = num1 - num2
    return result

value1 = addNum(10, 5) # 15
value2 = subNum(value1, 9) #6
print( value1 ) # 15
print( value2 ) # 6
print( subNum(100, addNum(12, 18)) ) # 70

# suma koszyka zakupów
def calcBasketValue(basketList):
    basketSum = 0
    for key in basketList:
        basketSum += basketList[key]
    return basketSum

shoppingBasket = {
    "smartphone" : 1200,
    "TV" : 1500,
    "console" : 1500
}

print( calcBasketValue (shoppingBasket) )