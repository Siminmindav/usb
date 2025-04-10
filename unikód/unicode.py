run = 1
while run:
    try:
        válasz = int(input("Egy karakter keresése: 1\nIntervallumos kiírás: 2\nKilépés: 3\n"))

        if válasz == 1:
            válasz2 = input("Keresés karakter alapján: 1\nKeresés szám alapján: 2\n")
            if válasz2 == "1":
                karakter = input("Karakter: ")
                print(f"{karakter} - {ord(karakter)}")
            elif válasz2 == "2":
                szám = int(input("Szám (0 <= x <= 1.114.111, pl.: 169): "))
                print(f"{szám} - {chr(szám)}")

        elif válasz == 2:
            válasz2 = list(map(int,input("Írd be az intervallumot (0 <= x <= 1.114.111, pl.: 0 10)\n").split()))
            for i in range(válasz2[0],válasz2[1]):
                try:
                    print(f"{i} - {chr(i)}")
                except:
                    pass

        elif válasz == 3:
            run = 0

    except:
        print("Hiba")