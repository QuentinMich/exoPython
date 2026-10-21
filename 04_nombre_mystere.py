mystNmb = 21

print ("On va jouer a un jeu, devine le nombre")

while True :
    nmb = int( input ("Quel est ton nombre ?"))
    if nmb > mystNmb :
        print ("Nope, trop Haut !")
        continue
    elif nmb < mystNmb :
        print ("Nope, trop petit !")
        continue
    else :
        print ("Bravo t'as gagné Batard !")
        break

