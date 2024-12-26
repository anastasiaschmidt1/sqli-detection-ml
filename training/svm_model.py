import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
import joblib

# Dynamische Pfade
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(script_dir, "..")
train_file = os.path.join(project_root, "data/data-train.csv")
model_path = os.path.join(project_root, "models/svm_model.pkl")
vectorizer_path = os.path.join(project_root, "models/vectorizer.pkl")

def train_model(train_file, model_path, vectorizer_path):
    """
    Trainiert ein SVM-Modell und speichert es zusammen mit dem Vektorisierer.
    :param train_file: Pfad zu den Trainingsdaten
    :param model_path: Pfad zum Speichern des Modells
    :param vectorizer_path: Pfad zum Speichern des Vektorisierers
    """
    try:
        # Trainingsdaten laden
        data = pd.read_csv(train_file)
        print(f"Trainingsdaten erfolgreich geladen: {train_file}")
    except Exception as e:
        print(f"Fehler beim Einlesen der Datei: {e}")
        return

    # Features und Labels extrahieren
    queries = data['Sentence']
    labels = data['Label']

    # Vektorisieren der Eingaben
    vectorizer = CountVectorizer(ngram_range=(1, 2), analyzer='char')
    X = vectorizer.fit_transform(queries)

    # Modell erstellen und trainieren
    model = SVC(kernel='linear', C=1.0, random_state=42)
    model.fit(X, labels)

    # Modell und Vektorisierer speichern
    try:
        joblib.dump(model, model_path)
        joblib.dump(vectorizer, vectorizer_path)
        print(f"Modell erfolgreich gespeichert: {model_path}")
        print(f"Vektorisierer erfolgreich gespeichert: {vectorizer_path}")
    except Exception as e:
        print(f"Fehler beim Speichern: {e}")
