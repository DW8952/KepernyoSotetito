import time
import sys
probalkozasok = 0
while True:
    szazalek = input("Mennyire sötétítsem a képernyőd? csak szamot adj meg 0-100 kozott. : ")
    with open('mentes.txt', 'a') as file:
        file.write(szazalek + '\n')
    try:
        szam = int(szazalek)
    except ValueError:
        print("nem jo. 0-100 kozott, semmi mas. nem latom mit irtal de elrontottad xd szeretlek szivem")
        print("(ha ki akarsz lepni, akkor nyomd meg a ctrl+c-t, vagy zárd be ezt az ablakot. :3)")
        print()
        probalkozasok += 1
        if probalkozasok > 2:
            print("\n \n \n")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("1 dolgod volt gec xd")
            time.sleep(4)
            sys.exit()
        continue
    if szam < 0 or szam > 100:
        print("nem jo. 0-100 kozott, semmi mas. nem latom mit irtal de elrontottad xd szeretlek szivem")
        print("(ha ki akarsz lepni, akkor nyomd meg a ctrl+c-t, vagy zárd be ezt az ablakot. :3)")
        print()
        probalkozasok += 1
        if probalkozasok > 2:
            print("\n \n \n")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("1 dolgod volt gec xd")
            time.sleep(4)
            sys.exit()
        continue
    szazalek = szam
    break
print(f"A képernyő sötétítése: {szazalek}%-al...")
if szazalek == 0:
    print("nem sötétítettem a képernyőt, mert 0%-ot adtál meg. :P")
    sys.exit()
atvaltas255re = int(szazalek * 2.55)
with open('hasznal.txt', 'w') as file:
    file.write(str(atvaltas255re))   

import subprocess
import sys
import os
if getattr(sys, 'frozen', False):
    # Ha lefordított EXE-ből fut
    alkalmazas_mappa = os.path.dirname(sys.executable)
else:
    # Ha sima Python szkriptből fut
    alkalmazas_mappa = os.path.dirname(os.path.abspath(__file__))

# A dimmer elérési útjának összeállítása
# Fontos: Exe készítés után itt már a .exe kiterjesztést kell keresni!
dimmer_eleresi_ut = os.path.join(alkalmazas_mappa, "dimmer.exe")

# Indítás
folyamat = subprocess.Popen([dimmer_eleresi_ut])

print("El is indult! Ha be szeretnéd zárni a sötétítést, akkor zárd be azt az ablakot ami megnyílt. :3")
time.sleep(1)
print("ezt ne zárd be! bezárom én magamtól köszi :P")
time.sleep(2)
print("I love you more +1 bleeeee")
time.sleep(1)
print("Bezárásig:")
for i in range(10, 0, -1):
    print(f"{i}...")
    time.sleep(1)
sys.exit()