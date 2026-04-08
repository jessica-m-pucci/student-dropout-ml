# 🎓 Student Dropout ML

Progetto di Machine Learning per predire il dropout universitario, sviluppato nell'ambito del corso **Develhope Data/AI Analyst**.

## 📋 Descrizione

Il progetto utilizza dati reali di 4.424 studenti universitari per costruire un modello predittivo in grado di identificare gli studenti a rischio di abbandono degli studi. Il problema è trattato come classificazione binaria: `Dropout` vs `Graduate`.

Il dataset è disponibile sull'[UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success).

## 👥 Il Team

- Youssra Zarouky
- Chiara Gulli
- Vincenzo Nuccio
- Jessica M Pucci

## 🛠️ Installazione

### Prerequisiti
- Python 3.13 o superiore
- Git

### Setup dell'ambiente

1. Clona la repository:
```bash
   git clone https://github.com/jessica-m-pucci/student-dropout-ml.git
   cd student-dropout-ml
```

2. Crea il virtual environment:
```bash
   python -m venv .venv
```

3. Attiva il virtual environment:

   **Windows:**
```bash
   .venv\Scripts\Activate.ps1
```

   **Mac/Linux:**
```bash
   source .venv/bin/activate
```

4. Installa le dipendenze:
```bash
   pip install -r requirements.txt
```

## 🚀 Avvio dei Notebook

Apri la cartella del progetto in VS Code e seleziona il kernel `.venv` per eseguire i notebook nella cartella `notebooks/`:

| Notebook | Contenuto |
|---|---|
| `01_preliminary_analysis.ipynb` | Caricamento, pulizia e analisi preliminare |
| `02_exploratory_analysis.ipynb` | Analisi esplorativa e visualizzazioni |
| `03_outlier_analysis.ipynb` | Rilevazione e gestione degli outlier |
| `04_machine_learning.ipynb` | Modelli ML e valutazione |

## 📁 Struttura della Repository

```
student-dropout-ml/
│
├── data/
│   ├── raw/                        # Dataset originale — NON modificare mai questi file
│   │   └── data.csv
│   └── processed/                  # Dataset dopo pulizia e preprocessing
│       └── data_clean.csv
│
├── notebooks/
│   ├── 01_preliminary_analysis.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_outlier_analysis.ipynb
│   └── 04_machine_learning.ipynb
│
├── src/                            # Funzioni Python riutilizzabili
│   ├── __init__.py                 # File vuoto, serve a Python per riconoscere la cartella
│   ├── preprocessing.py            # Funzioni di pulizia e encoding
│   ├── visualization.py            # Funzioni per generare grafici
│   └── evaluation.py               # Funzioni per valutare i modelli
│
├── outputs/
│   └── figures/                    # Tutti i grafici salvati in PNG
│
├── presentation/                   # Slide finali
│
├── requirements.txt                # Lista delle librerie Python usate
└── README.md                       # Descrizione del progetto e istruzioni
```