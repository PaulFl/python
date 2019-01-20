import random

numero_choisi = input("Choisir un numéro: ")
mise = input("Mise: ")

tirage = random.randint(0, 49)

if tirage == numero_choisi:
    print("Vous avez gagné ", 3*tirage)
elif tirage % 2 == numero_choisi % 2:
    print("Vous avez gagné ", 2*tirage)
else:
    print("Vous avez perdu")
