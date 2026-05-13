import pandas as pd
from sklearn.metrics import accuracy_score, f1_score


def build_comparison_table(y_test, predictions: dict) -> pd.DataFrame:
    """
    Costruisce una tabella di confronto tra modelli di classificazione binaria.

    Parametri:
    - y_test: array-like con le etichette reali (0=Graduate, 1=Dropout)
    - predictions: dict {nome_modello: array predizioni}

    Ritorna: DataFrame con Accuracy, F1 Graduate, F1 Dropout, F1 Macro per ogni modello
    """
    rows = []
    for name, y_pred in predictions.items():
        rows.append({
            'Modello':     name,
            'Accuracy':    round(accuracy_score(y_test, y_pred), 3),
            'F1 Graduate': round(f1_score(y_test, y_pred, pos_label=0), 3),
            'F1 Dropout':  round(f1_score(y_test, y_pred, pos_label=1), 3),
            'F1 Macro':    round(f1_score(y_test, y_pred, average='macro'), 3),
        })
    return pd.DataFrame(rows)
