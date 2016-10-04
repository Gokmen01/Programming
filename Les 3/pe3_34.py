def pay(uurLoon,uren):
    if uren > 40:
        return ((uren -40) * uurLoon * 1.5) + 40 * uurLoon
    else:
        return uurLoon * uren

print(pay(10,45))



