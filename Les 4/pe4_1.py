def convert(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit
def table(celsiusMin, celsiusMax):
    print(' {:6}    {}'.format('F','C'))
    for graden in range(celsiusMin,celsiusMax, 10):
        print ('{:5}   {:5}'.format(convert(graden), graden))

print(table(-30, 21))

