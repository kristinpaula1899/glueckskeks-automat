# --------------------------------------------------------------
# Dateiname: app.py
# Autorin: Kristin Göbel
# Datum: 2025-06-05
# Beschreibung: Glückskeksautomat als Web-App mit Streamlit
# - Benutzer gibt Stimmung ein (frei)
# - Spruch wird zufällig aus JSON-Datei gewählt
# - Ausgabe als Glückskeks-Spruch über Weboberfläche
# --------------------------------------------------------------

import streamlit as st
import json
import random

# Titel und Beschreibung anzeigen
st.title("🥠 Glückskeks-Automat")
st.markdown("Schreib deine Stimmung in das Feld unten – egal ob hungrig, wütend oder einfach meh ...")

# Eingabe durch Benutzer
stimmung = st.text_input("🧠 Wie fühlst du dich gerade?")

# Sprüche aus JSON-Datei laden
def lade_sprueche():
    with open("glueckskeks_sprueche.json", "r", encoding="utf-8") as f:
        daten = json.load(f)
        return daten["sprueche"]

sprueche = lade_sprueche()

# Button anzeigen – immer sichtbar
if st.button("🎯 Keks ziehen!"):
    st.write(f"🧠 Deine Stimmung: *{stimmung}*")
    spruch = random.choice(sprueche)
    st.success(f"🥠 Dein Glückskeks sagt:\n\n**{spruch}**")


