def horner_algorythm(stopien, lista, x):
    b = lista[stopien]
    for i in range(1, stopien+1):
        b=b*x+lista[i-1]
    return b

print('Podaj stopień wielomianu')
n = int(input('n = '))
a = []
for i in range(n+1):
    print("Wprowadź współczynnik",i, 'wielomianu')
    a.append(int(input()))
x = float(input("Wprowadź wartość x "))
print(horner_algorythm(n, a, x))