from loader.ArreraIALoad import ArreraIALoad
from colorama import Fore, Style

def use_model_gemma(dir:str):
    bot = ArreraIALoad()

    bot.load_model_gguf(dir)

    while True:
        user_input = input(Fore.CYAN + "Vous: " + Style.RESET_ALL)

        if user_input.lower() in ["quit", "exit", "q"]:
            break

        reponse = bot.send_request(user_input)
        print(Fore.MAGENTA + f"Bot: {reponse}")