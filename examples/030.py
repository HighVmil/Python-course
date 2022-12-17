# definiowanie funkcji - return

def printList(listData):
    if len(listData) <= 3:
        # funkcja kończy działanie
        # jeśli lista ma mniej niż
        # 3 elementy
        return
    print(listData)
    # return na końcu jest opcjonalne
    # jeśli nie zwracana jest
    # konkretna wartość
    return

print(["a","b","c"])
printList(["a","b","c", "d", "e"])