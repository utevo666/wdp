
suma = 0
for i in range(2,101,2):
    suma += i

print("Suma wszystkich liczb parzystych od 2 do 100 jest rowna:", suma)

suma_kwadratow = 0 
for i in range(1,101):
    suma_kwadratow += i**2
    
print("Suma wszystkich kwadratow od 1 do 101 jest rowna:", suma_kwadratow)

suma_poteg = 0 
for i in range(1,64):
    suma_poteg += 2**i

print("Suma wszystkich wykladnikow poteg od 1 do 63 jest rowna:", suma_poteg)

a = int(input("Podaj pierwsza liczbe:"))
b = int(input("Podaj druga liczbe:"))
suma_nieparzystych = 0 
if a > b:
    print("a > b wiec suma wynosi 0")
else:
    for i in range(a,b+1):
        if i % 2 != 0:
            suma_nieparzystych += i
print("Suma liczb nieparzystych miedzy a i b wynosi:", suma_nieparzystych)    
