
def kwadraten_som(grondgetallen):
    for getallen in grondgetallen:
        if getallen > 0:
            return (sum( getallen * getallen))
lijst = [4, 5, 3, -81]
print(kwadraten_som(lijst))
