#1
eesnimi=input("Sisesta eesnimi:")
if eesnimi.lower() == "juku":
    print("Lähme Jukuga kinno!")
    if eesnimi.isupper():
        print("Ära karju, Juku!")
    elif eesnimi.islower():
        print("Ära sosista, Juku!")
        vanus=input(f"Kui vana on {eesnimi}?")
        if vanus.isdigit():
            vanus=int(vanus)
            if 0<vanus<6:
                pilet="tasuta pilet"
            elif 6<=vanus<14:
                pilet="Läpseplet"
            elif 14<=vanus<65:
                pilet="täispilet"
            elif 65<=vanus>=100:
                print="sooduspilet"
            else:
                pilet="tundmatu pilet"
            print(f"{eesnimi} vajab {pilet}.")
        else:
            print("Viga andmedega")
else:
    print("Täna kinno ei minda.")

#2
pinginaabrid=["Mati","Kati"]
nimi1=input