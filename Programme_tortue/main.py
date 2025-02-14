# Faire  escalier

import turtle

""""
def escalier(taille, nb) :
    t = turtle.Turtle()
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)
    return escalier
"""

def carre(taille) :
    for i in range(0, 4) :
     t.forward(taille)
     t.left(90)

def carres(taille_depart, nb):
    for i in range (0, nb) :
     taille = (i+1)*taille_depart
     carre(taille)


t = turtle.Turtle()
# 5 marches de 30 pixels
# escalier(9, 3)

#carre de 10 pixels
#carre(50)
#carre(100)

# 4 Carre de 10 pixels
carres(10, 10)
turtle.done()

    

