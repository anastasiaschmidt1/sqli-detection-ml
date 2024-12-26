import os
import pandas as pd
from sklearn.model_selection import train_test_split

# Dynamische Pfade relativ zum Skript
script_dir = os.path.dirname(os.path.abspath(__file__))  # Ordner, in dem das Skript liegt
project_root = os.path.join(script_dir, "..")  # Gehe ein Verzeichnis höher (Projekt-Root)
input_file = os.path.join(project_root, "data/processed/SQLiV3-processed.csv")
train_file = os.path.join(project_root, "data/data-train.csv")
test_file = os.path.join(project_root, "data/data-test.csv")

def split_data(input_file, train_file, test_file, test_size=0.2, random_state=42):
    """
    Teilt die Daten in Trainings- und Testdaten auf.
    Speichert die Ergebnisse in separaten CSV-Dateien.
    
    :param input_file: Pfad zur Eingabedatei
    :param train_file: Pfad zur Ausgabedatei für Trainingsdaten
    :param test_file: Pfad zur Ausgabedatei für Testdaten
    :param test_size: Anteil der Testdaten (default: 0.2)
    :param random_state: Zufallsstartwert (default: 42)
    """
    try:
        # Daten einlesen
        data = pd.read_csv(input_file)
        print(f"Datei erfolgreich geladen: {input_file}")
    except Exception as e:
        print(f"Fehler beim Einlesen der Datei: {e}")
        return

    # Daten aufteilen
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)
    
    # Daten speichern
    try:
        train_data.to_csv(train_file, index=False)
        test_data.to_csv(test_file, index=False)
        print(f"Daten erfolgreich aufgeteilt:")
        print(f"- Trainingsdaten gespeichert in: {train_file} (Anzahl: {len(train_data)})")
        print(f"- Testdaten gespeichert in: {test_file} (Anzahl: {len(test_data)})")
    except Exception as e:
        print(f"Fehler beim Speichern der Dateien: {e}")

# Skript ausführen
if __name__ == "__main__":
    split_data(input_file, train_file, test_file)
