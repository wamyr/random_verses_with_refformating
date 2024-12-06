import random

def get_random_verse(file_path):
    # Ouvrir le fichier de versets
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

# Nettoyer les lignes pour ignorer les lignes vides
    cleaned_lines = [line.strip() for line in lines if line.strip()]

    # Créer une liste de versets complets (texte + référence)
    verses = []
    for i in range(0, len(cleaned_lines) - 1, 2):  # Lire deux lignes à la fois (texte + référence)
        verse_text = cleaned_lines[i]  # Ligne 1 : Texte du verset
        reference = cleaned_lines[i + 1]  # Ligne 2 : Référence
        verses.append(f"{verse_text}\n{reference}")

    # Choisir un verset aléatoire
    random_verse = random.choice(verses)
    return random_verse.strip()

if __name__ == "__main__":
    # Chemin du fichier de versets
    file_path = "/home/sammygros/versets/versets_v1.txt"  # Modifiez ceci avec le chemin réel de votre fichier versets.txt
    print(get_random_verse(file_path))
