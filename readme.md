# Explication des classes

## ModelTrainer

Objet qui gère la compilation et l’entraînement du réseau de neurones.

### Méthodes

- **train** : Entraîne le modèle.
- **save** : Sauvegarde le modèle entraîné dans un fichier .h5.

## ModelBuilder

Objet qui s’occupe de créer le modèle.

### Méthodes

- **build** : Construit le modèle avec l’architecture du modèle Keras.

## ArreraIALoad

Charge et exécute directement des modèles d'IA à partir de leurs fichiers.
Cette classe agit comme un conteneur pour un modèle chargé en mémoire.

### Methode 

#### Private 

**__loadArreraModel2026** : Charge les modeles d'IA crée par Arrera 
**__sendRequetteArreraTextModel** : Gere l'envoie de requette au modele de texte d'Arrera

### Public

**send_request** : Permet d'envoyer des requette au model charger


