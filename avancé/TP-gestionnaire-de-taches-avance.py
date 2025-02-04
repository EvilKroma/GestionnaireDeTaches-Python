#     ___           ___
#    /\  \         /\  \
#    \:\  \       /::\  \
#     \:\  \     /:/\:\  \
#     /::\  \   /::\~\:\  \
#    /:/\:\__\ /:/\:\ \:\__\
#   /:/  \/__/ \/__\:\/:/  /
#  /:/  /           \::/  /
#  \/__/             \/__/


# Énoncé du TP : Gestionnaire de tâches

# Objectifs (Niveau avancé) :  
# Créer un programme Python permettant de gérer une liste de tâches stockées dans un fichier JSON. Ce gestionnaire de tâches doit inclure les fonctionnalités suivantes :
# 1. Ajouter une tâche.
# 2. Afficher toutes les tâches.
# 3. Modifier le statut d'une tâche (par exemple : "à faire", "en cours", "terminée").
# 4. Supprimer une tâche.
# 5. Sauvegarder automatiquement les modifications dans un fichier JSON.



# Exigences fonctionnelles :
# 1. Format du fichier JSON :
#    - Les tâches doivent être stockées dans une liste dans le fichier JSON, et chaque tâche doit contenir les informations suivantes :
#      - Un identifiant unique (`id`).
#      - Une description (`description`).
#      - Un statut (`statut`).

#    Exemple de fichier JSON :
#    {
#        "taches": [
#            {
#                "id": 1,
#                "description": "Apprendre Python",
#                "statut": "à faire"
#            },
#            {
#                "id": 2,
#                "description": "Compléter le TP",
#                "statut": "en cours"
#            }
#        ]
#    }


# 2. Fonctionnalités :
#    - Ajouter une tâche avec une description et un statut par défaut ("à faire").
#    - Afficher toutes les tâches avec leur identifiant, description et statut.
#    - Modifier le statut d'une tâche existante.
#    - Supprimer une tâche en fournissant son identifiant.
#    - Sauvegarder toutes les modifications dans le fichier JSON.

# 3. Interface utilisateur :
#    - Le programme doit afficher un menu permettant de choisir parmi les options ci-dessus.
#    - Le menu doit continuer à apparaître jusqu'à ce que l'utilisateur choisisse de quitter.





# # Algorithme
# # ----------

# 1. Initialisation :
#    - Charger les données du fichier JSON :
#      - Si le fichier existe, lire son contenu.
#      - Sinon, initialiser une structure vide (`{"taches": []}`).

# 2. Boucle principale :
#    - Afficher un menu avec les options suivantes :
#      1. Ajouter une tâche.
#      2. Afficher toutes les tâches.
#      3. Modifier le statut d'une tâche.
#      4. Supprimer une tâche.
#      5. Quitter.

# 3. Ajouter une tâche :
#    - Demander une description à l'utilisateur.
#    - Générer un identifiant unique en fonction de la longueur actuelle de la liste.
#    - Ajouter la nouvelle tâche avec un statut par défaut ("à faire").
#    - Confirmer l'ajout.

# 4. Afficher les tâches :
#    - Parcourir la liste des tâches et afficher chaque tâche (ID, description, statut).
#    - Si aucune tâche n'est disponible, afficher un message approprié.

# 5. Modifier le statut d'une tâche :
#    - Demander à l'utilisateur l'identifiant de la tâche à modifier.
#    - Rechercher cette tâche dans la liste.
#    - Si elle est trouvée, demander le nouveau statut (parmi "à faire", "en cours", "terminée").
#    - Mettre à jour la tâche et confirmer la modification.
#    - Si la tâche n'est pas trouvée, afficher un message d'erreur.

# 6. Supprimer une tâche :
#    - Demander à l'utilisateur l'identifiant de la tâche à supprimer.
#    - Rechercher cette tâche dans la liste.
#    - Si elle est trouvée, la supprimer.
#    - Confirmer la suppression.
#    - Si la tâche n'est pas trouvée, afficher un message d'erreur.

# 7. Sauvegarder les données :
#    - Avant de quitter le programme, sauvegarder toutes les modifications dans le fichier JSON.

# 8. Quitter le programme :
#    - Afficher un message d'adieu et sortir de la boucle principale.
