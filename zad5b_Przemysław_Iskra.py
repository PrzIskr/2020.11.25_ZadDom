#Przemysław Iskra
#nr almumu: 145863
#grupa: L6
# zadanie 5b

list_len = 5
from random import randint

rand_list = [randint(1, 10) for element in range (list_len)]

for randoms in rand_list:
    print(randoms)
