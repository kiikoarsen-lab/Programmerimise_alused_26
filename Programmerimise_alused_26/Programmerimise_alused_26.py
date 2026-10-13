# siia kirjutame mis moodulid tahame importida ja hiljem kasutame
import math


print("Tere tulemast!") #kommentaar
print("Esimene pragramm") #sep =" ",end="\n"
# #muutujad
# kursus=2
# print("Ma õpin",1,".kursusel")#sep =" ",end="\n"
# print("Ma õpin",kursus,".kursusel",sep="***",end=". ")
# kursus=int(input("Aga sina?")) # str->int
# print("Tore! Sa õpid",kursus,".kursusel. Aga järgmisel aastal",kursus+1,"kursusel")
# nimi = input("Mis on sinu nimi? ")
# print("Tere,", nimi)
# print(nimi,"õpib",kursus,".kursusel")

# a = int(input("Esimene arv: "))
# b = int(input("Teine arv: "))
# print(a + b) # liitmin
#Põhioperarsiooonid: + - * / // % **
# astendamine	**	2 ** 3	8
# korrutamine	*	4 * 5	20
# jagamine	/	7 / 2	3.5
# jagamise täisarvuline osa	//	7 // 2	3
# jagamisjääk	%	7 % 2	1
# liitmine	+	10 + 3	13
# lahutamine	-	9 - 4	5
# a = float(input("Esimene arv: "))
# b = float(input("Teine arv: "))
# print(a ** b) # astendamine

# a = float(input("Esimene arv: "))
# b = float(input("Teine arv: "))
# print(a * b) # korrutamine

# a = float(input("Esimene arv: "))
# b = float(input("Teine arv: "))
# print(a / b) # jagamine

# a = float(input("Esimene arv: "))
# b = float(input("Teine arv: "))
# print(a // b) # jagamise täisarvuline osa

# a = float(input("Esimene arv: "))
# b = float(input("Teine arv: "))
# print(a % b) # jagamisjääk

# a = float(input("Esimene arv: "))
# b = float(input("Teine arv: "))
# print(a - b) # lahutamine

# nimi = "Mari"
# punktid = 87
# print(f"{nimi} sai {punktid} punkti.")

# hind = 19.9
# kogus = 3
# print(f"Kokku: {hind * kogus:.2f} eurot")

# #stingide ühendamine ja korrutamine
# print("Tere" + " " + "päevast")
# print("-" * 20)
# vanus = 17
# print("Vanus: " + str(vanus))

# math mooduli kasutamine
print("Pii väärtus:", math.pi)
print("√16 =", math.sqrt(16))
print("sin(π/2) =", math.sin(math.pi / 2))
print("sin(30°) =", round(math.sin(math.radians(30)), 2))
print("5! =", math.factorial(5))