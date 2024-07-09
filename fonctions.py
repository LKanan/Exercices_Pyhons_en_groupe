import os

def creer_fichier(nom):
  if not(os.path.exists(nom)):
    with open(nom, 'w') as fichier :
      ligne = "{:<{colonne1}} {:<{colonne2}} {:<{colonne3}} {:<{colonne4}} {:<{colonne5}} \n".format('NCIN', 'NOM', 'PRENOM', 'AGE', 'DECISION', colonne1=10, colonne2=10, colonne3=10, colonne4=10, colonne5=10)
      fichier.write(ligne)

def ajout_candidat():
  donnee = []
  informations = ['NCIN', 'NOM', 'PRENOM', 'AGE', 'DECISION']
  print('Veiller completer les informations suivantes :')
  for i in range(0, len(informations)):
    info = input(f'{informations[i]} : ')
    donnee.append(info)

  with open('concours.txt', 'a') as fichier:
    ligne = "{:<{colonne1}} {:<{colonne2}} {:<{colonne3}} {:<{colonne4}} {:<{colonne5}} \n".format(donnee[0], donnee[1], donnee[2], donnee[3], donnee[4], colonne1=10, colonne2=10, colonne3=10, colonne4=10, colonne5=10)
    fichier.write(ligne)

def recuperation_donnee():
  donnee = []
  with open('concours.txt', 'r') as fichier:
    lignes = fichier.readlines()

    for ligne in lignes:
      print(ligne.strip())


def saisir():
  creer_fichier('concours.txt')
  ajout_candidat()
  print("Candidat ajouté avec success")

def admis() :
  print('Candidat admis')
  recuperation_donnee()

def attente():
  print('Plus de 30 ans')

def statistiques():
  print('Statistiques')

def supprimer():
  print('Supprimer')