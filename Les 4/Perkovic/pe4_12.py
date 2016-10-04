s = 'abcdefghijklmnopqrstuvwxyz'
print(s[1:4], s[:3], s[3:-2], s[-4:-1], s[-4:], sep='\n')


poem = "\nDit is regel 1,\ndit is lijn 2, \nen dit is lijn 3."

print(poem)

a = "0123456789"

print(a[2:5], a[7:9], a[1:8], a[:4], (a[-3:]))

x = '2;3;5;7;11;13'

test = x.split(';')

print(test)

table = str.maketrans('abcdef', 'uvwxyz')
translate = 'cad'.translate(table)
print(translate)

forecast = 'It will be a sunny day today'

optellen = forecast.count("day")
print(optellen)
weer = forecast.find("sunny")
print(weer)
verander = forecast.replace('sunny', 'cloudy')
print(verander)


def even(n):
    for i in range(2, n+1):
        if i%2 == 0 or i%3 == 0:
            print(i, end=', ')
even(17)

first = 'Gökmen'
last = 'Simsek'
street = 'Tulpenstraat'
number = 33
city = 'Doetinchem'
state = 'Gelderland'
zipcode = '7004DE'
print("\n{} {} \n{} {} \n{}, {} {}" . format(first,last,number,street,city, state, zipcode))
print('\nMy name is {} {}, and my address is, {} {},\nthe city i live in is, {}, {} and my zipcode is {}' .format(first,last,street,number,city,state,zipcode))
print('i i**2 i**3 2**i')
def growthrates(x):
    print(' i   i**2   i**3    2**i')
    formatStr = '{0:2d} {1:6d} {2:6d} {3:6d}'
    for i in range(2,x+1):
        print(formatStr.format(i,i**2,i**3,2**i))

print(growthrates(6))
