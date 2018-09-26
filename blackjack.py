import random
tal = (random.randint(1, 4))
gissning = (int(input("Gissa om det är Hjärter, Spader, Klöver eller Rutter (1-4): ")))

if gissning == tal:
    print("Rätt.")
else:
    print("Fel. Rätt svar var:")
    print(tal)