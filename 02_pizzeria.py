pizNbr = int ( input ("Combien de pizzas ? ") )
pizPrc = int ( input ("Prix des pizzas ? ") )

totHT = pizNbr * pizPrc
disc = totHT * 0.1

if pizNbr > 5:
    totWT = totHT - disc
    reduc = f" -{disc} €"
else :
    totWT = totHT
    reduc = " 0.0 € "

if totWT <= 20:
    total = totWT + 3 
    livr = "3.0 €"
else :
    total = totWT
    livr = "Gratuite"

print (f"=== PIZZA TICKET ===\nPizzas : {pizNbr} x {pizPrc} €\nRéduction :{reduc}\nLivraison : {livr}\nTOTAL : {total} €")