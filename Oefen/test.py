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

    if weekendrit in dagen[0:5] and leeftijd < '12' or leeftijd >= '65':
        prijs = prijs * 0.70
        return "%s is niet in het weekend, prijs is €%s" %(weekendrit, prijs)
    elif weekendrit in dagen[5:7] and leeftijd < '12' or leeftijd >= '65':
        prijs = prijs * 0.65
        return "%s is in het weekend, prijs is €%s" %(weekendrit, prijs)
    elif weekendrit in dagen[5:7]:
        prijs = prijs * 0.60
        return "Reguliere prijs met korting voor in het weekend €%s" %(prijs)
    else:
        return "Reguliere prijs is €%s" %(prijs)

weekendrit = input("Welke dag is het ?")
leeftijd = input("Wat is uw leeftijd ?")


print(standaardtarief(20))
print(ritprijs(leeftijd,weekendrit,20))
