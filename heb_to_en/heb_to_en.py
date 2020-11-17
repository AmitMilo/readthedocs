import sys

def map_heb_to_en(text: str):
    heb_to_en_map = {
        "א":"t",
        "ב":"c",
        "ג": "d",
        "ד": "s",
        "ה": "v",
        "ו": "u",
        "ז": "z",
        "ח": "j",
        "ט": "y",
        "י": "h",
        "כ": "f",
        "ל": "k",
        "מ": "n",
        "נ": "b",
        "ס": "x",
        "ע": "g",
        "פ": "p",
        "צ": "m",
        "ק": "e",
        "ר": "r",
        "ש": "a",
        "ת": ",",
        "/": "q",
        "׳": "w",
        "ף": ";",
        "ך": "l",
        "ץ": ".",
        "ם": "o",
        "ן": "i",
    }

    return text.translate(text.maketrans(heb_to_en_map))


if __name__ == '__main__':
    print(map_heb_to_en(sys.argv[1]))