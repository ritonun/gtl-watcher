"""
"""
path_pokemon_names_fra = "../data/file/pokemon_names_fr.txt"
path_pokemon_names_eng = ""

path_pokemon_items_fra = ""
path_pokemon_items_eng = ""

supported_language = ["fra", "eng"]


def check_language_is_supported(lang):
    if lang not in supported_language:
        print("Supported language:", supported_language)
        raise ValueError(
            "The language you entered is not supported. You entered: {}".format(lang)
        )


def get_file_pokemon_name(lang):
    check_language_is_supported(lang)
    if lang == "fra":
        path = path_pokemon_names_fra
    elif lang == "eng":
        path = path_pokemon_names_eng
    return path


def get_file_pokemon_item(lang):
    check_language_is_supported(lang)
    if lang == "fra":
        path = path_pokemon_items_fra
    elif lang == "eng":
        path = path_pokemon_items_eng
    return path


def load_pokemon_name(lang):
    pokemon_names = []
    with open(get_file_pokemon_name(lang=lang), "r", encoding="utf-8") as file:
        line = file.readlines()
        line = str(line).replace("\\n", "")
        pokemon_names.append(line)
    return pokemon_names[0]


def load_pokemon_item(lang):
    pokemon_items = []
    with open(get_file_pokemon_item(lang=lang), "r", encoding="utf-8") as file:
        line = file.readlines()
        line = str(line).replace("\\n", "")
        pokemon_items.append(line)
    return pokemon_items[0]


def dict_language_var(lang):
    check_language_is_supported(lang)
    # buy, lvl, currency
    language_dict = {"buy": "Acheter", "lvl": "Niv.", "currency": "$"}
    if lang == "fra":
        pass
    elif lang == "eng":
        language_dict["buy"] = "Buy"
        language_dict["lvl"] = "Lvl."
        language_dict["currency"] = "$"

    return language_dict
