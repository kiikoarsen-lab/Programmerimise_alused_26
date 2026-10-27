#Ülesanne 1
import calendar
from datetime import *
from calendar import * #monthrange
tana=date.today()
print(f"Tere! \nTäna on {tana}")

# 27/12/2022
tana1 = tana.strftime("%d/%m/%Y")
print(f"Täna on {tana1}")

# December 27, 2022
tana2 = tana.strftime("%d/%m/%Y")
print(f"Täna on {tana2}")

# 12/27/22
tana3 = tana.strftime("%d/%m/%Y")
print(f"Täna on {tana3}")

# Dec-27-2022
tana4 = tana.strftime("%d/%m/%Y")
print(f"Täna on {tana4}")

# Omadused day, month, year kasutatakse päeva, kuu ja aasta parameetri leidmiseks date klassist.
# Arvuta mitu päeva on jäänud kuu lõpuni, aasta lõpuni.
# Arvuta oma vanus aastates, kuudes ja päevades.
print("Täna on", tana.day)
print("päev, kuu number on", tana.month)
print("ja aasta on", tana.year)
kuulõpuni=monthrange(tana.year, tana.month)[1] - 1
print("Kuu lõponi on jäänud", kuulõpuni, "päeva")
aastalõpuni=(date(tana.year, 12, 31) - tana).days
print("Aasta lõpuni on jäänud", aastalõpuni,"päeva.")
sünnipäev=date(2011, 6, 17)
vanus=aastalõpuni//365
print("Oled", vanus, "aastat,")
print((aastalõpuni%365)//30, "kuud ja")
print((aastalõpuni%365)%30, "päeva vana.")


#Ülesanne 2
print("3 + 8 / (4 - 2) * 4 =", 3 + 8 / (4 - 2) * 4)
print("(3 + 8) / 4 - 2 * 4 =", 3 + 8 / 4 - 2 * 4)
print("(3 + 8) / 4 - 2 * 4 =", (3 + 8) / 4 - 2 * 4)


#Ülesanne 3

try:
    R= float(input("Sisesta ringi raadius: "))
    print("Ruudu pindala", R**2)
    print("Ruudu ümbermõõt:", 4*R)
    print("Ringi pindala", 3.14*R**2)
    print("Ringi ümbermõõt:", 2*3.14*R)
except ValueError:
    print("Valed andmed")
    
#Ülesanne 4
# Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes müntides ehk teisisõnu:
# kui palju 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa. Kasuta teadmist, 
# et Maa raadius ekvaatori kohal on 6378 km. 


raadius_km = 6378
myndi_mm = 25.75 
pi = 3.14
ekvaator_km = 2 * pi * raadius_km
ekvaator_mm = ekvaator_km * 1000000
myntide_arv = round(ekvaator_mm / myndi_mm)
print("Ekvaatorile mahub nii palju", myntide_arv, "münte")
#Ülesanne 5
a="Kill-koll"
b="Killadi-koll")
print(a.upper()* 3 + b.upper() + a.upper()* 3 + b.upper() + a.upper()* 3)

#Ülesanne 6
print("Rong see sõitus tsuhh tsuhh tsuhh,".upper())
print("""piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill.""".upper())
 
#Ülesanne 7
