# Explication des classes

## ModelTrainer

Objet qui gère la compilation et l’entraînement du réseau de neurones.

### Parametre d'entrer du constructeur

La class ModelTrainer prend  aucun parametre au constructeur

### Méthodes

- **createModel** : Cree un model avec la class ModelBuilder. Prend en parametre les memes parametre que le constructeur ModelBuilder.
- **loadModel** : Prend un model deja charger en parametre.
- **train** : Entraîne le modèle.
- **save** : Sauvegarde le modèle entraîné dans un fichier .keras.

### Utilisation 

Si vous voulez cree un model pour l'entrainer utiliser la methode **createModel** sinon utiliser la methode **loadModel**.

## ArreraIALoad

Charge et exécute directement des modèles d'IA à partir de leurs fichiers.
Cette classe agit comme un conteneur pour un modèle chargé en mémoire.

### Methode 

#### Private 

**__loadArreraModel2026** : Charge les modeles d'IA crée par Arrera 
**__sendRequetteArreraTextModel** : Gere l'envoie de requette au modele de texte d'Arrera

### Public

**send_request** : Permet d'envoyer des requette au model charger


