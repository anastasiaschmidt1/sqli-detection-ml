import argparse
from training.svm_model import train_model
from training.test_svm_model import test_model
import os
import joblib

# Dynamische Pfade
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(script_dir, ".")
train_file = os.path.join(project_root, "data/data-train.csv")
test_file = os.path.join(project_root, "data/data-test.csv")
model_path = os.path.join(project_root, "models/svm_model.pkl")
vectorizer_path = os.path.join(project_root, "models/vectorizer.pkl")

def predict(query):
    """
    Vorhersage eines Labels für eine gegebene SQL-Abfrage.
    :param query: SQL-Abfrage (String)
    """
    try:
        # Modell und Vektorisierer laden
        model = joblib.load(model_path)
        vectorizer = joblib.load(vectorizer_path)
        print("Modell und Vektorisierer erfolgreich geladen.")

        # Eingabe transformieren und Vorhersage durchführen
        query_vector = vectorizer.transform([query])
        prediction = model.predict(query_vector)[0]
        print(f"Eingabe: {query}")
        print(f"Vorhersage: {'SQLi' if prediction == 1 else 'Normal'}")

    except Exception as e:
        print(f"Fehler bei der Vorhersage: {e}")

def main():
    # Argumente definieren
    parser = argparse.ArgumentParser(description="SQL Injection Detection")
    parser.add_argument("action", choices=["train", "test", "predict"], help="Aktion: train, test oder predict")
    parser.add_argument("--query", type=str, help="SQL-Query für die Vorhersage (nur für predict)")
    args = parser.parse_args()

    if args.action == "train":
        print("Training gestartet...")
        train_model(train_file, model_path, vectorizer_path)

    elif args.action == "test":
        print("Testen gestartet...")
        test_model(test_file, model_path, vectorizer_path)

    elif args.action == "predict":
        if args.query:
            print("Vorhersage gestartet...")
            predict(args.query)
        else:
            print("Bitte eine Eingabe mit --query angeben.")

if __name__ == "__main__":
    main()
