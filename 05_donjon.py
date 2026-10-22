score = 0
life = 3
donj = 0
# Ajout de la var donj pour suivre le systeme de salle grace a ce qu'on viens d'apprendre 
cont = "y"
# j'ai ajouté la var cont pour le continue après la var donj parce quand j'ai appris qu'une boucle ne prenait pas les conditions d'une boucle parent.


while cont == "y":
    print ( "Vous entrez dans le donjon de naheulbeurk, devant vous une porte immense se dresse. ")
    while donj == 0 and life > 0:
        choice = int ( input ("Que faite vous ?\n1: Je Casse la porte !\n2: Je toque a la porte ?\n3: Je passe par les égouts !\n") )
        if choice == 1:
            print ("Grand malade ! Tu es entendu par la garde et elle t'attaque, tu perd 1 vie mais tu passe. +5 points !")
            score += 5
            life -= 1
        elif choice == 2:
            print ("Toc Toc Toc !\n Un gobelin en costar t'ouvre la porte avec un sourir et te laisse passer, bravo ! +10 points")
            score += 10
        elif choice == 3:
            print ("Heu... tu te perd dans les égouts pendant des heures et meurs de manière pitoyable\n\nglou glou glou")
            life = 0
        else :
            print ("Tu ne peux pas faire ça !")
            continue
        donj += 1

    while donj == 1 and life > 0:
        print ("toto")
        choice = int ( input ("Que faite vous ?\n1:tata  !\n2:titi  ?\n3:tutu  !\n") )
        if choice == 1:
            print ("tata")
            score += 5
            life -= 1
        elif choice == 2:
            print ("titi")
            score += 10
        elif choice == 3:
            print ("tutu")
            life = 0
        else :
            print ("Tu ne peux pas faire ça !")
            continue
        donj += 1


    print (f"\n the end. \n\n   Score = {score} \n")
    cont = input ("Continue ? Y/N").lower
    # Jc'onnaissait pas lower c'est quand j'ai fait vérifier mon code qu'il m'a parlé de ça.
    if cont == "y":
        donj = 0
        life = 3
        score = 0
        continue
    else :
        print (f"\n----Game over----\n\n")