from collections import Counter
counts = Counter()
with open("mentes.txt", "r") as file:
    for line in file:
        stripped = line.strip()
        if stripped.isdigit():
            number = int(stripped)
            if 0 <= number <= 100:
                counts[number] += 1
if counts:
    most_common_number, frequency = counts.most_common(1)[0]
    print(f"A leggyakoribb szám: {most_common_number} (beirtad {frequency} alkalommal)")
else:
    print("Nincs érvényes szám a fájlban.")   
akartobbet = str(input("kell tobb info? Y/N"))
if akartobbet == "Y" or akartobbet == "Yes":
    mindenszam = []
    with open("mentes.txt", "r") as file:
        for line in file:
            stripped = line.strip()
            if stripped.isdigit():
                szam = int(stripped)
                if 0 <= number <= 100:
                    hasznaltszam = szam
                    if hasznaltszam in mindenszam:
                        pass
                    else:
                        mindenszam.append(hasznaltszam)
    print("Minden szám ami 0-100 között volt, és használtál:")
    for i in range(mindenszam.len):
        
        print("")