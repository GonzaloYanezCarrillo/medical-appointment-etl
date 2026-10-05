# Proyecto Académico: Pipeline ETL - Análisis de Ausentismo Médico

Este repositorio contiene un ejercicio práctico de **ETL (Extracción, Transformación y Carga)** enfocado en la limpieza y estructuración de datos de salud. 

El proyecto fue desarrollado originalmente como un análisis exploratorio en **Google Colab** para fines académicos, y posteriormente refactorizado bajo una arquitectura modular de ingeniería de datos para su publicación en GitHub.

## 📊 Sobre el Dataset
El proyecto utiliza el dataset público de Kaggle **[Medical Appointment No Shows](https://www.kaggle.com/datasets/joniarroba/noshowappointments)** (KaggleV2-May-2016.csv), el cual contiene más de 110.000 registros de citas médicas en Brasil. El objetivo original de estos datos es predecir si un paciente asistirá o no a su consulta médica.

## ⚙️ Fases del Proceso ETL

1. **Extract (Extracción):** Lectura e ingesta del archivo `.csv` crudo desde una ruta local aislada.
2. **Transform (Transformación):** 
   - **Limpieza de anomalías biológicas:** Filtrado de edades imposibles (menores a 0) y *outliers* extremos (mayores a 100 años).
   - **Corrección de errores lógicos temporales:** Normalización de formatos `datetime` a medianoche (`00:00:00`) para salvar +38.000 registros de pacientes atendidos el mismo día del agendamiento, previniendo falsos negativos en la resta de fechas.
   - **Feature Engineering:** Creación de nuevas variables analíticas como `Tiempo_Espera` (días), `Dia_Semana`, y binarización de la variable objetivo (`No_show_num`).
3. **Load (Carga):** Exportación del *DataFrame* limpio y estructurado a un nuevo archivo `.csv`, listo para ser consumido por herramientas de visualización o modelos de Machine Learning.

## 🗂️ Arquitectura del Proyecto

El código fue modularizado separando responsabilidades, simulando un entorno de producción:

```text
medical-appointments-etl/
│
├── data/                   # (Ignorado en git) Almacenamiento de datos
│   ├── raw/                # Dataset original (KaggleV2-May-2016.csv)
│   └── processed/          # Dataset limpio tras la ejecución del ETL
│
├── notebooks/              
│   └── analisis_exploratorio.ipynb  # Cuaderno original de Google Colab
│
├── src/                    # Código fuente
│   ├── __init__.py
│   ├── extract.py          # Lógica de lectura de datos
│   ├── transform.py        # Reglas de negocio y limpieza
│   └── load.py             # Lógica de exportación/persistencia
│
├── main.py                 # Orquestador del pipeline ETL
├── .gitignore              # Reglas de exclusión de archivos pesados/sensibles
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación