import fontTools.subset as subset
import os
import argparse


def get_font_files(directory):
    font_files = []

    for filename in os.listdir(directory):
        if filename.endswith(".otf") or filename.endswith(".ttf"):
            font_files.append({"dir": directory, "name": filename})

    return font_files


def main():
    # Configurazione del parser per gli argomenti della linea di comando
    parser = argparse.ArgumentParser(
        description="Processa file di font in una directory."
    )
    parser.add_argument(
        "directory", type=str, help="La directory contenente i file di font"
    )
    args = parser.parse_args()

    font_files = get_font_files(args.directory)
    os.makedirs("reduced_font", exist_ok=True)

    for font_file in font_files:
        print(f"Reducing: {font_file['name']}")

        subset.main((
            os.path.join(font_file["dir"], font_file["name"]),
            f"--output-file={os.path.join('reduced_font', font_file["name"])}",
            "--unicodes-file=unicodes.txt"
        ))


if __name__ == "__main__":
    main()
