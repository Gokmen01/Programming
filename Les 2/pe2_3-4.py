leeftijd = input("Uw leeftijd:")
paspoort = input("Beschikt u over een paspoort?")

if (leeftijd >="18" and paspoort == "ja" or "Ja"):
    print("Gefeliciteerd, je mag stemmen!")
else:
    print("U mag niet stemmem")
print("Done.")
