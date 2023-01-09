#funkcja odwrotna do funkcji zadanej słownikiem f1

def inverse_func(f1):
    f2 = {}
    for i in range(len(f1)):
        f2[f1[i]] = i
    return f2

def superposition(f1, f2):
    return {i:f1[f2[i]] for i in range(10)}

f3= {1:2, 2:3, 3:4, 4:5, 5:0, 0:1}
f4= {0:3, 1:4, 2:5, 3:5, 4:3, 5:2, 6:1, 7:2, 8:3, 9:1}

print(inverse_func(f3))
print(superposition(f3,f4))

f5= {i:i**2 for i in range(20)}
f6= {i**2:i**3 for i in range(20)}

print(superposition(f6,f5))