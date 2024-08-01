import fontforge
import os
import argparse

# Definisci gli intervalli Unicode da mantenere
intervalli_da_mantenere = [
    (0x0020, 0x007F),  # Basic Latin
    (0x0080, 0x00FF),  # Latin-1 Supplement
    (0x0100, 0x017F),  # Latin Extended-A
    (0x0180, 0x024F),  # Latin Extended-B
    (0x2000, 0x206F),  # Punteggiatura generale
    (0x2070, 0x209F),  # Superscript e subscript
    (0x20A0, 0x20CF),  # Currency
    (0x2100, 0x214F),  # Letterlike Symbols
    (0xFE50, 0xFE6F),  # Small Form Variants
    (0xFF00, 0xFFEF),  # Halfwidth and Fullwidth Forms
    (0xFEFF, 0xFEFF),  # Zero width no break space
]


def get_font_files(directory):
    # Lista per memorizzare i percorsi dei file trovati
    font_files = []

    # Scorre tutti i file nella directory specificata
    for filename in os.listdir(directory):
        # Controlla se il file ha estensione .otf o .ttf
        if filename.endswith(".otf") or filename.endswith(".ttf"):
            # Costruisce il percorso completo del file e lo aggiunge alla lista
            font_files.append({"dir": directory, "name": filename})

    return font_files


def font_reduce(font_file: dict):
    # Carica il font
    font = fontforge.open(os.path.join(font_file["dir"], font_file["name"]))

    # Funzione per verificare se un codice Unicode è in uno degli intervalli
    def unicode_in_intervalli(unicode, intervalli):
        for start, end in intervalli:
            if start <= unicode <= end:
                return True
        return False

    # Elimina i glifi non presenti negli intervalli definiti
    for glifo in font.glyphs():
        if not unicode_in_intervalli(glifo.unicode, intervalli_da_mantenere):
            font.removeGlyph(glifo)

    # Salva il font modificato
    try:
        font.generate(f"reduced_font/{font_file['name']}")
    except Exception as e:
        print(e)
    font.close()


def main():
    # Configurazione del parser per gli argomenti della linea di comando
    parser = argparse.ArgumentParser(
        description="Processa file di font in una directory."
    )
    parser.add_argument(
        "directory", type=str, help="La directory contenente i file di font"
    )

    # Parsing degli argomenti
    args = parser.parse_args()

    # Ottenere tutti i file .otf e .ttf dalla directory specificata
    font_files = get_font_files(args.directory)
    os.makedirs("reduced_font", exist_ok=True)

    # Esegui le operazioni desiderate su ogni file
    for font_file in font_files:
        print(f"Reducing: {font_file['name']}")
        # Esegui qui le tue operazioni sui file font
        font_reduce(font_file)


if __name__ == "__main__":
    main()
