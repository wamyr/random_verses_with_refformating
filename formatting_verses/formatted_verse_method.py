
import re
import os 

def clean_unicode(file_path):

    temp_file_path = file_path + ".temp"
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Supprimer les caractères Bidi invisibles (U+202D, U+202C)
    content_cleaned = (
        content
        .replace('\u202D', '')  # Supprimer U+202D (LEFT-TO-RIGHT OVERRIDE)
        .replace('\u202C', '')  # Supprimer U+202C (POP DIRECTIONAL FORMATTING)
        .replace('\u00A0', ' ')  # Remplacer les espaces insécables par des espaces normaux
        .replace('\u202f', ' ')  # Remplacer les espaces fines insécables
        .replace('“', '"')       # Remplacer les guillemets typographiques par des guillemets droits
        .replace('”', '"')
        .replace('‘', "'")       # Remplacer les apostrophes typographiques par des apostrophes simples
        .replace('’', "'")
        .replace('–', '-')       # Remplacer les tirets longs par des tirets normaux
        .replace('—', '-')       # Remplacer les tirets cadratins par des tirets normaux
    )

    # Écrire le contenu nettoyé dans le fichier de sortie
    with open(temp_file_path, 'w', encoding='utf-8') as temp_file:
        temp_file.write(content_cleaned)

    # Remplacer l'ancien fichier par le fichier temporaire
    os.replace(temp_file_path, file_path)


def reformat_verses(verse_lines):
    formatted_verses = []
    duplicate_check = set()
    duplicates = []
    
    # Nettoyer les lignes et s'assurer qu'elles suivent le bon format
    cleaned_lines = [line.strip() for line in verse_lines if line.strip() != '']
    #print(len(cleaned_lines))
    # Traiter les versets en blocs de 2 lignes (verset, référence)
    for i in range(0, len(cleaned_lines), 2):  
		#print("Index i: %d" % i)
        verse_text = cleaned_lines[i]  # Première ligne : texte du verset
        reference = cleaned_lines[i + 1]  # Deuxième ligne : référence
        #print("Index i: %d" % i)
        # 1. Supprimer tout avant la première lettre ou un guillemet «
        verse_text = re.sub(r'^[^\w»[]*', '', verse_text)
        
        # 2. Remplacer les guillemets au début par « et à la fin par ”
        if verse_text.startswith('»'):
            verse_text = re.sub(r'^[^\w[]*', '', verse_text)
            verse_text = '«' + verse_text.strip()  
        #supprimer le dernier élément 
        verse_text = verse_text[:-1]
        #print(verse_text)
        # Détection et formatage de la référence et de la version
        #print(reference)
        reference = re.sub(r'^[^a-zA-Z0-9]*', '', reference)
        match = re.search(r'^(.*?)\s(\[?(S21|BDS|LSG)\]?)$', reference)
        if not match :
        	print("error reference")
        if match:
            book_reference = match.group(1).strip()
            version = match.group(2).strip()
            
            # Vérifier si la version est déjà entre crochets
            if not version.startswith('[') and not version.endswith(']'):
                # Si ce n'est pas entre crochets, ajouter les crochets autour de la version
                version = f"[{version}]"
            # Si la version est déjà entre crochets, elle restera telle quelle
            # Formater correctement le verset et la référence
            formatted = f"   • “{verse_text}”\n      — {book_reference} {version}\n\n"
            
            # Vérifier les doublons
            unique_key = (book_reference.lower(), version.lower())
            if unique_key in duplicate_check:
                duplicates.append(formatted)
            else:
                duplicate_check.add(unique_key)
                formatted_verses.append(formatted)
	
    return formatted_verses, duplicates


if __name__ == "__main__":
    input_file = "../versets.txt"  # Votre fichier d'entrée
    #input_file = "/home/sammygros/versets/formatting_verses/versets_clean.txt"
    formatted_file = "formatted_verses/verses_formatted.txt"  # Fichier de sortie
    duplicates_file = "formatted_verses/duplicates_summary.txt"  # Fichier des doublons
    
    clean_unicode(input_file)
	
    with open(input_file, "r", encoding="utf-8") as file:
        verses_content = file.readlines()

    # Afficher les lignes pour vérifier le contenu du fichier
    #for line in verses_content:
        #print(line.strip())

    formatted_verses, duplicates = reformat_verses(verses_content)

    # Sauvegarde des versets formatés
    with open(formatted_file, "w", encoding="utf-8") as formatted_file :
        formatted_file.writelines(formatted_verses)

    # Sauvegarde des doublons
    with open(duplicates_file, "w", encoding="utf-8") as duplicates_file:
        duplicates_file.writelines(duplicates)

    print(f"Formatted verses saved in {formatted_file}")
    print(f"Duplicates saved in {duplicates_file}")

