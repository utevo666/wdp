
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

#1. Napisz program, który wczyta z klawiatury liczbę zmiennoprzecinkową i używa- jąc prostej instrukcji warunkowej wypisze na ekran wartość bezwzględną tej liczby. W tym programie nie należy używać funkcji wbudowanej abs.

liczba = float(input("Podaj liczbę zmiennoprzecinkową: "))

if liczba < 0:
    bezwzgledna = -liczba
else:
    bezwzgledna = liczba

print(f"Wartość bezwzględna liczby: {bezwzgledna}")

#2. Napisz funkcję sgn(x), która zwraca znak (inaczej: signum) swojego argumentu.(Znak liczby dodatniej jest równy 1, znak liczby ujemnej jest równy -1, a znak liczby
#0 jest równy 0.) W funkcji main wczytaj liczbę zmiennoprzecinkową, a następnie
#wypisz na ekran jej znak.


def sgn(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def main():
    liczba = float(input("Podaj liczbę zmiennoprzecinkową: "))
    znak = sgn(liczba)
    print(f"Znak liczby {liczba} to: {znak}")

main()

#3. Napisz program, który wczyta dwie liczby zmiennoprzecinkowe, a następnie wypisze
#wynik z dzielenia pierwszej przez drugą, o ile druga liczba jest różna od zera. Jeżeli
#dzielenie nie będzie możliwe, to należy wypisać na ekran odpowiedni komunikat.

liczba1 = float(input("Podaj pierwszą liczbę zmiennoprzecinkową: "))
liczba2 = float(input("Podaj drugą liczbę zmiennoprzecinkową: "))

if liczba2 != 0:
    wynik_dzielenia = liczba1 / liczba2
    print(f"Wynik dzielenia {liczba1} przez {liczba2}: {wynik_dzielenia}")
else:
    print("Nie można dzielić przez zero.")
    
#3. Napisz funkcję ile_ujemnych, która zwraca jako swój wynik liczbę ujemnych #elementów listy podanej jako jedyny argument tej funkcji. Przetestuj tę funkcję w #funkcji main.

def ile_ujemnych(lista):
    count = 0
    for element in lista:
        if element < 0:
            count += 1
    return count

moja_lista = [-1, 2, -3, 4, -5]
print(f"Liczba ujemnych elementów: {ile_ujemnych(moja_lista)}")

#Funkcja czy_nalezy(lista, element) => czy element należy do list, czy element jest w liście, np.: [5,3,1,4,2] i 4  => odpowiedź True

def czy_nalezy(lista, element):
    return element in lista

moja_lista = [5, 3, 1, 4, 2]
element_do_sprawdzenia = 4

wynik = czy_nalezy(moja_lista, element_do_sprawdzenia)
print(wynik)

#Funkcja czy_zawiera(lista1, lista2) => czy lista2 jest podzbiorem listy1, czy wszystkie elementy listy2 należą do listy1, np.: [5,3,1,4,2] i [3,2] => odpowiedź True

def czy_zawiera(lista1, lista2):
    return all(element in lista1 for element in lista2)


lista1 = [5, 3, 1, 4, 2]
lista2 = [3, 2]

wynik = czy_zawiera(lista1, lista2)
print(wynik)



napis = "abrakadabra"
usuwany = "ab"
def remove(napis, usuwany):
    print(napis.replace(usuwany,"",1))

remove(napis,usuwany)

def dzielniki(liczba):
    wynik = []
    for i in range(1,int(liczba / 2 + 1)):
        if liczba % i == 0:
            wynik.append(i)
    return wynik

print(dzielniki(50))

def suma(lista):
    wynik = 0
    for liczba in lista:
        wynik += liczba
    return wynik
print(suma([1,2,3,4,5]))


def czy_doskonala(liczba):
    dz = dzielniki(liczba)
    su = suma(dz)
    return su == liczba

print(czy_doskonala(100))
