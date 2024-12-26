# SQL Injection Detection

--------

## 🚨 **Wichtige Anmerkung** 🚨

**Dieses Projekt wurde im Rahmen des Moduls "Wissenschaftliches Projekt" an der Berliner Hochschule für Technik (BHT) im Wintersemester 2024/2025 erstellt.**

Es werden Vorlagen aus dem Modul **"Künstliche Intelligenz"** verwendet und zudem wurde das Projekt mit Hilfe von **ChatGPT**😱 entwickelt und ist komplett in **Deutsch**😱😱.

**⚠️ Es wird darauf hingewiesen, dass dieses Projekt keine Garantie auf die Qualität oder die fehlerfreie Funktion des Codes gibt. Jegliche Nutzung des Projekts erfolgt auf **eigene Verantwortung****

--------

## Projektübersicht
Dieses Projekt zur Erkennung von SQL-Injection-Angriffen nutzt maschinelles Lernen (SVM-Modell), um SQL-Injection-Angriffe anhand von Benutzereingaben zu identifizieren.

Die **Daten** stammen von [Kaggle: SQL Injection Dataset](https://www.kaggle.com/datasets/syedsaqlainhussain/sql-injection-dataset), das SQL-Injection-Strings sowie normale Benutzereingaben enthält. Nach der Bereinigung werden die Daten in **Trainingsdaten** und **Testdaten** aufgeteilt, um das Modell zu trainieren und zu evaluieren.

--------

## Projektstruktur
Das Projekt ist wie folgt strukturiert:

```
sqli-detection-ml/
│
├── data/                         
│   ├── raw/                       # Rohdaten
│   │   └── SQLiV3.csv             
│   ├── processed/                 # Bereinigte Daten (generierte Datei)
│   │   └── SQLiV3-processed.csv  
│   ├── data-train.csv             # Trainingsdaten (generierte Datei)
│   └── data-test.csv              # Testdaten (generierte Datei)
│   └── README-data.md             
│
├── helper/                       
│   ├── format_data.py             # Skript zur Bereinigung der Daten
│   └── split_data.py              # Skript zur Aufteilung der Daten
│
├── models/                        
│   ├── svm_model.pkl              # Trainiertes SVM-Modell (generierte Datei)
│   └── vectorizer.pkl             # Vektorisierer (generierte Datei)
│
├── training/                      
│   ├── svm_model.py               # Logik für Modelltraining und Vorhersagen
│   ├── test_svm_model.py          # Tests für das Modell
│
├── .gitignore   
├── main.py                        # Hauptskript für Training und Vorhersagen
├── README.md                      
└── requirements.txt               # Abhängigkeiten
```
--------

## Installation und Nutzung

### Getestete Umgebung
Das Projekt wurde in **Anaconda** mit **Python 3.12.7** getestet. _(Anaconda ist eine Python-Distribution, die speziell für Data-Science- und maschinelles Lernen optimiert wurde. Sie bietet eine einfache Verwaltung von Python-Versionen und Abhängigkeiten.)_

Die folgenden Versionen der Bibliotheken wurden verwendet:

* **pandas: 2.2.2**
* **scikit-learn: 1.5.1**
* **joblib: 1.4.2**
* **numpy: 1.26.4**

### Abhängigkeiten
Das Projekt benötigt folgende Python-Pakete, die für das Datenmanagement, Modelltraining und Vorhersagen zuständig sind:

**pandas:** Wird zur Verarbeitung und Manipulation von Daten verwendet. Es stellt leistungsfähige Datenstrukturen wie DataFrames zur Verfügung, die für das Projekt zur Speicherung und Analyse der SQL-Abfragen genutzt werden.

**scikit-learn:** Wird für das maschinelle Lernen verwendet. Diese Bibliothek enthält zahlreiche Algorithmen, einschließlich SVM (Support Vector Machine), die im Projekt zur Erkennung von SQL-Injection-Angriffen eingesetzt wird.

**joblib:** Wird zur Serialisierung des Modells und des Vektorisierers verwendet. Dies ermöglicht es, das trainierte Modell und den Vektorisierer zu speichern und später wieder zu laden.

**numpy:** Wird für numerische Berechnungen verwendet und ist eine grundlegende Bibliothek für die Arbeit mit Arrays und Matrizen, die in vielen Algorithmen von scikit-learn erforderlich sind.


Installiere alle Abhängigkeiten mit:
```bash
pip install -r requirements.txt
```

### Nutzung

1. **Daten bereinigen**:
```bash
python helper/format_data.py
```
2. **Daten aufteilen**:
 ```bash
python helper/split_data.py
```
3. **Modell trainieren**:
```bash
python main.py train
```
4. **Modell testen**:
```bash
python main.py test
```
5. **Vorhersage durchführen**:
```
python main.py predict --query "DEINE_BEISPIEL_EINGABE"
```
Beispiel: Wenn du eine SQL-Abfrage vorhersagen möchtest, kannst du das Modell wie folgt verwenden:
```bash
python main.py predict --query "SELECT * FROM users WHERE id='1' OR 1=1 --"
```
Dies gibt zurück, ob es sich um eine SQL-Injection handelt (`SQLi`) oder nicht (`Normal`).

--------

## Modellbeschreibung

Das Modell verwendet einen **Support Vector Machine (SVM)**-Algorithmus, um zwischen **SQL-Injection-Angriffen** und **normalen Benutzereingaben** zu unterscheiden. Der SVM-Algorithmus wurde mit einem Datensatz von SQL-Injection-Strings und normalen SQL-Abfragen trainiert.

Ein wesentlicher Bestandteil des Modells ist die **Vektorisierung der SQL-Abfragen**. Es wird `CountVectorizer` aus der Bibliothek **`scikit-learn`** verwendet, um die Textdaten in **numerische Vektoren** zu transformieren. Dabei wird **n-Gramme**, also Kombinationen von aufeinanderfolgenden Zeichen berücksichtigt. Dies hilft dem Modell, **Zeichenfolgenmuster** zu erkennen, die typisch für SQL-Injections sind.

Der **Vektorisierer** (gespeichert als `vectorizer.pkl`) extrahiert sowohl **einzelne Zeichen (1-Gramme)** als auch **zwei aufeinanderfolgende Zeichen (2-Gramme)** aus den SQL-Abfragen. Dies ermöglicht es dem Modell, komplexe Muster zu erkennen, die in SQL-Injection-Angriffen häufig auftreten, wie z.B. die Kombination `--` oder `1=1`.

Das trainierte Modell wird als **`svm_model.pkl`** gespeichert und kann für Vorhersagen auf neuen SQL-Abfragen verwendet werden.
