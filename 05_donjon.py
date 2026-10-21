score = 0
life = 3

print ( "Vous entrez dans le donjon de naheulbeurk, devant vous une porte immense se dresse. ")

while life > 0:
    choice = int ( input ("Que faite vous ?\n1: Je Casse la porte !\n2: Je toque a la porte ?\n3: Je passe par les égouts !\n") )
    if choice == 1:
        print ("Grand malade ! Tu es entendu par la garde et elle t'attaque, tu perd 1 vie mais tu passe. +5 points !")
        score += 5
        life -= 1
        break
    elif choice == 2:
        print ("Toc Toc Toc !\n Un gobelin en costar t'ouvre la porte avec un sourir et te laisse passer, bravo ! +10 points")
        score += 10
        break
    elif choice == 3:
        print ("Heu... tu te perd dans les égouts pendant des heures et meurs de manière pitoyable\n\nglou glou glou")
        life -= 3
    else :
        print ("Tu ne peux pas faire ça !")
        continue

    print ("")
    choice = int ( input ("Que faite vous ?\n1:  !\n2:  ?\n3:  !\n") )
    if choice == 1:
        print ("")
        score += 5
        life -= 1
        break
    elif choice == 2:
        print ("")
        score += 10
        break
    elif choice == 3:
        print ("")
        life -= 3
    else :
        print ("Tu ne peux pas faire ça !")
        continue

print (f"\n----Game over----\n\n   Score : {score} ")