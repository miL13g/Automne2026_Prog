# Auteur : Émile Bousquet
# Date : 10/09/2026
# Sujet : Demo du cours du 10 septembre 2026

# age = 60
# genre = "masculin"


# if age >= 80:
#     print("très vieux")
# elif age >= 70:
#     print("vieux")
# elif age >= 60:
#     print("petite jeunesse")
# else:
#     print("jeune")

# if age == 81 :
#     print("il a 81 ans")
#     if genre == "masculin":
#         print("c'est un homme de 81 ans")
#     else:
#         print("Cet une femme de 81 ans")
# else:
#     print("il a pas 81 ans")

jour = 2

# match jour:
#     case 1:
#         print("Dimanche")
#     case 2:
#         print("Lundi")
#     case 3:
#         print("Mardi")
#     case 4:
#         print("Mercredi")
#     case 5:
#         print("Jeudi")
#     case 6:
#         print("Vendredi")
#     case 7:
#         print("Samedi")
#     case _:
#         print("Jour Invalide")

# match jour:
#     case 1 | 7:
#         print("Fin de semaine")
#     case _:
#         print("Semaine")

age = 11
if age >= 18:
    statut = "adulte"
else:
    statut = "enfant"

#ou

statut = "adulte" if age >=18 else "enfant"
print(statut)



print("fin")    