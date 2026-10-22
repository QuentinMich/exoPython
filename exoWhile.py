i = 1
while i <= 9 :
    print (i)
    i += 1
print (i)

while 2 <= i:
    print (i)
    i -= 1
print (i)

# j'ai voulu utiliser qu'une valeur i parce que je pouvais le faire tout simplement 

r=10

while r > 0 :
    print (r*2)
    r -= 1
 
# oupsie j'ai oublié qu'on travaillais while

num = [423,5435,654,234,765]
i = 0
toto = 0

# print (sum(num))

while i < len(num):
    toto += num[i]
    i += 1

print (toto)

# plutot simple une seule commande

c = [14,16,1,17,8]
i = 0
m = 0

# print (sum(c)/len(c))

while i < len(c):
    m += c[i]
    i += 1

moyenne = m / len(c)

print (moyenne)

# une commande avec un calule a l'interieur pour le plaisir j'ai fait en sorte que ce soit peu importe le nombre de notes

m = 0
count = 0
numbers = [0]
while count < 101:
    numbers.append(count)
    count += 1
    m += numbers[count]
print (m)

# ça avait l'air compliqué mais en vrai avec toutes les commmandes qu'on a on le fait pépouse

while input("Vas tu réussir dans le dev ? ").lower() !="oui":
    continue
print ("\n\n\n\n\nBon toutou")
# BANG BANG EASY WIN BLAP BLAP BLAP