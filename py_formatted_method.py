import re

def reformat_verses_with_spacing(verse_lines):
    formatted_verses = []
    duplicate_check = set()
    duplicates = []
    
    # Nettoyer les lignes et s'assurer qu'elles suivent le bon format
    cleaned_lines = [line.strip() for line in verse_lines if line.strip() != '']

    for i in range(len(cleaned_lines)):
        line = cleaned_lines[i]
        if re.match(r'^["«]', line):
            verse_text = line.strip('«»“”"').replace('’', "'")
            next_line = cleaned_lines[i + 1].strip() if i + 1 < len(cleaned_lines) else ""
            
            match = re.search(r'(—|^)?\s*([\w\s:()\-\u202f]+)\s(\[.*\]|S21|LSG|BDS)', next_line)
            if match:
                book_reference = match.group(2).strip()
                version = match.group(3).strip().replace('S21', '[S21]').replace('LSG', '[LSG]').replace('BDS', '[BDS]')
                formatted = f"   • “{verse_text}”\n      — {book_reference} {version}\n\n"

                unique_key = (verse_text.lower(), book_reference.lower(), version.lower())
                if unique_key in duplicate_check:
                    duplicates.append(formatted)
                else:
                    duplicate_check.add(unique_key)
                    formatted_verses.append(formatted)

    return formatted_verses, duplicates


if __name__ == "__main__":
    input_file = "versets.txt"  # Votre fichier d'entrée
    formatted_file = "formatted_versets_with_spacing.txt"  # Fichier de sortie
    duplicates_file = "duplicates_summary.txt"  # Fichier des doublons

    with open(input_file, "r", encoding="utf-8") as file:
        verses_content = file.readlines()

    # Afficher les lignes pour vérifier le contenu du fichier
    for line in verses_content:
        print(line.strip())

    formatted_verses, duplicates = reformat_verses_with_spacing(verses_content)

    # Sauvegarde des versets formatés
    with open(formatted_file, "w", encoding="utf-8") as formatted_file_with_spacing:
        formatted_file_with_spacing.writelines(formatted_verses)

    # Sauvegarde des doublons
    with open(duplicates_file, "w", encoding="utf-8") as duplicates_file_with_spacing:
        duplicates_file_with_spacing.writelines(duplicates)

    print(f"Formatted verses saved in {formatted_file}")
    print(f"Duplicates saved in {duplicates_file}")

