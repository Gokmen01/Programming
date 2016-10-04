import csv

with open('ticker', 'r') as ticker:
    reader = csv.reader(ticker, delimiter=':')
    print("Enter Company name:")
    bedrijf = input()
    for (key,value) in reader:
        if (key) == bedrijf:
            print('Ticker symbol: {}\n' .format(value))
            break
    print("Enter Ticker symbol:")
    symbol = input()
    for (key,value) in reader:
        if (value) == symbol:
            print('Company name: {}' .format(key))
