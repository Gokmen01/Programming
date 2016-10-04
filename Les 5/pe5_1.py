
lst = ["Januari", "Februari","Maart","April","Mei","Juni","Juli","Augustus","September","Oktober", "November", "December"]
print(lst[-1:])
while True:
    print('Voer een maand in: (enter om te stoppen)')
    maand = input()
    if maand == '':
        break
    if maand in lst[:3]:
       print("In %s is het lente " %(maand))
    elif maand in lst[3:6]:
        print("In %s is het zomer" %(maand))
    elif maand in lst[6:9]:
        print("In %s is het herfst" %(maand))
    elif maand in lst[-1:]:
        print("In %s is het winter" %(maand))
    else:
        print('%s is geen geldige maand..' % (maand))
        continue
