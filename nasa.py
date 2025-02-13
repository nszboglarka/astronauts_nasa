honapok = []
with open('astronauts.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        urhajos = sor.strip().split(',')
        szuletes = urhajos[4].split('/')
        if len(szuletes) == 3:
            honap = szuletes[0]
            honapok.append(int(honap))

szam = 1
gyakorisagok = []
while szam < 13:
    hanyszor = honapok.count(szam)
    gyakorisagok.append(hanyszor)
    szam = szam + 1


sorrend = []
for elem in gyakorisagok:
    sorrend.append(elem)
sorrend.sort()


print(f'A leggyakoribb hónap: {gyakorisagok.index(sorrend[-1])+1}., az űrhajósok {sorrend[-1]/(len(honapok)+1)*100} %-a született ekkor.')
print(f'A második leggyakoribb hónap: {gyakorisagok.index(sorrend[-2])+1}., az űrhajósok {sorrend[-2]/(len(honapok)+1)*100} %-a született ekkor.')
print(f'A harmadik leggyakoribb hónap: {gyakorisagok.index(sorrend[-3])+1}., az űrhajósok {sorrend[-3]/(len(honapok)+1)*100} %-a született ekkor.')
