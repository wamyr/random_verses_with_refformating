from bs4 import BeautifulSoup

def clean_html_file(input_file, output_file):
    """Nettoie un fichier HTML et supprime les deux premières lignes du texte extrait."""
    # Charger le contenu du fichier
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Utiliser BeautifulSoup pour parser le HTML
    soup = BeautifulSoup(content, "html.parser")

    # Extraire le texte brut
    text = soup.get_text()

    # Supprimer les deux premières lignes
    lines = text.split("\n")
    cleaned_text = "\n".join(lines[2:])

    # Sauvegarder le texte nettoyé dans un nouveau fichier
    with open(output_file, "w", encoding="utf-8") as output_file:
        output_file.write(cleaned_text)


if __name__ == "__main__":
    # Fichiers d'entrée et de sortie
    input_file = "Notes_verses.txt"  # Remplacez par le chemin de votre fichier d'entrée
    output_file = "../../versets.txt"  # Remplacez par le chemin de votre fichier de sortie

    # Appeler la fonction pour nettoyer le fichier
    clean_html_file(input_file, output_file)
