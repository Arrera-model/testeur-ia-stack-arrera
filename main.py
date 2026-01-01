import colorama
from main_use_model import use_model_gemma
from main_model_trainer import model_trainer_bluider,model_trainer
from main_model_download import use_model_download

# Initialisation des couleurs pour le terminal
colorama.init(autoreset=True)

def main():
    print("## Programme de teste pour la stack de gestion model d'Arrera ##")
    var = 1
    while var !=0:
        var = input("1. Entrainer et crée un model\n"
                    "2. Entrainer un model deja crée\n"
                    "3. Charger un model local en .gguf\n"
                    "4. Teste de model downloader\n"
                    "0. Quitter\n"
                    "# ")
        try :
            var = int(var)
        except :
            print("Valeur invalide")
            continue

        match var :
            case 1:
                dataset_path = input("Emplacement du dataset : ")
                classe_file_path = input("Emplacement du fichier JSON : ")
                model_file_path = input("Emplacement du model : ")
                model_trainer_bluider(dataset_path,classe_file_path,model_file_path)
                print("Model crée")
            case 2:
                dataset_path = input("Emplacement du dataset : ")
                classe_file_path = input("Emplacement du fichier JSON : ")
                model_file_path = input("Emplacement du model : ")
                model_trainer(dataset_path,classe_file_path,model_file_path)
                print("Model entrainer")
            case 3:
                model_path = input("Emplacement du model local en .gguf : ")
                use_model_gemma(model_path)
            case 4 :
                use_model_download()
            case 0:
                var = 0
                print("Au revoir")
            case _:
                print("Erreur")

if __name__ == "__main__":
    main()