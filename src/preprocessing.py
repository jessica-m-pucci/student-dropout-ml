def rename_columns_to_snake_case(df):
    """
    Rinomina le colonne del DataFrame in formato snake_case.
    """

    column_mapping = {
        "Marital status": "marital_status",
        "Application mode": "application_mode",
        "Application order": "application_order",
        "Course": "course",
        "Daytime/evening attendance": "daytime_evening_attendance",
        "Previous qualification": "previous_qualification",
        "Previous qualification (grade)": "previous_qualification_grade",
        "Nacionality": "nationality",
        "Mother's qualification": "mother_qualification",
        "Father's qualification": "father_qualification",
        "Mother's occupation": "mother_occupation",
        "Father's occupation": "father_occupation",
        "Admission grade": "admission_grade",
        "Displaced": "displaced",
        "Educational special needs": "educational_special_needs",
        "Debtor": "debtor",
        "Tuition fees up to date": "tuition_fees_up_to_date",
        "Gender": "gender",
        "Scholarship holder": "scholarship_holder",
        "Age at enrollment": "age_at_enrollment",
        "International": "international",
        "Curricular units 1st sem (credited)": "curricular_units_1st_sem_credited",
        "Curricular units 1st sem (enrolled)": "curricular_units_1st_sem_enrolled",
        "Curricular units 1st sem (evaluations)": "curricular_units_1st_sem_evaluations",
        "Curricular units 1st sem (approved)": "curricular_units_1st_sem_approved",
        "Curricular units 1st sem (grade)": "curricular_units_1st_sem_grade",
        "Curricular units 1st sem (without evaluations)": "curricular_units_1st_sem_without_evaluations",
        "Curricular units 2nd sem (credited)": "curricular_units_2nd_sem_credited",
        "Curricular units 2nd sem (enrolled)": "curricular_units_2nd_sem_enrolled",
        "Curricular units 2nd sem (evaluations)": "curricular_units_2nd_sem_evaluations",
        "Curricular units 2nd sem (approved)": "curricular_units_2nd_sem_approved",
        "Curricular units 2nd sem (grade)": "curricular_units_2nd_sem_grade",
        "Curricular units 2nd sem (without evaluations)": "curricular_units_2nd_sem_without_evaluations",
        "Unemployment rate": "unemployment_rate",
        "Inflation rate": "inflation_rate",
        "GDP": "gdp",
        "Target": "target"
    }

    df = df.copy()
    df.columns = df.columns.str.strip()
    df = df.rename(columns=column_mapping)

    return df