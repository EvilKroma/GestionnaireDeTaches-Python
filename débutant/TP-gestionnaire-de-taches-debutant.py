  #     ___           ___
  #    /\  \         /\  \
  #    \:\  \       /::\  \
  #     \:\  \     /:/\:\  \
  #     /::\  \   /::\~\:\  \
  #    /:/\:\__\ /:/\:\ \:\__\
  #   /:/  \/__/ \/__\:\/:/  /
  #  /:/  /           \::/  /
  #  \/__/             \/__/
########################################
# GESTIONNAIRE DE TACHES - DEBUTANT    #
########################################
# Objectifs (Niveau débutant) : 


# Créer un programme en Python permettant de créer une tâche, de la supprimer et de l'afficher.
# Ce gestionnaire de tâches doit inclure les fonctionnalités suivante : 
# 1. Ajouter une tâche.
# 2. Afficher toutes les tâches.
# 3. Supprimer une tâche.

# ============================================
# Algorithme : Gestionnaire de tâches (Débutant)
# ============================================

# 1. Initialisation :
#    - Créer une liste vide `taches` pour stocker les tâches.

# 2. Boucle principale :
#    - Afficher un menu avec les options suivantes :
#      1. Ajouter une tâche.
#      2. Afficher toutes les tâches.
#      3. Supprimer une tâche.
#      4. Quitter.

# 3. Ajouter une tâche :
#    - Demander une description de tâche à l'utilisateur.
#    - Ajouter cette description à la liste `taches`.
#    - Confirmer l'ajout en affichant un message.

# 4. Afficher les tâches :
#    - Vérifier si la liste `taches` est vide :
#      - Si oui, afficher "Aucune tâche enregistrée."
#      - Sinon, afficher chaque tâche avec son numéro.

# 5. Supprimer une tâche :
#    - Vérifier si la liste `taches` est vide :
#      - Si oui, afficher un message et revenir au menu.
#    - Sinon, afficher la liste des tâches numérotées.
#    - Demander à l'utilisateur de saisir le numéro de la tâche à supprimer.
#    - Vérifier si l'entrée est valide :
#      - Si oui, supprimer la tâche correspondante.
#      - Si non, afficher un message d'erreur.

# 6. Quitter le programme :
#    - Afficher un message d'adieu et sortir de la boucle principale.


taches = ['Tâche 1', 'Tâche 2', 'Tâche 3']


# Ajoute une tâche puis les affiche toutes
def AjouterTache():
    nouvelleTache = input('Tâche à ajouter : ')
    taches.append(nouvelleTache)
    AfficherTaches()
    Init()


# Afficher toutes les tâches
def AfficherTaches():
    if taches:
        print('\nTâches :')
        for i, tache in enumerate(taches, 1):
            print(f"{i}. {tache}")
    else:
        print('Aucune tâche enregistrée.')
    Init()


# Supprimer une tâche
def SupprimerTache():
    if not taches:
        print('Aucune tâche à supprimer.')
    else:
        try:
            tacheASupprimer = int(input('Numéro de la tâche à supprimer : '))
            if 1 <= tacheASupprimer <= len(taches):
                taches.pop(tacheASupprimer - 1)
                print('Tâche supprimée.')
                Init()
            else:
                print('Numéro de tâche invalide.')
        except ValueError:
            print('Entrée invalide. Veuillez entrer un numéro.')


# Quitter le programme
def Quitter():
    print("Merci d'avoir utilisé le gestionnaire de tâches. À bientôt !")


def Init():
    cadre = """\n
 <============================================>
 |                                            |
 |  Choisissez une option :                   |
 |                                            |
 |  1 - Ajouter une tâche                     |
 |  2 - Afficher toutes les tâches            |
 |  3 - Supprimer une tâche                   |
 |  4 - Quitter                               |
 |                                            |
 <============================================>
    """
    print(cadre)

    option = input("Votre choix : ")

    # Gestion des options
    if option == '1':
        AjouterTache()
    elif option == '2':
        AfficherTaches()
    elif option == '3':
        SupprimerTache()
    elif option == '4':
        Quitter()
    else:
        print("Option invalide. Veuillez choisir une option valide.")

Init()
