# --------------------------------------------------------------
# Dateiname: glueckskeks_automat.py
# Autor: Kristin Göbel
# Datum: 2025-06-05
# Beschreibung: Glückskeksautomat mit Spruchausgabe per JSON-Datei.
# - Lese Sprüche aus externer JSON-Datei
# - Benutzer gibt Stimmung ein (z. B. "verliebt", "hungrig", ...)
# - Bei jeder Eingabe wird zufällig ein Spruch angezeigt
# - Das Programm endet durch Eingabe von "ENDE"
# --------------------------------------------------------------

import json
import random

# ------------------------------------------
# Pfad zur JSON-Datei mit den Glückskeks-Sprüchen
# ------------------------------------------
json_datei = r"C:\Users\krist\OneDrive\...VELPTEC\Übungsaufgaben\Glückskeksautomat\glueckskeks_sprueche.json"

# ------------------------------------------
# JSON-Datei laden und die Sprüche lesen
# ------------------------------------------
try:
    with open(json_datei, "r", encoding="utf-8") as f:
        daten = json.load(f)
        sprueche = daten["sprueche"]
except FileNotFoundError:
    print("❌ Die JSON-Datei mit den Glückskekssprüchen wurde nicht gefunden.")
    exit()

# ------------------------------------------
# Begrüßung und kurze Anleitung
# ------------------------------------------
print("🥠 Willkommen im Glückskeks-Automaten!")
print("Gib deine Stimmung ein (z.B. verliebt, verärgert, hungrig, verlassen, glücklich) ...")
print("Oder tippe 'ENDE', um das Programm zu beenden.\n")

# ------------------------------------------
# Haupt-Programmschleife
# ------------------------------------------
while True:
    stimmung = input("🧠 Deine Stimmung: ").strip().lower()

    if stimmung == "ende":
        print("👋 Auf Wiedersehen – und vergiss nicht: Glück steckt oft im Kleinen!")
        break

    # Die Stimmung beeinflusst nichts – wir ziehen immer zufällig
    spruch = random.choice(sprueche)

    print("\n🥠 Dein Glückskeks sagt:")
    print("👉", spruch)
    print("-" * 50)

