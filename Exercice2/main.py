from fonctions import *

def menuPrincipale():
  print('===================================')
  print('1. Ajouter un candidat au concour')
  print('2. Ajouter un candidat admis')
  print('3. Afficher les candidats agés de plus de 30 ans')
  print('4. Afficher le pourcentage de candidats')
  print('5. Supprimer les candidats')
  print('6. Quitter')

def main():
  option = 1
  while option != 6:
    menuPrincipale()
    option = int(input('Veiller entrer une option :'))
    print('\n')

    if option == 1:
      saisir()
    elif option == 2 :
      admis()
    elif option == 3:
      attente()
    elif option == 4:
      statistiques()
    elif option == 5:
      supprimer()
  

if __name__ == '__main__' :
  main()