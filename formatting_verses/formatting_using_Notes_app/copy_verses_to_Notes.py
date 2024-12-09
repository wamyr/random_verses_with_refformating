import subprocess

def copy_to_notes(file_path, note_index=1, folder_name="Versets"):
    """
    Copie le contenu d'un fichier texte dans une note spécifique de l'application Notes.
    
    Args:
        file_path (str): Chemin du fichier texte à copier.
        note_index (int): Index de la note cible dans le dossier.
        folder_name (str): Nom du dossier contenant la note.
    """
    # Lire le contenu du fichier
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} n'existe pas.")
        return
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return

    # Ajouter "Versets \n \n" au début du contenu
    content = "Versets\n\n" + content
    with open("/Users/sammygros/Documents/random_verses_with_refformating/versets_clean.txt", "w", encoding="utf-8") as file: file.write(content)

    # Remplacer les retours à la ligne (\n) par \\\n et les tabulations (\t) par \\\t
    """content = content.replace("\n", "\\\\n").replace("\t", "\\\\t")

    # Échapper les guillemets pour l'utiliser dans AppleScript
    escaped_content = content.replace('"', '\\"')

    # Script AppleScript pour définir le contenu d'une note
    applescript = f'''
    tell application "Notes"
        set body of note {note_index} of folder "{folder_name}" to "{escaped_content}"
    end tell
    '''

    # Exécuter le script via osascript
    result = subprocess.run(['osascript', '-e', applescript], capture_output=True, text=True)

    # Vérification du résultat
    if result.returncode == 0:
        print("Note mise à jour avec succès.")
    else:
        print(f"Erreur lors de la mise à jour de la note : {result.stderr}") """

def main():
    # Définir les paramètres
    file_path = "../formatted_verses/verses_formatted.txt"  # Chemin du fichier texte
    note_index = 1  # Index de la note cible
    folder_name = "Versets"  # Nom du dossier cible dans Notes

    # Appeler la fonction pour copier le contenu dans Notes
    copy_to_notes(file_path, note_index, folder_name)

if __name__ == "__main__":
    main()
