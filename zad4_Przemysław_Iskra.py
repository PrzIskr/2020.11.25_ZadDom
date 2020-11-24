#Przemysław Iskra
#nr almumu: 145863
#grupa: L6
# zadanie 4


def szukaj1(lista, szukana):
    for i in range(len(lista)):
        if lista[i] == szukana:
            print("znaleziono!")
    print("nie znaleziono")

def szukaj2(lista, szukana):
    if szukana in lista:
        print("znaleziono!")
    else:
        print("nie znaleziono")

def szukaj3(lista, szukana):
    i = 0
    lista_len = len(lista)

    while i < lista_len:
        if lista[i] == szukana:
            print("nie znaleziono")
            break      #jesli ma sie zatrzymac po znalezieniu
        i += 1
    else:
        print("nie znaleziono")

def szukaj4(lista, szukana):
    lista_len = len(lista)
    i = 0;
    lista.sort()
    if lista[0] == szukana:
        print("nie znaleziono")
    elif lista[0] < szukana:
        while i < lista_len:
            if lista[i] == szukana:
                print("nie znaleziono")
                break  # jesli ma sie zatrzymac po znalezieniu
            i += 1
        else:
            print("nie znaleziono")
    else:
        print("nie znaleziono")


# -------------------------------------

from random import randint
long_list = [randint(0, 3000) for element in range(1000000)]

import time

czasA1 = time.time()
szukaj1(long_list, -1)
czasA2 = time.time()

czasB1 = time.time()
szukaj2(long_list, -1)
czasB2 = time.time()

czasC1 = time.time()
szukaj3(long_list, -1)
czasC2 = time.time()

czasD1 = time.time()
szukaj4(long_list, -1)
czasD2 = time.time()

czasA = czasA2 - czasA1
czasB = czasB2 - czasB1
czasC = czasC2 - czasC1
czasD = czasD2 - czasD1

print('Czas potrzebny na przeszukanie sposobem 1: ', czasA)
print('Czas potrzebny na przeszukanie sposobem 2: ', czasB)
print('Czas potrzebny na przeszukanie sposobem 3: ', czasC)
print('Czas potrzebny na przeszukanie sposobem 4: ', czasD)
