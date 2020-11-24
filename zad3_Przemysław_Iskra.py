#Przemysław Iskra
#nr almumu: 145863
#grupa: L6
# zadanie 3

i = 3
slowo='ryba'

while i>0:
    i -= 1
    slowoU = input("Wprowadz slowo: ")
    if slowoU==slowo:
        print("Gratulacje! To bylo to slowo!")
        break
else:
    print("Przegrales. To nie bylo to slowo")