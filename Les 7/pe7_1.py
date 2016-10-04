try:
    print("Hoeveel mensen gaan er mee?")
    aantalPersonen = int(input())
    bedrag = 4356 / aantalPersonen
    if bedrag < 0:
        print("Negative getallen zijn niet toegestaan!")
    else:
        print(bedrag)
except ZeroDivisionError:
    print("Kan aantal niet delen door 0")
except ValueError:
    print("Vul alleen numerieke waardes in")
except:
    "Onjuiste invoer!"




