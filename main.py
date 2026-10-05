from src.extract import load_raw_data
from src.transform import clean_ages, fix_temporal_errors, create_features
from src.load import save_clean_data

def run_etl():
    print("Iniciando ETL...")
    # Extract
    df = load_raw_data('data/raw/KaggleV2-May-2016.csv')
    
    # Transform
    df = clean_ages(df)
    df = fix_temporal_errors(df)
    df = create_features(df)
    
    # Load
    save_clean_data(df, 'data/processed/dataset_limpio.csv')
    print(f"ETL finalizado con éxito. Total registros: {df.shape[0]}")

if __name__ == "__main__":
    run_etl()