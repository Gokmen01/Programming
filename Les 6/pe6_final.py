print('Voer je naam in:')
naam = input()
print('Voer beginstation in:')
beginstation = input()
print('Voer eindstation in:')
eindstation = input()

invoerstring = (naam+beginstation+eindstation)
lijst = []

def code(invoerstring):
    for letter in invoerstring:
        vertalen = chr(ord(letter) +3)# ingevoerde teken omzetten naar ASCII nummer en met 3 verhogen
        lijst.append(vertalen) # vertaalde tekens toevoegen aan lijst
    vertaald = ''.join(lijst) #items in lijst samenvoegen
    return vertaald

print('Unieke code: {}' .format(code(invoerstring)))
