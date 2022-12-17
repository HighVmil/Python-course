# Praca z czasem i datami

import time

ticks = time.time()
print(ticks) # np 1615215250.1979284 ilość sekund od 1.01.1970

timeData = time.localtime()
print(timeData)
print(timeData.tm_year) # rok 2021
print(timeData.tm_mon) # miesiąc 3 czyli marzec
print(timeData.tm_mday) # dzień miesiąca 8
print(timeData.tm_hour) # godzina 15
print(timeData.tm_min) # minuty 54
print(timeData.tm_sec) # sekundy 10
print(timeData.tm_wday) # dzień tygodnia od 0 do 6: 0 poniedziałek
print(timeData.tm_yday) # dzień roku od 1 do 366: 67
print(timeData.tm_isdst) # -1 oznacza, że Python zarządza czasem letnim itd: 0



# Praca z czasem i datami

# Do funkcji time.localtime() można przekazać również timestamp czyli ilość sekund od 01.01.1970:

# 0 sekund od 01.01.1970r
timeData = time.localtime(0)
print(timeData)


ticks = time.time()
print(ticks) # np 1615217257.9049973 ilość sekund od 1.01.1970
# Odjęcie jednej doby od aktualnego timestamp, zamiast 8 marca dane z 7 marca
timeData = time.localtime( ticks - (24 * 60 * 60))
print(timeData) # tm_mday=7



# Praca z czasem i danymi

# Funkcja time.asctime() formatuje w wygodny sposób datę i czas dostarczoną przez time.localtime()

# 1615217694.4971275
result = time.asctime( time.localtime(time.time()) )
print("Wynik:", result)


# Funkcja time.strftime() formatuje data i czas na string według podanego wzorca, korzysta z oznaczeń,
# które będą zastąpione konkretnymi wartościami w tekście: 
# %Y - rok, %m - miesiąc, %d - dzień, %H - godzina, %M - minuty, %S - sekundy

timeData = time.localtime() # aktualny czas
timeStr = time.strftime("%m/%d/%Y %H:%M:%S", timeData)
print(timeStr) # 10/12/2022 21:49:30



# Praca z czasem i datami

# Funkcja time.strptime() parsuje łańcuch znaków i tworzy z niego krotkę z datą i czasem

import time
timeStr = "08 March, 2025"
timeData = time.strptime(timeStr, "%d %B, %Y")
print(timeData)


# Funkcja time.sleep() usypia główny wątek programu na określoną ilość sekund

i = 0
while i < 10:
    time.sleep(1) # usypia wątek programu na sekundę
    print( time.asctime( time.localtime() ) )
    i += 1



# Praca z czasem i datami

# Pomiar czasu wykonywania programu
import time


# pomiar czasu wykonywania kodu
tStart = time.perf_counter()

time.sleep(0.1)

tEnd = time.perf_counter()


# measure wall time
interval = tEnd - tStart
print("Elapsed time: ", interval, "second") # Elapsed time:  0.10823860001983121 second



# Praca z czasem i datami - Praca z obiektem datetime

import datetime
datetimeObj = datetime.datetime(2021, 3, 8) # utworzenie obiektu datetime z daty
datetime = datetime.datetime(2025, 5, 30, 23, 59, 0)
datetimeObj = datetime.now() # aktualny czas i data
print("date(): ", datetimeObj.date() ) # 2021-03-08
print("time(): ", datetimeObj.time() ) # 18:12:32.246343
print("timestamp(): ", datetimeObj.timestamp() ) # 1615223552.246343
print("weekday(): ", datetimeObj.timestamp() ) # 0 poniedziałek od 0 do 6
print("today(): ", datetimeObj.today() ) # 2021-03-08 18:12:32.764959
print("year: ", datetimeObj.year ) # 2021
print("hour: ", datetimeObj.hour ) # 18
print("minute:", datetimeObj.minute ) # 12
print("second:", datetimeObj.second ) # 32
print("microsecond:", datetimeObj.microsecond ) # 246343
print("format: ", datetimeObj.strftime("%m/%d/%Y %H:%M:%S") ) # 03/08/2021 18:12:32



# Praca z czasem i datami - Daty łatwo porównywać jak np zwykłe liczby

import datetime
datetime1 = datetime.datetime(2025, 5, 30, 23, 59, 0) # Year Month Day Hour Minute Second
datetime2 = datetime.datetime(2025, 5, 30, 23, 59, 10)

print( datetime1 > datetime2 ) # False
print( datetime1 < datetime2 ) # True
print( datetime1 == datetime2 ) # False
print( datetime2 == datetime2 ) # True

date1 = datetime.date(2019, 4, 16)
date2 = datetime.date(2020, 11, 3)

print( date1 > date2 ) # False
print( date1 < date2 ) # True
print( date1 == date2 ) # False
print( date2 == date2 ) # True