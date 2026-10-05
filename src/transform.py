import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/content/KaggleV2-May-2016.csv')
def clean_ages(df: pd.DataFrame) -> pd.DataFrame:
    """Elimina edades negativas y mayores a 100."""
    return df[(df['Age'] >= 0) & (df['Age'] <= 100)]

def fix_temporal_errors(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza fechas y elimina citas anteriores al agendamiento."""
    df['ScheduledDay_date'] = pd.to_datetime(df['ScheduledDay']).dt.normalize()
    df['AppointmentDay_date'] = pd.to_datetime(df['AppointmentDay']).dt.normalize()
    return df[df['AppointmentDay_date'] >= df['ScheduledDay_date']]

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """Genera variables para el análisis."""
    df['Tiempo_Espera'] = (df['AppointmentDay_date'] - df['ScheduledDay_date']).dt.days
    df['Dia_Semana'] = df['AppointmentDay_date'].dt.day_name()
    df['No_show_num'] = df['No_show'].map({'Yes': 1, 'No': 0})
    return df