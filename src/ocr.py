"""
OCR
Optical Character Recognition
"""
import pytesseract
import pandas as pd
import string

import language
import utils

# OCR pytesseract variable
ocr_language = "eng+fra"
custom_config = ""
output = pytesseract.Output.DICT  #STRING, BYTES, DATAFRAME, DICT
custom_timeout = 5  # time in seconds after wich process is terminated
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

global_language = "fra"
pokemon_names = language.load_pokemon_name(global_language) # list of all pokemon name in pokemmo in custom language
language_var = language.dict_language_var(global_language)


class CleanInput:
    def get_level(word):
        level = 0
        try:
            level = word[4:]
            level = int(level)
        except:
            level = 0
        return level

    def get_price(word):
        try:
            price = word[1:]
            price = price.replace(",", "")
            price = int(price)
        except:
            price = -1
        return price

    def clean_word(word):
        all_char = string.printable
        special_chars = all_char[62:].replace("$", "").replace(",", "").replace(".", "")

        cleaned_word = ''
        for char in word:
            if char not in special_chars and char != " ":
                cleaned_word += char
        cleaned_word = cleaned_word.strip()
        return cleaned_word


def get_text_from_image(img_path):
    ocr_data = pytesseract.image_to_data(img_path, lang=ocr_language, config=custom_config, 
                                         output_type=output, timeout=custom_timeout)
    return ocr_data


def keep_line(line):
    keep = False
    for word in line:
        if word.find(language_var["buy"]) != -1:
            keep = True
    return keep


def get_text_line_per_line(ocr_data):
    len_data = len(ocr_data["level"])

    lines = []
    line = []

    for index in range(0, len_data):
        if ocr_data["top"][index] > ocr_data["top"][index - 1] + 10 and index > 0:
            if keep_line(line):
                lines.append(line)
                line = []
        line.append(ocr_data["text"][index])
    return lines[1:]


def get_data_list(table, datetime):
    data = []
    for line in table:
        lvl = None
        name = None
        price = None

        for word in line:
            word = CleanInput.clean_word(word)
            if word.find(language_var["lvl"]) != -1:
                lvl = CleanInput.get_level(word)
            elif word in pokemon_names:
                name = word
            elif word.find(language_var["currency"]) != -1:
                price = CleanInput.get_price(word)
                break

        if lvl == None:
            lvl = 0
        if not name == '':
            data.append([datetime, lvl, name, price])
    return data


def ocr_dataframe(img_path):
    # Get ocr data and clean data
    ocr_data = get_text_from_image(img_path)
    lines = get_text_line_per_line(ocr_data)

    date_time = utils.get_creation_time_of_img(img_path)

    data = get_data_list(lines, date_time)

    # Get panda DataFrame
    df = pd.DataFrame.from_dict(data)
    df.columns = ["Datetime", "Level", "Name", "Price"]
    
    return df
