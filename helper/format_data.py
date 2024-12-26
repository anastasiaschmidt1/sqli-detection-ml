import os
import pandas as pd

# Dynamische Pfade relativ zum Skript
script_dir = os.path.dirname(os.path.abspath(__file__))  # Ordner, in dem das Skript liegt
project_root = os.path.join(script_dir, "..")  # Gehe ein Verzeichnis höher (Projekt-Root)
input_file = os.path.join(project_root, "data/raw/SQLiV3.csv")
output_file = os.path.join(project_root, "data/processed/SQLiV3-processed.csv")

def format_data(input_file, output_file):
    """
    Liest eine CSV-Datei ein, bereinigt die Daten und speichert das Ergebnis.
    - Beibehaltung der Spalten 'Sentence' und 'Label'
    - Entfernen von Zeilen mit fehlenden Werten (NaN)
    - Konvertierung von Labels in Ganzzahlen
    - Zeigt Statistiken vor und nach der Bereinigung
    """
    try:
        # Daten einlesen
        data = pd.read_csv(input_file)
        print(f"Datei erfolgreich geladen: {input_file}")
    except Exception as e:
        print(f"Fehler beim Einlesen der Datei: {e}")
        return

    # Überprüfen, ob die notwendigen Spalten existieren
    if 'Sentence' not in data.columns or 'Label' not in data.columns:
        print("Die Spalten 'Sentence' und 'Label' fehlen in der Eingabedatei.")
        return

    # Konvertierung der Label-Spalte in Ganzzahlen
    data['Label'] = pd.to_numeric(data['Label'], errors='coerce').astype('Int64')

    # Statistiken vor der Bereinigung
    print(f"Anzahl der Zeilen vor der Bereinigung: {len(data)}")

    # Spalten 'Sentence' und 'Label' extrahieren und leere Zeilen entfernen
    formatted_data = data[['Sentence', 'Label']].dropna()

    # Nach der Bereinigung sicherstellen, dass Labels int sind
    formatted_data['Label'] = formatted_data['Label'].astype(int)

    # Statistiken nach der Bereinigung
    print(f"Anzahl der Zeilen nach der Bereinigung: {len(formatted_data)}")
    print(f"Anzahl der '1'-Labels nach der Bereinigung: {sum(formatted_data['Label'] == 1)}")
    print(f"Anzahl der '0'-Labels nach der Bereinigung: {sum(formatted_data['Label'] == 0)}")

    # Ergebnis speichern
    try:
        formatted_data.to_csv(output_file, index=False)
        print(f"Bereinigte Datei erfolgreich gespeichert unter: {output_file}")
    except Exception as e:
        print(f"Fehler beim Speichern der Datei: {e}")

# Skript ausführen
if __name__ == "__main__":
    format_data(input_file, output_file)
