def standaardtarief(afstandKM):
    if afstandKM > 50:
        return (afstandKM * 0.60) + 15
    elif afstandKM < 0:
        return 0
    else:
        return afstandKM * 0.80

dagen = ["Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag","Zaterdag", "Zondag"]

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardtarief(afstandKM)

    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit in dagen[0:5]:
            prijs = prijs * 0.70
            return "%s is niet in het weekend, prijs met korting is %s" %(weekendrit, prijs)
        if weekendrit in dagen[5:7]:
            prijs = prijs * 0.65
            return "%s is in het weekend, prijs is %s" %(weekendrit, prijs)
        if weekendrit != dagen:
           print("%s is geen geldig dag" %(weekendrit))
    elif weekendrit in dagen[5:7]:
        prijs = prijs * 0.60
        return "Reguliere prijs met korting voor in het weekend %s" %(prijs)
    else:
        return "Reguliere prijs is %s" %(prijs)
print("Wat is uw leeftijd ?")
leeftijd = eval(input())
print("Welke dag is het ?")
weekendrit = input()
print("Geef een afstand op")
afstand = eval(input())


print(ritprijs(leeftijd,weekendrit,afstand))
print(ritprijs(leeftijd,weekendrit,-10))
print(ritprijs(12,"Woensdag",100))
print(ritprijs(11,"Maandag",20))
print(ritprijs(11,"Zaterdag",20))
print(ritprijs(15,"Zaterdag",20))
