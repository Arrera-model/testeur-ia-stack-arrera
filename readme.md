# Explication des class 

## DataGestion 

Objet qui sert gerer le chargement des donnée, le prétraitement et la creation de vecteur d'entrainement

### Methode 

- load_and_process : Charge le JSON et prépare le vocabulaire (Stemming).
- setDirClassePKLFile : Permet de definir l'emplacement des fichier classes.pkl sera enregistrer
- setDirWorkPKLFile : Permet de definir l'emplacement des fichier words.pkl sera enregistrer
- create_training_data : Génère les vecteurs X (Bag of Words) et Y (One-Hot labels).
