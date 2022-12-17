# Kontrola przebiegu pętli - break

data = [0,1,2,3,4,5,6,7]

for v in data:
    if v == 3:
        break
    print(v)

print("Dalsza część programu")



# Kontrola przebiegu pętli - continue

data = [0,1,2,3,4,5,6,7]

for v in data:
    if v == 3:
        continue
    print(v)

print("Dalsza część programu")



# Instrukcja pass

if 40 > 6:
    pass
else:
    pass