#Przemysław Iskra
#nr almumu: 145863
#grupa: L6
# zadanie 6

import copy
di = {'one': [1], 'two': [2], 'three': [3], 'four': [4]}
#diCopy = di.copy() # kopiowanie plytkie tworzy refrencje do oryginalu w kopii
diCopy = copy.deepcopy(di)

print(di)
print(diCopy)

di['four'][0] = 'cztery'

print(di)
print(diCopy)