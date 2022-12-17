# Dict - słownik, z ang. dictionary

contacts = {

"Ania" : "ania@example.com",
"Daniel" : "daniel@example.com",
"Ola" : "ola@example.com"

}

contacts["Olek"] = "olek@example.com"

print(len(contacts)) # 4
print(contacts["Ania"]) # ania@example.comm
print(contacts["Olek"]) # olek@example.com

print(contacts.keys()) # klucze dostępne w słowniku
print(contacts.values()) # wartości dostępne w słowniku