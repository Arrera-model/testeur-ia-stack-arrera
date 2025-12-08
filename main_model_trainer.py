from objet.ModelTrainer import ModelTrainer
from objet.DataLoader import DataLoader

def main():
    loader = DataLoader("model_test/intents.json")
    print("Loader charger")

    sentences, labels_raw, classes = loader.load_data()

    train_y = loader.encoding_label()
    print(f"Données chargées : {len(sentences)} phrases détectées.")

    if not loader.save_classe_file("model_test/classes.json"):
        return
    print("Fichier classe.json sauvegardé.")

    trainer = ModelTrainer()
    print("Initilisation de l'entrainer de model")

    trainer.create_vectorizer(sentences)
    print("Creation du vectorizer")

    trainer.createModel(len(classes))
    print("Creation du model")

    trainer.train(sentences,train_y)
    print("Entrainement reussi")

    trainer.save("model_test/test_model.keras")
    print("Enregistrement du model")

if __name__ == "__main__":
    main()