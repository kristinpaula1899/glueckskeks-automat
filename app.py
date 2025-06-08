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
import os

st.title("🥠 Glückskeks-Automat")
st.markdown("Schreib deine Stimmung in das Feld unten – egal ob hungrig, wütend oder einfach meh ...")

stimmung = st.text_input("🧠 Wie fühlst du dich gerade?")

def lade_sprueche():
    try:
        with open("glueckskeks_sprueche.json", "r", encoding="utf-8") as f:
            daten = json.load(f)
            return daten.get("sprueche", [])
    except FileNotFoundError:
        st.error("Die Sprüche-Datei fehlt. Bitte glueckskeks_sprueche.json ins Verzeichnis legen!")
        return []
    except Exception as e:
        st.error(f"Fehler beim Laden der Sprüche: {e}")
        return []

sprueche = lade_sprueche()

if st.button("🎯 Keks ziehen!"):
    if not sprueche:
        st.error("Keine Sprüche gefunden!")
    else:
        st.write(f"🧠 Deine Stimmung: *{stimmung}*")
        spruch = random.choice(sprueche)
        st.success(f"🥠 Dein Glückskeks sagt:\n\n**{spruch}**")


