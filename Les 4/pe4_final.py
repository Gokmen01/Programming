annulering = []
stations = []

treinritten = open('treinritten')
treinrittenList = treinritten.readlines()
treinritten.close()

annuleringen = open('annuleringen')
annuleringList = annuleringen.readlines()
annuleringen.close()

for station in annuleringList:
    rittenList = station.rstrip().split(':')
    annulering.append(rittenList[1])

for treinStations in treinrittenList:
    Stations = treinStations.rstrip().split('-')
    if (annulering.count(Stations[1]) == 0):
        stations.append(treinStations)

definitief = open('definitief', 'w')
definitief.writelines(stations)
definitief.close()

print('{} \n{}' .format(annulering, stations))
