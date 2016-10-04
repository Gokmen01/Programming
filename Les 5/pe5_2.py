strings = eval(input("geef een lijstje met minimaal 10 strings"))

vier_letter_strings = []
for s in strings:
    if (len(s) == 4):
        vier_letter_strings.append(s)

print(vier_letter_strings)
#-------------------
lst = [2,6,7,8,4,2]

print(max(lst))
totaal = 0

for nr in lst:
    if (nr %2 == 0):
        totaal += nr
        print(totaal)

