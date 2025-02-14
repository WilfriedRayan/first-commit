"""import random
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 4



def poser_question() :

    a = random.randint (NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint (NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint (0, 1)
    operateur_str = "+"
    if o == 1 :
        operateur_str = "*"
    reponse_str = input(f" Calculez: {a} {operateur_str} {b} = ")
    reponse_int = int(reponse_str)
    calcul = a+b 
    if o == 1 :
        calcul = a*b
    if reponse_int== calcul :
        return True
    return False       


nb_points = 0

for i in range (0 , NB_QUESTIONS) :
    print (f"Question n°{i+1} sur {NB_QUESTIONS} ?")
    if poser_question () :
        print("Reponse Correcte")
        nb_points += 1
    else :
        print("Reponse incorrecte")
    print ()


print(f"Votre note est : {nb_points} / {NB_QUESTIONS}")

moyenne = int(NB_QUESTIONS/2)

if nb_points == NB_QUESTIONS :
    print ("Excellent")
elif nb_points == 0 :
    print("Revisez vos maths")
elif nb_points == moyenne :
    print("pas mal")
else :
    print("peut mieux faire")"""
    


"""import turtle

def carre (taille) :

    t = turtle.Turtle()

    for i in range (0,4):
        t.forward(taille)
        t.left(90)
        
def carres(taille_depart , nb) :
    for i in range(0 , nb) :
        taille = (i+1)*taille_depart
        carre(taille)
    

carres(10, 10)
turtle.done()"""

def convert_inches_to_cm(inches):
    return inches * 2.54

def convert_cm_to_inches(cm):
    return cm * 0.394

def main():
    print("Bienvenue dans le programme de conversion d'unités !")
    print("1 - Convertir de pouces vers centimètres")
    print("2 - Convertir de centimètres vers pouces")
    
    # Choisir le type de conversion
    choice = input("Entrez votre choix (1 ou 2) : ").strip()
    
    if choice == "1":
        unit = "pouces"
        conversion_func = convert_inches_to_cm
        output_unit = "cm"
    elif choice == "2":
        unit = "centimètres"
        conversion_func = convert_cm_to_inches
        output_unit = "pouces"
    else:
        print("Choix invalide. Fin du programme.")
        return
    
    while True:
        # Demander la valeur à convertir
        value = input(f"Entrez la valeur en {unit} à convertir (ou 'q' pour quitter) : ").strip()
        
        if value.lower() == 'q':
            print("Merci d'avoir utilisé le programme. Au revoir !")
            break
        
        try:
            value = float(value)
            converted_value = conversion_func(value)
            print(f"{value} {unit} = {converted_value:.2f} {output_unit}")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
        
if __name__ == "__main__":
    main()