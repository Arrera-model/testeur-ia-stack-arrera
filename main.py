from objet.ArreraIALoad import ArreraIALoad
import colorama
from colorama import Fore, Style

# Initialisation des couleurs pour le terminal
colorama.init(autoreset=True)

def main():
    # Chemins vers vos fichiers générés par l'entraînement
    MODEL_PATH = "model_test/test_model.keras"
    CLASSES_PATH = "model_test/classes.json"

    print(Fore.YELLOW + "Chargement du cerveau en cours...")

    bot = ArreraIALoad()

    if not bot.loadArreraModel2026(MODEL_PATH, CLASSES_PATH):
        print(Fore.RED + "Impossible de lancer le chatbot.")
        return

    print(Fore.GREEN + "\n--- Chatbot Prêt ! (Tapez 'quit' pour quitter) ---")
    print(Style.DIM + f"Seuil de confiance : 70%")

    while True:
        user_input = input(Fore.CYAN + "Vous: " + Style.RESET_ALL)

        if user_input.lower() in ["quit", "exit", "q"]:
            break

        # Prédiction
        tag, confidence = bot.send_request(user_input, confidence_threshold=0.70)

        if tag:
            print(Fore.MAGENTA + f"Bot: [Intention: {tag}] ({confidence:.2%})")
            # Ici, plus tard, vous ajouterez la logique de réponse :
            # if tag == "salutation": print("Bonjour !")
        else:
            print(Fore.RED + f"Bot: Je n'ai pas compris... ({confidence:.2%})")

if __name__ == "__main__":
    main()