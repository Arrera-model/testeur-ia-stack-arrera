from objet.ArreraIALoad import ArreraIALoad


if __name__ == '__main__':
    print("Démonstration de la classe ArreraIALoad pour un chargement direct de modèle.\n")

    try:
        # 1. Charger notre chatbot
        # Note : Assurez-vous que les chemins sont corrects par rapport à l'endroit où vous exécutez le script.
        chatbot = ArreraIALoad()

        # 2. Envoyer des requêtes si le modèle est bien chargé
        if chatbot.loadModel(model_directory="model_test",nameModel="test_model.keras"):
            print("\n--- Test du chatbot ---")

            prompt1 = "Salut, comment ça va ?"
            response1 = chatbot.send_request(prompt1)
            print(f"Vous: {prompt1}")
            print(f"Bot: {response1}\n")

            prompt2 = "Quels sont vos horaires ?"
            response2 = chatbot.send_request(prompt2)
            print(f"Vous: {prompt2}")
            print(f"Bot: {response2}\n")

            prompt3 = "adieu"
            response3 = chatbot.send_request(prompt3)
            print(f"Vous: {prompt3}")
            print(f"Bot: {response3}\n")

    except FileNotFoundError as e:
        print(f"Erreur de chemin: {e}")
        print("Veuillez vérifier que les fichiers 'chatbot_model_fr.h5', 'words.pkl', 'classes.pkl', et 'intents_fr.json' existent.")
    except Exception as e:
        print(f"Une erreur inattendue est survenue lors de la démonstration : {e}")