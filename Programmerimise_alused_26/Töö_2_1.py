#1
# from curses.ascii import isalpha


# eesnimi=input("Sisesta eesnimi:")
# if eesnimi.lower() == "juku":
#     print("Lähme Jukuga kinno!")
#     if eesnimi.isupper():
#         print("Ära karju, Juku!")
#     elif eesnimi.islower():
#         print("Ära sosista, Juku!")
#         vanus=input(f"Kui vana on {eesnimi}?")
#         if vanus.isdigit():
#             vanus=int(vanus)
#             if 0<vanus<6:
#                 pilet="tasuta pilet"
#             elif 6<=vanus<14:
#                 pilet="Läpseplet"
#             elif 14<=vanus<65:
#                 pilet="täispilet"
#             elif 65<=vanus>=100:
#                 print="sooduspilet"
#             else:
#                 pilet="tundmatu pilet"
#             print(f"{eesnimi} vajab {pilet}.")
#         else:
#             print("Viga andmedega")
# else:
#     print("Täna kinno ei minda.")

#2

from curses.ascii import isdigit
from math import pi
from multiprocessing import Value


pinginaabrid=["Mati","Kati"]
nimi1=input("Sisesta nimi:")
nimi2=input("Sisesta nimi:")
if nimi1.isalpha() and nimi2.isalpha():
    print(f"Tere {nimi1.capitalize()} ja {nimi2.capitalize()}")
    if nimi1.capitalize() in pinginaabrid and nimi2.capitalize() in pinginaabrid:
        print(f"{nimi1} ja {nimi2} on pinginaabrid")
    else:
        print("Nad ei ole pinginaabrid") 
            
else:
    print("Viga: nimed on valesti sisestatud! Kasuta ainult tähed")

#3   
# Küsi ristkülikukujulise toa pikkus ja laius ning arvuta põranda pindala.
# Seejärel küsi, kas kasutaja soovib remonti teha. Kui vastus on jaatav,
# küsi ruutmeetri hind ja arvuta põranda vahetamise hind.
# Lisaküsimus: kas kasutaja teeb remondi ise või kasutab professionaali abi? 
# Professionaali puhul küsi ka töö hind ruutmeetri kohta ja arvuta remondi koguhind koos tööga.
# Kasuta: float(), lower() (vastuse „Jah“, „JAH“, „jah“ äratundmiseks), round()
# try:
#      pikkus=float(input("Sisesta pikkus: "))
#      laius=float(input("Sisesta laius: "))
#      pindala=round(pikkus*laius,2)
#      print(f"Pindala on {pindala}")
#      remondi_soov=input("Kas soovid remonti teha? (jah/ei):").lower()
#      if remondi_soov=="jah":
#          print("Teeme remonti!")
#          try:
#              rm_hind=float(input("Sisesta ruutmeetri hind: "))
#              hind=round(pindala*rm_hind,2)
#              print(f"Põranda vahetamise hind on {hind} €")
#              ise=input("Kas teeb remondi is?(jah/ei)").lower()
#              if ise=="jah":
#                  print(f"Põranda vahetamise hind on sama {hind} €")
#              else:
#                  try:
#                      töö_hind=float(input("Töö hind: "))
#                      koguhind=round(hind+pindala*töö_hind,2)
#                      print(f"Remondi koguhind koos tööga on {koguhind}")
#                  except ValueError:
#                      print("Töögind on ujukomarv")
#          except ValueError:
#              print("Viga: ruutmeetri hind on arv")
#      else:
#          print("Remonti ei tehta!")



# except ValueError:
#      print("Viga: kasuta numbreid pikkuse ja sisestamiseks")

#4
try:
    hind = float(input("Sisesta kauba hind: "))
    if hind > 700:
        lopphind = round(hind * 0.7,2)
    else:
        lopphind = hind
    print(f"Kauba lõpphind on {lopphind} €")
except ValueError:
    print("Viga! Palun sisesta korrektne hin ")

#5
try:
    temperatuur = float(input("Sisestage ruumi temperatuur: "))
    if temperatuur > 18:
        print("Temperatuur ületab 18 kraadi")
    else:
        print("Temperatuur ei ületa 18 kraadi.")

except ValueError:
     print("Viga! Palun sisesta korrektne hin ")
#6,7
sugu = input("Sisestage oma sugu (M / mees või N / naine): ").lower()
if sugu in ["m", "mees"]:
    try:
        pikkus = int(input("Kirjutage oma pikkus: "))
        if pikkus < 165:
            print("Te olete lühikest kasvu")
        elif 166<=pikkus<178:
            print("Te olete keskmist kasvu:")
        elif 179<=pikkus<=185:
            print("Te olete pikka kasvu")
        elif 186<=pikkus> 190:
            print("Te olete väga pikka kasvu")
        else:
            print("Te olete väga lühikest kasvu ")
    except  ValueError:
        print("Viga! Palun sisesta korrektne hin ")
if sugu in ["n","naine"]:
    try:
       pikkus1 = int(input("Kirjutage oma pikkus: "))
       if 152<=pikkus1<=159:
            print("Te olete lühikest kasvu")
       elif 160<=pikkus1<169:
            print("Te olete keskmist kasvu:")
       elif 170<=pikkus1<=180:
            print("Te olete pikka kasvu")
       elif pikkus1> 180:
            print("Te olete väga pikka kasvu")
       else:
            print("Te olete väga lühikest kasvu ")
    except  ValueError:
        print("Viga! Palun sisesta korrektne hin ")
#8
from random  import *
summa=0
arve="Toode  Kogus Hind  Kokku\n"
valik=input("Kas soovid osta piima? (jah/ei): ")
if valik.lower()=="jah":
    kogus=input("Kui palju piima soovid osta (täisarv): ")
    if kogus.isdigit():
        kogus=int(kogus)
        piim_hind=round(uniform(0.5, 3), 2)
        print(f"Piima hind on {piim_hind} eurot.")
        summa+=round(kogus*piim_hind,2)
        print(f"Piima kogusumma om {summa} eurot.")
        arve+=f"piim  {kogus}  {piim_hind}€  {kogus*piim_hind}€\n"
    else:
        print("Viga: vale hind!")
else:
    print("Selge: Piima ei taha")
print(f"Kogusumma on:{summa} eurot.")

valik = input("\nKas soovid osta leiba? (jah/ei): ")
if valik.lower() == "jah":
    kogus = input("Kui palju leiba soovid osta (täisarv): ")
    if kogus.isdigit():
        kogus = int(kogus)
        leib_hind = round(uniform(0.5, 3), 2)
        print(f"Leiva hind on {leib_hind} eurot.")
        toote_summa = round(kogus * leib_hind, 2)
        summa += toote_summa
        print(f"Leiva kogusumma on {toote_summa} eurot.")
        arve += f"Leib {kogus} {leib_hind}€  {toote_summa}€\n"
    else:
        print("Viga: vale kogus!")
else:
    print("Selge: Leiba ei taha")

valik = input("\nKas soovid osta sai? (jah/ei): ")
if valik.lower() == "jah":
    kogus = input("Kui palju sai soovid osta (täisarv): ")
    if kogus.isdigit():
        kogus = int(kogus)
        sai_hind = round(uniform(0.5, 3), 2)
        print(f"Sai hind on {sai_hind} eurot.")
        toote_summa = round(kogus * sai_hind, 2)
        summa += toote_summa
        print(f"Sai kogusumma on {toote_summa} eurot.")
        arve += f"Sai {kogus} {sai_hind}€  {toote_summa}€\n"
    else:
        print("Viga: vale kogus!")
else:
    print("Selge: Sai ei taha")

valik = input("\nKas soovid osta juust? (jah/ei): ")
if valik.lower() == "jah":
    kogus = input("Kui palju juust soovid osta (täisarv): ")
    if kogus.isdigit():
        kogus = int(kogus)
        juust_hind = round(uniform(0.5, 3), 2)
        print(f"Juust hind on {juust_hind} eurot.")
        toote_summa = round(kogus * juust_hind, 2)
        summa += toote_summa
        print(f"Juust kogusumma on {toote_summa} eurot.")
        arve += f"Juust {kogus} {sai_hind}€  {toote_summa}€\n"
    else:
        print("Viga: vale kogus!")
else:h
    print("Selge: Juust ei taha")



