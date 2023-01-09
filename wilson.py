n = int(input('Wprowadź liczbę: '))
silnia_modulo = 1
for i in range(2, n):
    silnia_modulo = (silnia_modulo * i) % n
if silnia_modulo == (n-1): print("Liczba n jest liczbą pierwszą")
else: print("Liczba n nie jest liczbą pierwszą")
