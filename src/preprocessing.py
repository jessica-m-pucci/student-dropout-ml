import pandas as pd

def rename_columns(df):
    """
    Rinomina tutte le colonne del dataset in snake_case.
    Rimuove spazi, apostrofi e caratteri speciali.
    
    Parametri:
    - df: DataFrame pandas
    
    Ritorna: DataFrame con colonne rinominate
    """
    rename_dict = {
        "Marital status": "marital_status",
        "Application mode": "application_mode",
        "Application order": "application_order",
        "Course": "course",
        "Previous qualification": "previous_qualification",
        "Previous qualification (grade)": "previous_qualification_grade",
        "Nacionality": "nationality",
        "Mother's qualification": "mothers_qualification",
        "Father's qualification": "fathers_qualification",
        "Mother's occupation": "mothers_occupation",
        "Father's occupation": "fathers_occupation",
        "Admission grade": "admission_grade",
        "Displaced": "displaced",
        "Educational special needs": "educational_special_needs",
        "Debtor": "debtor",
        "Tuition fees up to date": "tuition_fees_up_to_date",
        "Gender": "gender",
        "Scholarship holder": "scholarship_holder",
        "Age at enrollment": "age_at_enrollment",
        "International": "international",
        "Curricular units 1st sem (credited)": "cu_1st_sem_credited",
        "Curricular units 1st sem (enrolled)": "cu_1st_sem_enrolled",
        "Curricular units 1st sem (evaluations)": "cu_1st_sem_evaluations",
        "Curricular units 1st sem (approved)": "cu_1st_sem_approved",
        "Curricular units 1st sem (grade)": "cu_1st_sem_grade",
        "Curricular units 1st sem (without evaluations)": "cu_1st_sem_without_evaluations",
        "Curricular units 2nd sem (credited)": "cu_2nd_sem_credited",
        "Curricular units 2nd sem (enrolled)": "cu_2nd_sem_enrolled",
        "Curricular units 2nd sem (evaluations)": "cu_2nd_sem_evaluations",
        "Curricular units 2nd sem (approved)": "cu_2nd_sem_approved",
        "Curricular units 2nd sem (grade)": "cu_2nd_sem_grade",
        "Curricular units 2nd sem (without evaluations)": "cu_2nd_sem_without_evaluations",
        "Unemployment rate": "unemployment_rate",
        "Inflation rate": "inflation_rate",
        "GDP": "gdp",
        "Target": "target"
    }
    
    df = df.rename(columns=rename_dict)
    df.columns = [col.replace("Daytime/evening attendance\t", "daytime_evening_attendance") 
                  if "Daytime" in col else col for col in df.columns]
    return df


def analyze_missing_values(df):
    """
    Analizza i valori mancanti nel DataFrame.
    Mostra una tabella con numero e percentuale di missing per colonna.
    
    Parametri:
    - df: DataFrame pandas
    
    Ritorna: DataFrame con il riepilogo dei missing values
    """
    missing = df.isnull().sum()
    pct = (missing / len(df)) * 100
    
    summary = pd.DataFrame({
        'missing': missing,
        'percentuale': pct.round(2)
    }).sort_values('missing', ascending=False)
    
    print(f"Colonne con valori mancanti: {(missing > 0).sum()} su {len(df.columns)}")
    print()
    print(summary)
    return summary


def detect_outliers_std(df, columns, threshold=3):
    """
    Identifica gli outlier usando il metodo della deviazione standard.
    Un valore e outlier se |x - mean| > threshold * std.

    Parametri:
    - df: DataFrame pandas
    - columns: lista di colonne numeriche da analizzare
    - threshold: numero di deviazioni standard (default: 3)

    Ritorna: DataFrame con numero e percentuale di outlier per colonna
    """
    results = []
    for col in columns:
        mean = df[col].mean()
        std = df[col].std()
        n_outliers = ((df[col] - mean).abs() > threshold * std).sum()
        pct = round((n_outliers / len(df)) * 100, 2)
        results.append({
            'colonna': col,
            'n_outlier': n_outliers,
            'percentuale': pct,
            'mean': round(mean, 2),
            'std': round(std, 2)
        })

    summary = pd.DataFrame(results).sort_values('n_outlier', ascending=False)
    return summary
