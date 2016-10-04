bestand = open('C:/Users/Gokmen/Documents/kaartnummers.txt', 'r')
linelist = bestand.readlines()
nummerMax = max(linelist)
nummerIndex= nummerMax[:6]
regel = linelist.index(nummerMax)
bestand.close()
print('Deze file telt {} regels' .format(len(linelist)))
print('Het hoogste kaartnummer is: {} en dat staat op regel: {}'.format(nummerIndex,regel+1))





