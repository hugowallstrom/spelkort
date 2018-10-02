import random
fel = 0
tal = (random.randint(1, 4))
gissning = 0#start värden

while gissning != 5:
        
    gissning = (int(input("Gissa om det är Hjärter, Spader, Klöver eller Rutter (1-4): ")))
    
    if gissning == tal:
        print("Rätt. Slumpar siffran igen. Antal fel: ")
        print(fel)#visar felgissningar
        tal = (random.randint(1, 4))
        
    else:
        print("Fel. Försök igen.")
        fel += 1#räknar antal fel