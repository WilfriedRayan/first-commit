
def afficher_information_personne(nom,age):
   print (f"Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
   print (f"L'anne prochain vous aurez " + str(age+1) + " ans")

   if age == 17 :
      print ("vous est majeur")
   elif age == 18 :
      print("vous est majeur : Felicitation")
   elif age > 60 :
      print("vous etes senior")
   elif age >= 18 :
      print("vous etes majeur")
   elif age < 10 :
      print("vous est enfant")
   else :
      print("vous est mineur")

def demande_nom():
   reponse_nom = ""
   while reponse_nom == "" : 
      reponse_nom = input("Quel est ton nom ? ")
   return reponse_nom 

def demande_age(nom_personne):
   age_int = 0
   while age_int == 0:
      age_chaine  = input( nom_personne + " quel age as-tu ? ")
      try:
         age_int = int(age_chaine) + 1
      except ValueError:
         print("ERREUR: Vous devez rentrer un nombre pour l'age")
   return age_int
#________________________________________________________________________________

# demander le nom
nom1 = "personne1"
nom2 = "personne2"

# demander l'age
age1 = demande_age(nom1)
age2 = demande_age(nom2)

# Afficher les resulta
afficher_information_personne(nom1, age1)
afficher_information_personne(nom2, age2) 

#la bouble for
for i in range (0 , 3) :
   nom ="personne" + str(i+1)
   age = demande_age(nom)
   afficher_information_personne(nom, age)
