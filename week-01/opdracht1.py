# Oefening 1
# Print de volgende zin "Hello World"
 
print ("hello World")


# Oefening 2
# Verander de waarde van de onderstaande variabelen.
# Print deze daarna 1 voor 1 uit

naam = "Bjorn"
leeftijd = 18
woonstad = "Breukelen"


# Oefening 3
# Gebruik nu bovenstaande variabelen om zinnen te bouwen
# Bijvoorbeeld print("Hallo mijn naam is ", naam) of print(f"Mijn naam is {naam}")
print(f"Hallo mijn naam is {naam} en ik ben {leeftijd} jaar oud.")


# Oefening 4
# Maak variabelen aan voor je favoriete game, hoe veel uur je deze hebt gespeeld en welk cijfer je dit spel zou geven
# Print deze daarna in zinnen uit, bijvoorbeeld "Mijn favoriete game is Minecraft" "Ik heb deze game 150 uur gespeeld", "Ik geef deze game een 8.5"
game = "Valorant"
uren = 2200
cijfer = 7.3

print(f"Mijn favoriete game is {game}")
print(f"Ik heb deze game {uren} uur gespeeld")
print(f"Ik geef deze game een {cijfer}")


# Oefening 5
# Maak twee variabelen aan, number1 en number2
# Bereken daarna de som (+), het verschil (-) en het product (*) uit van deze nummers.
# Print daarna de uitkomsten uit
number1 = 10
number2 = 5

print(number1 + number2)
print(number1 - number2)
print(number1 * number2)


# Oefening 6
# Maak een simpel game character met minimaal de volgende variabelen: name, health, level, damage
# Print deze vervolgens uit
# Zorg er daarna voor dat je character 20 damage neemt, print nu de nieuwe waarde van zijn health uit

name = "sonic"
health = 200
level = 1
damage = 20
health1 = health - damage 
weapon = "pump" 
exp = 0
weaponDamage = 73
exp += 150


if exp >= 100:
    level += 3
    exp -= 100

print (f"{name} krijgt {damage} damage, hij heeft nu minder dan {health} health. zijn heelft is nu {health1} ")


# Oefening 7
# Ga verder met je character van de vorige oefening. Voeg nu een nieuw variabel "weapon" toe.
# Geef het wapen een naam, verhoog de damage van je character en verhoog het level met 1
# Print daarna de nieuwe waardes uit 
print (f"sonic pakt een {weapon} op, hij komt een vijand tegen en killed hem hij deed {weaponDamage + damage} damage. na een kill maken krijgt hij {exp} exp, nu is zijn level {level}  ") 



# Oefening 8
# Maak een programma dat een profiel van een gamer laat zien
# Maak minimaal de volgende variabelen: name, age, favouriteGame, hoursPlayed, level, score
# Print al deze informatie netjes uit
# Verhoog daarna de score van het profiel met 250 en print de nieuwe waarde
# Bonus! Voeg zelf 3 nieuwe variabelen toe


name = "Bjorn"
age = 17
favouriteGame = "Valorant"
hoursPlayed = 120
level = 25
score = 1500

weapon = "Vandal"
kills = 250
rank = "Gold"


print("=== Gamer Profiel ===")
print("Naam:", name)
print("Leeftijd:", age)
print("Favoriete game:", favouriteGame)
print("Uren gespeeld:", hoursPlayed)
print("Level:", level)
print("Score:", score)

print("Wapen:", weapon)
print("Kills:", kills)
print("Rank:", rank)


score = score + 250


print("Nieuwe score:", score)