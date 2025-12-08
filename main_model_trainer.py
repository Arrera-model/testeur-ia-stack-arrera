from objet.ModelTrainer import ModelTrainer
from objet.DataLoader import DataLoader

def model_trainer_bluider(dataset_file:str,classe_file_path:str,model_file_path:str):
    loader = DataLoader(dataset_file)
    print("Loader charger")

    sentences, labels_raw, classes = loader.load_data()

    train_y = loader.encoding_label()
    print(f"Données chargées : {len(sentences)} phrases détectées.")

    if not loader.save_classe_file(classe_file_path):
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

    trainer.save(model_file_path)
    print("Enregistrement du model")

def model_trainer(dataset_file:str,classe_file_path:str,model_file_path:str):
    loader = DataLoader(dataset_file)
    print("Loader charger")

    sentences, labels_raw, classes = loader.load_data()

    train_y = loader.encoding_label()
    print(f"Données chargées : {len(sentences)} phrases détectées.")

    if not loader.save_classe_file(classe_file_path):
        return
    print("Fichier classe.json sauvegardé.")

    trainer = ModelTrainer()
    print("Initilisation de l'entrainer de model")

    trainer.loadModel(model_file_path)
    print("Model charger")

    trainer.train(sentences,train_y)
    print("Entrainement reussi")