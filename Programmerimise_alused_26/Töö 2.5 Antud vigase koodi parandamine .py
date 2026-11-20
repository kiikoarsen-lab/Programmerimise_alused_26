menüü = input("Sisestaga menüü (Arvu kontroll / arv või Kehamassiindeks / k või Ostu allahindlus / o)").lower()
if menüü in ["a", "arv"]:
    print("Arvu kontroll")#print('-->"Arvu kontroll")
    try:
           arv=float(input("Sisesta täisarv => "))#float
           if arv>0: #:
               print("Arv on positiivne")
               if arv == 0:#kusututa else
                print("Arv on null")
           else:
                print("Arv on negatiivne")
           if arv%2==0:
               print("Arv on paarisarv")
           else:
               print("Arv on paaritu")
    except ValueError:
     print("Valed andmed. Sisesta täisarv")
if menüü in ["k", "keha"]:
    print("Kehamassiindeks")
    try:
        mass=float(input("Sisesta kaal (kg) => "))
        pikkus=float(input("Sisesta pikkus (m) => "))# )
        kmi=mass/pikkus**2
        print("KMI:", round(kmi,1))
        if kmi<18.5:
            print("Alakaal")
        elif kmi<=18.5:
            print("Normaalkaal")
        elif kmi<=29:
            print("Ülekaal")
        elif kmi<=30:# :
            print("Rasvumine")
        else:
          print("Ostu allahindlus")
    except ValueError:
        print("Valed andmed. Sisesta täisarv")
if menüü in ["o", "ostu"]:
    try:
        summa=float(input("Sisesta ostusumma => "))
        if summa<=0:
            print("Vigane summa")
        elif summa>100 or summa>=500:
            print("Allahindlus 5%, maksta:", round(summa*0.95,2))
        elif summa<500:
            print("Allahindlus 10%, maksta:", round(summa*0.9,2))
        else: 
            print("Allahindlust pole, maksta:", summa)
    except ValueError:
        print("Valed andmed. Sisesta täisarv")
# Programmi tulemus:

 
# Arvu kontroll
# Sisesta täisarv => 9
# Arv on positiivne
# Arv on paaritu

# Kehamassiindeks
# Sisesta kaal (kg) => 85
# Sisesta pikkus (m) => 1.75
# KMI: 27.8
# Ülekaal

# Ostu allahindlus
# Sisesta ostusumma => 650
# Allahindlus 10%, maksta: 585.0
