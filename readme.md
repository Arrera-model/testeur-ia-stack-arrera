# Explication des classes

## DataLoader

Objet qui sera chargé des données d’entraînement pour le modèle

### Paramètre d’entrée du constructeur

Prend en paramètre json_file qui correspond à l’emplacement du fichier JSON de données

### Méthodes

**load_data** : Charge le fichier JSON et retourne les listes nécessaires pour l’entraînement. (sentences : list, labels : numpy.array, classes : list)
**save_classe_file** : Sauvegarde les noms des classes dans un fichier JSON (obligatoirement)
**encoding_label** : Ce changement de l’encodage des labels (String → Int)


## ModelTrainer

Objet qui gère la compilation et l’entraînement du réseau de neurones.

### Paramètre d’entrée du constructeur

L’objet ModelTrainer ne prend aucun paramètre au constructeur.

### Méthodes

- **create_vectorizer** : Crée le vectorizer qui est obligatoire pour la création du modèle.
- **get_vectorizer** : Retourne le vectorizer créé (peut être utile).
- **createModel** : Crée un modèle avec la classe ModelBuilder. Ne prend en paramètre que num_classes.
- **loadModel** : Prend un modèle déjà chargé en paramètre.
- **train** : Entraîne le modèle.
- **save** : Sauvegarde le modèle entraîné dans un fichier .keras.

### Utilisation 

Si vous voulez créer un modèle pour l’entraîner, utilisez la méthode **createModel**, sinon utilisez la méthode **loadModel**.

## ArreraIALoad

Charge et exécute directement des modèles d’IA à partir de leurs fichiers.  
Cette classe agit comme un conteneur pour un modèle chargé en mémoire.

### Methode 

#### Private 

- **__predict_arrera_2026_model** : Gère l’envoi de requêtes au modèle de texte d’Arrera. Prend en paramètre *sentence*, qui correspond à la phrase de l’utilisateur, et *confidence_threshold*, qui correspond au seuil de confiance.
- **__predict_gguf_model** : Gère l’envoi de requêtes à des modèles locaux (.gguf) chargés au préalable

### Public

- **send_request** : Permet d’envoyer des requêtes au modèle chargé. Prend les mêmes paramètres que les méthodes privées *predict* correspondant à chaque modèle.
- **loadArreraModel2026** : Charge les modèles d’IA développés par Arrera en 2026. 
- **load_model_gguf** : Charge les modèles d’IA téléchargés en local au format .gguf 


