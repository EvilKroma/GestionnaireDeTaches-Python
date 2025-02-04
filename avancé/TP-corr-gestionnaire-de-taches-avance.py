





































import json

# Initialiser le fichier JSON
fichier = "taches.json"

try:
    # Charger les données existantes si le fichier existe
    with open(fichier, "r") as file:
        taches = json.load(file)
except FileNotFoundError:
    # Si le fichier n'existe pas, créer une structure vide
    taches = {"taches": []}

def ajouter_tache():
    """Ajoute une nouvelle tâche."""
    description = input("Entrez la description de la tâche : ")
    # Générer un ID unique pour la tâche
    nouvel_id = len(taches["taches"]) + 1
    nouvelle_tache = {"id": nouvel_id, "description": description, "statut": "à faire"}
    taches["taches"].append(nouvelle_tache)
    print("Tâche ajoutée avec succès !")

def afficher_taches():
    """Affiche toutes les tâches."""
    if not taches["taches"]:
        print("Aucune tâche à afficher.")
    else:
        for tache in taches["taches"]:
            print(f'ID: {tache["id"]}, Description: {tache["description"]}, Statut: {tache["statut"]}')

def modifier_statut():
    """Modifie le statut d'une tâche."""
    try:
        id_tache = int(input("Entrez l'ID de la tâche à modifier : "))
        for tache in taches["taches"]:
            if tache["id"] == id_tache:
                print("Statuts possibles : [à faire, en cours, terminée]")
                nouveau_statut = input("Entrez le nouveau statut : ")
                if nouveau_statut in ["à faire", "en cours", "terminée"]:
                    tache["statut"] = nouveau_statut
                    print("Statut mis à jour avec succès !")
                else:
                    print("Statut invalide. Aucun changement effectué.")
                return
        print("Tâche non trouvée.")
    except ValueError:
        print("Veuillez entrer un ID valide.")

def supprimer_tache():
    """Supprime une tâche par son ID."""
    try:
        id_tache = int(input("Entrez l'ID de la tâche à supprimer : "))
        for tache in taches["taches"]:
            if tache["id"] == id_tache:
                taches["taches"].remove(tache)
                print("Tâche supprimée avec succès !")
                return
        print("Tâche non trouvée.")
    except ValueError:
        print("Veuillez entrer un ID valide.")

# Boucle principale
while True:
    print("\nMenu :")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Modifier le statut d'une tâche")
    print("4. Supprimer une tâche")
    print("5. Quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        ajouter_tache()
    elif choix == "2":
        afficher_taches()
    elif choix == "3":
        modifier_statut()
    elif choix == "4":
        supprimer_tache()
    elif choix == "5":
        # Sauvegarder les données avant de quitter
        with open(fichier, "w") as file:
            json.dump(taches, file, indent=4)
        print("Données sauvegardées. Au revoir !")
        break
    else:
        print("Option invalide, veuillez réessayer.")
