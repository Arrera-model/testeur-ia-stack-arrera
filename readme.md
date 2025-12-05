# Explication des class 

## Tokeniser

Objet qui sert a gerer tout ce qui concerne la tokenisation 

Dans le constructeur de la class l'objet s'assure que le packer punkt et punkt_tab sois bien telecharger sur la machine pour eviter tout probleme 

### Methode 

- tokenize : Découpe une phrase en mots.
- stem : Réduit un mot à sa racine si le stemmer est actif.
- clean_sentence : Combine tokenisation et stemming pour une phrase complète.

## DataGestion 

Objet qui sert gerer le chargement des donnée, le prétraitement et la creation de vecteur d'entrainement

### Methode 

- load_and_process : Charge le JSON et prépare le vocabulaire (Stemming).
- setDirClassePKLFile : Permet de definir l'emplacement des fichier classes.pkl sera enregistrer
- setDirWorkPKLFile : Permet de definir l'emplacement des fichier words.pkl sera enregistrer
- create_training_data : Génère les vecteurs X (Bag of Words) et Y (One-Hot labels).

## ModelTrainer 

Objet qui gère la compilation et l'entraînement du réseau de neurones.

### Methode 

- train : Entraine le model 
- save : Sauvegarde le model entrainer dans un fichier .h5

## ModelBuilder

Objet qui s'occupe de cree le modele  

### Methode 

- build : Contruit le model avec l'architecture du modèle Keras.