print ("Je vois dans ma grosse boule, mon enfant")
name = input ("Donne moi ton prénom, mon enfant ")
age = int(input ("Donne moi ton âge maintenant "))
print ("Azakazam boom boom, je vais te lire ton avenir")

if  0 <= age < 18:
    pred = "tu va te faire taper par un CRS"
elif  18 <= age <= 30:
    pred = "tu va voter pour LFI sale petit chenapan"
elif  31 <= age <= 60:
    pred = "tu ne te rendra jamais compte que glucksman c'est en fait Macron 2.0"
else :
    pred = "tu n'arretera jamais de croire Cnews comme moi HAHAHAHAHAHAHAHAH"

year = 2026 - age
agePlus = age + 10

print (f"Madame Irma voit tout, {name} !\nTu es né(e) vers {year}.\nDans 10 ans, tu aura {agePlus} ans.\nTa prédiction est que {pred} !")