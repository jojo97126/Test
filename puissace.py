a = int(input("Saisir A "))
b = int(input("Saisir B "))
#resultat = a ** b
resultat = 1
if b>0 :
    for i in range (b):
        resultat *= a
    print("Le resultat est :", resultat)
elif b<0:
    for i in range(-b):
        resultat /= a
    print("le resultat est :", resultat)
elif b == 1:
    print("le resultat est :", a)
else:
    print("le resultat est :", 1)
2
