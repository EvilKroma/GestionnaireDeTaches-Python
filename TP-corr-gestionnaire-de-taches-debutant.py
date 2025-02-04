





































# Gestionnaire de tâches - Niveau Débutant
# ------------------------------------------------
# Ce programme permet d'ajouter, afficher et supprimer des tâches.

# Étape 1 : Initialiser une liste pour stocker les tâches
taches = []  # Liste vide au démarrage

# Étape 2 : Définir les fonctions du programme

def ajouter_tache():
    """Ajoute une nouvelle tâche à la liste."""
    description = input("Entrez la description de la tâche : ")
    taches.append(description)  # Ajout à la liste
    print(f"Tâche ajoutée : {description}\n")

def afficher_taches():
    """Affiche toutes les tâches enregistrées."""
    if not taches:  # Vérifier si la liste est vide
        print("Aucune tâche enregistrée.\n")
    else:
        print("\n📋 Liste des tâches :")
        for index, tache in enumerate(taches, start=1):  # Affichage numéroté
            print(f"{index}. {tache}")
        print()  # Saut de ligne pour plus de lisibilité

def supprimer_tache():
    """Supprime une tâche en fonction de son numéro."""
    afficher_taches()  # Afficher les tâches avant de demander une suppression
    if not taches:  # Vérifier si la liste est vide avant de supprimer
        return  # Si aucune tâche, retour au menu

    try:
        choix = int(input("Entrez le numéro de la tâche à supprimer : ")) - 1
        if 0 <= choix < len(taches):
            tache_supprimee = taches.pop(choix)  # Supprimer l'élément sélectionné
            print(f"Tâche supprimée : {tache_supprimee}\n")
        else:
            print("Numéro invalide. Aucune tâche supprimée.\n")
    except ValueError:
        print("Veuillez entrer un nombre valide.\n")

# Étape 3 : Boucle principale avec menu utilisateur
while True:
    print("📌 Gestionnaire de Tâches 📌")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Supprimer une tâche")
    print("4. Quitter")

    choix = input("Choisissez une option (1-4) : ")

    if choix == "1":
        ajouter_tache()
    elif choix == "2":
        afficher_taches()
    elif choix == "3":
        supprimer_tache()
    elif choix == "4":
        print("(づ｡◕‿‿◕｡)づ Au revoir !")
        break  # Quitter la boucle et le programme
    else:
        print("(╯°□°）Option invalide, veuillez réessayer.\n")
