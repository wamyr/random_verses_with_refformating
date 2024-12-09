#!/bin/zsh
# Exécute le script Python et affiche un verset aléatoire
cd /Users/sammygros/Documents/random_verses_with_refformating/formatting_verses/formatting_using_Notes_app
osascript -e 'tell application "Notes" to get body of note 1 of folder "Versets"' > Notes_verses.txt
python3 formatted_Notes_verses.py #installer : pip install beautifulsoup4
cd ..
python3 formatted_verse_method.py  #PATH
cd formatting_using_Notes_app
python3 copy_verses_to_Notes.py
cd