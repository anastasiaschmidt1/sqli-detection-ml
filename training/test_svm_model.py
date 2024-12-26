import os
import pandas as pd
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Dynamische Pfade
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(script_dir, "..")
test_file = os.path.join(project_root, "data/data-test.csv")
model_path = os.path.join(project_root, "models/svm_model.pkl")
vectorizer_path = os.path.join(project_root, "models/vectorizer.pkl")

def test_model(test_file, model_path, vectorizer_path):
    """
    Testet das gespeicherte Modell mit den Testdaten.
    :param test_file: Pfad zu den Testdaten
    :param model_path: Pfad zum gespeicherten Modell
    :param vectorizer_path: Pfad zum gespeicherten Vektorisierer
    """
    try:
        # Testdaten laden
        data = pd.read_csv(test_file)
        print(f"Testdaten erfolgreich geladen: {test_file}")
    except Exception as e:
        print(f"Fehler beim Einlesen der Datei: {e}")
        return

    # Features und Labels extrahieren
    queries = data['Sentence']
    true_labels = data['Label']

    # Modell und Vektorisierer laden
    try:
        model = joblib.load(model_path)
        vectorizer = joblib.load(vectorizer_path)
        print(f"Modell und Vektorisierer erfolgreich geladen.")
    except Exception as e:
        print(f"Fehler beim Laden des Modells oder Vektorisierers: {e}")
        return

    # Eingaben vektorisieren und Vorhersagen machen
    X = vectorizer.transform(queries)
    predictions = model.predict(X)

    # Ergebnisse evaluieren
    print("\nClassification Report:")
    print(classification_report(true_labels, predictions))
    print(f"Accuracy: {accuracy_score(true_labels, predictions):.4f}")

# Skript ausführen
if __name__ == "__main__":
    test_model(test_file, model_path, vectorizer_path)
