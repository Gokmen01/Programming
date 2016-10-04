while True:
    print("Geef een string van vier letters:")
    woord = input()
    if len(woord) == 4:
        print('Inlezen van correcte string: %s is geslaagd' %(woord))
        break
    else:
        lengte = len(woord)
        print('%s heeft %s letters' %(woord, lengte))
