# Explication des classes

## Tokeniser

Objet qui sert à gérer tout ce qui concerne la tokenisation.

Dans le constructeur de la classe, l'objet s’assure que les paquets **punkt** et **punkt_tab** soient bien téléchargés sur la machine pour éviter tout problème.

### Méthodes

- **tokenize** : Découpe une phrase en mots.
- **stem** : Réduit un mot à sa racine si le stemmer est actif.
- **clean_sentence** : Combine tokenisation et stemming pour une phrase complète.

## DataGestion

Objet qui sert à gérer le chargement des données, le prétraitement et la création de vecteurs d’entraînement.

### Méthodes

- **load_and_process** : Charge le JSON et prépare le vocabulaire (stemming).
- **setDirClassePKLFile** : Permet de définir l’emplacement où le fichier **classes.pkl** sera enregistré.
- **setDirWorkPKLFile** : Permet de définir l’emplacement où le fichier **words.pkl** sera enregistré.
- **create_training_data** : Génère les vecteurs X (Bag of Words) et Y (One-Hot labels).

## ModelTrainer

Objet qui gère la compilation et l’entraînement du réseau de neurones.

### Méthodes

- **train** : Entraîne le modèle.
- **save** : Sauvegarde le modèle entraîné dans un fichier .h5.

## ModelBuilder

Objet qui s’occupe de créer le modèle.

### Méthodes

- **build** : Construit le modèle avec l’architecture du modèle Keras.
