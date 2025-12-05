from objet.ModelTrainer import ModelTrainer
import numpy as np
import os


if __name__ == "__main__":
    print("=== TEST DU MODEL TRAINER ===")

    # 1. Configuration des dimensions pour le test
    # Exemple : un "sac de mots" (bag of words) de 50 mots et 3 intentions (classes) possibles
    INPUT_SIZE = 50
    OUTPUT_SIZE = 3
    NUM_SAMPLES = 20  # Nombre d'exemples d'entraînement factices

    # 2. Génération de données factices (Dummy Data)
    print(f"Génération de {NUM_SAMPLES} données factices...")

    # X : Des vecteurs aléatoires de 0 et 1 (simulant un bag of words)
    train_x = np.random.randint(2, size=(NUM_SAMPLES, INPUT_SIZE))

    # Y : Encodage One-Hot (catégoriel) pour la sortie
    # On crée une matrice de zéros et on met un '1' aléatoire par ligne
    train_y = np.zeros((NUM_SAMPLES, OUTPUT_SIZE))
    for i in range(NUM_SAMPLES):
        random_class = np.random.randint(0, OUTPUT_SIZE)
        train_y[i, random_class] = 1

    print(f"Shape X: {train_x.shape}")
    print(f"Shape Y: {train_y.shape}")

    # 3. Initialisation du Trainer
    try:
        trainer = ModelTrainer(input_shape=INPUT_SIZE, output_shape=OUTPUT_SIZE)
        print("Initialisation réussie.")
    except Exception as e:
        print(f"Erreur lors de l'initialisation : {e}")
        exit()

    # 4. Lancement de l'entraînement
    # On réduit les epochs à 5 pour que le test soit rapide
    try:
        trainer.train(train_x, train_y, epochs=5, batch_size=5)
    except Exception as e:
        print(f"Erreur lors de l'entraînement : {e}")
        exit()

    # 5. Sauvegarde
    try:
        trainer.save('model_test/test_model.keras')

        # Vérification que le fichier existe bien
        if os.path.exists('model_test/test_model.keras'):
            print("Succès : Le fichier du modèle a bien été créé sur le disque.")
            # Nettoyage du fichier de test (optionnel)
            # os.remove('test_model.h5')
        else:
            print("Erreur : Le fichier n'a pas été trouvé après la sauvegarde.")

    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")