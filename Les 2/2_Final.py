stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam', 'Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '\'s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginStation = input("Wat is je beginstation? :")

if beginStation in stations:
    print("Beginstation is: %s" %(beginStation))
else:
    beginStation = stations[0]
    print("Dit station is niet geldig, beginstation is: %s" %(beginStation))

eindStation =input("Wat is je eindstation? :")

if eindStation in stations and stations.index(beginStation) < stations.index(eindStation):
    print("Eindstation is: %s" %(eindStation))
else:
    eindStation = stations[-1]
    print("Dit station is niet geldig, eindstation is: %s" %(eindStation))
beginIndex = stations.index(beginStation) +1
eindIndex = stations.index(eindStation) +1
afstandStation = eindIndex- beginIndex
prijs = afstandStation * 5

print("Het beginstation %s is het %se station in het traject" %(beginStation, beginIndex))
print("Het eindstation %s is het %se station in het traject" %(eindStation, eindIndex))
print("De afstand bedraagt %s station(s)" %(afstandStation))
print("De prijs van het kaartje is %s euro." %(prijs))
print("\n")
print("Jij stapt in de trein in: %s" %(beginStation))
haltes = range(beginIndex -1, eindIndex -1)
for i in haltes:
    print('  -' + stations[i])
print("Jij stapt uit in: %s" %(eindStation))
