from objet.gestionnaire_data import gestionnaire_data, Tokeniser,np
import sys


def main():
    # 1. Instanciation du processeur
    # Assure-toi que le fichier 'intents_fr.json' existe bien dans le dossier
    processor = gestionnaire_data(intents_file="data_set/test_intents_fr.json")

    processor.setDirWorkPKLFile("training_file/work.pkl")
    processor.setDirClassePKLFile("training_file/classes.pkl")

    print("--- Démarrage du traitement ---")

    # 2. Chargement et traitement des mots/classes
    print("Chargement et tokenisation des données...")
    if processor.load_and_process():
        print("✅ Données chargées et fichiers 'words.pkl' / 'classes.pkl' créés.")
    else:
        print("❌ Erreur : Impossible de trouver ou lire le fichier d'intentions.")
        sys.exit(1)

    # 3. Création des données d'entraînement (Bag of Words)
    print("Génération des vecteurs d'entraînement...")
    train_x, train_y = processor.create_training_data()

    # 4. Affichage des statistiques pour vérification
    print("\n--- Résumé des données ---")
    print(f"Nombre de documents (patterns) traités : {len(train_x)}")
    print(f"Dimension de l'entrée (vocabulaire)    : {train_x.shape[1]}")
    print(f"Dimension de la sortie (classes)       : {train_y.shape[1]}")

    # 5. Exemple de ce à quoi ressemblent les données
    if len(train_x) > 0:
        print("\nExemple de donnée (premier élément) :")
        print(f"X (Pattern) : {train_x[0]}")
        print(f"Y (Class)   : {train_y[0]}")

    # 6. (Optionnel) Sauvegarde des données prêtes pour le réseau de neurones
    # Tu peux décommenter ces lignes si tu veux sauvegarder les matrices NumPy
    # np.save('train_x.npy', train_x)
    # np.save('train_y.npy', train_y)
    # print("\nDonnées d'entraînement sauvegardées (train_x.npy, train_y.npy).")

    print("\n✅ Prêt pour l'étape d'entraînement du modèle IA.")


if __name__ == "__main__":
    main()