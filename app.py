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

import streamlit as st
import json
import random

# Titel und Beschreibung anzeigen
st.title("🥠 Glückskeks-Automat")
st.markdown("Schreib deine Stimmung in das Feld unten – egal ob hungrig, wütend oder einfach meh ...")

# Eingabe durch Benutzer
stimmung = st.text_input("🧠 Wie fühlst du dich gerade?")

# Sprüche aus JSON laden
def lade_sprueche():
    with open("glueckskeks_sprueche.json", "r", encoding="utf-8") as f:
        daten = json.load(f)
        return daten["sprueche"]

sprueche = lade_sprueche()

# Button anzeigen und Spruch ausgeben
if stimmung:
    if st.button("🎯 Keks ziehen!"):
        spruch = random.choice(sprueche)
        st.success(f"🥠 Dein Glückskeks sagt:\n\n**{spruch}**")
    print("👉", spruch)
    print("-" * 50)

