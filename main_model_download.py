from model_downloader.model_downloader import model_downloader

def use_model_download():
    downloader = model_downloader()
    print("Teste de model downloader")
    v = input("1. Voir les modele disposnible\n"
              "2. Voir le detail d'un modele\n"
              "3. Voir les model telecharger"
              "# ")

    try :
        v = int(v)
    except:
        print("Valeur invalide")

    match v :
        case 1 :
            print(downloader.get_model_list())
        case 2 :
            print("Liste des modeles disponible")

            for model in downloader.get_model_list():
                print(f"- {model}")

            print("___________________")
            v = input("Modele : ")
            if v in downloader.get_model_list():
                name,url,description = downloader.get_data_model(v)
                print(f"name : {name}\nurl : {url}\ndescription : {description}")
            else :
                print("Modele non disponible")
            print("___________________")
        case 3 :
            print("Modele telecharger : ")
            for v in downloader.get_model_download():
                print(f"- {v}")

        case _ :
            print("Valeur invalide")