from math import * # pi sqrt()
from random import *
# Kirjuta enda esimene programm, mis väljastab käsureale teksti:
#    “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii:
#    “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”
#Ülesanne1
 print("Tere, maalim!")
 nimi=input("Mis on sinu nimi? ")
 print("Tere, maalim! Tetrvitan sind",nimi)
 try:
     vanus=int(input("Kui vana sa oled"))
     print(" Tere, maalim! Tervitan sind " ,nimi,"Sa oled",vanus,"aastat vana.")
 except ValueError:
     print("Palun sisesta oma vanus numbrina")


# Mis tüüpi on järgnevad muutujad:
# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 16.5
# d) kas_käib_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# Kirjuta kood tüüpide kontrollimiseks.
#Ülesanne2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print("vanus:", vanus, "tüüp:", type(vanus))
print("eesnimi:", eesnimi, "tüüp:", type(eesnimi))
print("pikkus:", pikkus, "tüüp:", type(pikkus))
print("kas_käib_koolis:", kas_käib_koolis, "tüüp:", type(kas_käib_koolis))

# Kirjuta enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik). Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
# Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, kui palju komme laual nüüd on. 
#Ülesanne3
kommide_arv=randint(1,100) #1-100 vahel juhuslik täisarv
print("Laual on", kommide_arv, "kommi")
try:
    b=int(input("Mitu kommi soovid laualt ära võtta?"))
    kommide_arv -= b
    print("Laual on nüüd", kommide_arv,"kommi.")
except ValueError:
    print("Palun sisesta kommid numbrina.")
    


#Ülesanne4
# Puu läbimõõdu arvutamine
# Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.


# ümbermõõt=float(input("Sisesta puu ümbermõõt: "))

# labimõõt=ümbermõõt/pi
# print("Puu läbimõõt on:", läbimõõt)

# Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal,
#  mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
#Ülesanne5
N = float(input("Sisesta maatüki pikkus (N):"))
M = float(input("Sisesta maatüki pikkus (M):"))
diagonaal = sqrt(N**2 + M**2)
print("Ristkülikukujulise maatüki diagonaal on:", round (diagonaal,2))

#Ülesanne6
# Leidke järgnevast näiteprogrammist loogiline viga:



aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg

print("Sinu kiirus oli " + str(kiirus) + " km/h")

#Ülesanne7
# Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.
# Leia nende arvude summa, jagatuna kasutaja poolt sisestatud arvuga, täisarvuline osa ja jääk.
arv1=int(input("Sisesta esimene täisarv: "))
arv2=int(input("Sisesta teine täisarv: "))
arv3=int(input("Sisesta kolmas täisarv: "))
arv4=int(input("Sisesta neljas täisarv: "))
arv5=int(input("Sisesta viies täisarv: "))
summa=arv1+arv2+arv3+arv4+arv5
jagaja=int(input("Sisesta arv, millega jagada: "))
tulemus=summa/jagaja
print("Tulemus:", tulemus)
print("Täisarvuline osa:", int(tulemus))
print("Jääk:", summa % jagaja)

#Ülesanne8
# Joonista samasugune konn
print("  @..@")
print(" (----)")
print("( \__/ )")
print("^^ "" ^^")

#Ülesanne9
# Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Kasuta valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
c = float(input("Kolmas arv: "))
summa= a+b+c
print("P=",summa,)

#Ülesanne9
# Pitsa

# Võtsite sõpradega (näiteks P inimest) suure pitsa, mille hind on 12,90 €.
# Jätate teenindajale 10% jootraha.
# Koosta programm, mis arvutab, kui palju igaüks peab maksma.
P = int(input("inimest sööbib pitsa"))
hind = 12.90
jotraha = hind*0.10
kokku = hind + jotraha
inimese_osa = kokku / P
print("Igaüks peab maksma", round(inimese_osa, 2), "eurot")
