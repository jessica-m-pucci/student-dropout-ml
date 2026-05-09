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
        "Nacionality": "nacionality",
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
    df = df.rename(columns={"nacionality": "nationality"})
    return df