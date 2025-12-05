from objet.tokeniser import Tokeniser

def main():
    print("=== Démarrage du programme de test ===\n")

    # 1. Instanciation de la classe
    print("1. Création de l'instance Tokeniser...")
    try:
        t = Tokeniser()
        print("-> Succès : Instance créée.\n")
    except Exception as e:
        print(f"-> Erreur critique : {e}")
        exit()

    # 2. Test de la méthode tokenize()
    phrase_simple = "Bonjour tout le monde."
    print(f"2. Test de tokenize() sur : '{phrase_simple}'")
    tokens = t.tokenize(phrase_simple)
    print(f"-> Résultat : {tokens}")
    print("-" * 20)

    # 3. Test de la méthode stem() (Mots individuels)
    mots_a_tester = ["Manger", "Mangé", "Mangeais", "Chevaux", "Cheval"]
    print("3. Test de stem() sur des variations de mots :")
    for mot in mots_a_tester:
        racine = t.stem(mot)
        print(f"-> Mot : {mot:10} | Racine : {racine}")
    print("-" * 20)

    # 4. Test de la méthode clean_sentence() (Phrase complète)
    phrase_complexe = "Les chats mangent des souris dans le jardin."
    print(f"4. Test de clean_sentence() sur : '{phrase_complexe}'")
    cleaned = t.clean_sentence(phrase_complexe)
    print(f"-> Résultat : {cleaned}")

    # Vérification visuelle
    attendu = ['le', 'chat', 'mang', 'de', 'souris', 'dan', 'le', 'jardin', '.']
    print(f"-> Attendu (approx) : {attendu}")

    print("\n=== Fin des tests ===")

if __name__ == "__main__":
    main()