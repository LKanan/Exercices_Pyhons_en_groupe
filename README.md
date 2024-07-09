# Exercices_Pyhons_en_groupe
Projet qui va permettre de prendre ne main les commandes git-github pour le travail en equipe en ligne
##Instructions
- Inserez les fichiers de votre exercice dans le dossier correspondant
- Creez vos branches pour eviter des conflits
## Les questions sont les suivantes :
### Exercice 6
`(Caldie & Lucien)`  
Un administrateur d’un site web veut assurer un maximum de sécurité pour les utilisateurs du site. Pour ceci
il décide de réaliser une application qui évalue la force des mots de passe des différents utilisateurs du site,
sachant qu’un mot de passe est une chaine de caractères qui ne comporte pas d’espaces et de lettres accentuées.
La force d’un mot de passe varie, selon la valeur d’un score calculé, de ‘Très faible’ jusqu’à ‘Très fort’ :
 - Si le score <20, la force du mot de passe est ‘Très faible’
 - Sinon si le score<40, la force d’un mot de passe est ‘Faible’
 - Sinon si le score <80, la force du mot de passe est ‘Fort’
 - Sinon la force du mot de passe est ‘Très fort’
Le score se calcule en additionnant des bonus et en retranchant des pénalités.
Les bonus attribués sont :
 - Nombre total de caractères * 4
 - (Nombre total de caractères – nombre de lettres majuscules) * 2
 - (Nombre total de caractères – nombre de lettres minuscules) * 3
 - Nombre de caractères non alphabétiques * 5
Les pénalités imposées sont :
 - La longueur de la plus longue séquence de lettres minuscules * 2
 - La longueur de la plus longue séquence de lettres majuscules * 3

Exemple :

Pour le mot de passe ‘P@cSI_promo2017’, le score se calcule comme suit :
La somme de bous = 15*4 + (15-3) *2 + (15-6) *3+6*5=141
 - Le nombre total de caractères = 15
 - Le nombre de lettres majuscules = 3
 - Le nombre de lettres minuscules=6
 - Le nombre de caractères non alphabétiques =6
La somme des pénalités = 5*2+2*2=14
 - La longueur de la plus longue séquence de lettres minuscules(‘promo’) =5
 - La longueur de la plus longue séquence de lettres majuscules(‘SI’) =2
Le score final = 141-14=127 ; puisque 127>80 alors le mot de passe est considéré comme ‘Très fort’

#### Travail demandé :
- [ ] (1) Ecrire une fonction NbCMin(pass) qui retourne le nombre de caractères minuscules.
- [ ] (2) Ecrire une fonction NbCMaj(pass) qui retourne le nombre de caractères majuscules.
- [ ] (3) Ecrire une fonction NbCAlphapass) qui retourne le nombre de caractères non alphabétiques.
- [ ] (4) Ecrire une fonction LongMaj(pass) retourne la longueur de la plus longue séquence de lettres majuscules.
- [ ] (5) Ecrire une fonction LongMin(pass) retourne la longueur de la plus longue séquence de lettres minuscules.
- [ ] (6) Ecrire une fonction Score(pass) qui affiche le score d’un mot de passe

### Exercice 7
`(Glodie & Gloria)`  
Soit un fichier typé intitulé concours.txt qui comporte les enregistrements relatifs aux candidats d’un
concours. Chaque enregistrement est composé de : NCIN, NOM, PRENOM, AGE, DECISION :
(type contenant les identificateurs suivants : admis, refusé, ajourné), et séparé par point virgule ( ;).

#### Travail demandé :
- [ ] (1) Définir la fonction saisir() qui permet de remplir les données relatives aux candidats dans le fichier concours.txt
- [ ] (2) Définir la fonction admis() qui permet créer le fichier admis.txt comportant les données relatives aux candidat admis
- [ ] (3) Afin de sélectionner en priorité les candidats admis et âgés moins de 30 ans, créer la fonction attente() qui produira 
à partir du fichier admis.txt, un nouveau fichier intitulé attente.txt comportant les données relatives aux candidats admis 
et âgés plus que 30 ans. Une ligne du fichier attente.txt comprend le NCIN, le NOM et PRENOM d’un candidat séparés par point virgule ( ;).
- [ ] (4) Définir la fonction statistiques(dec) qui permet de retourner le pourcentage des candidats pour la décision dec (admis, refusé et ajourné).
Exemple : Le pourcentage des candidats admis = ( Nombre des candidats admis Nombre des
candidats)*100
- [ ] (5) Définir la fonction supprimer() qui supprimera du fichier admis.txt les candidat âgés plus que 30