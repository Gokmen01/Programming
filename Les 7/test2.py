try:
    print("geef getal onder de 10")
    waarde = int(input())
    print("De ingevoerde waarde is " + str(waarde))
except ValueError:
    print("Voer een numerieke waarde in")
