import pandas as pd
from pathlib import Path

columns_to_drop = ['fastest_lap_rank', 'driver_id', 'constructor_id']
columns_to_rename = ({"constructor": "team"})

def drop_columns(df: pd.DataFrame, columns_to_drop: list) -> pd.DataFrame:
    """
    Deleta colunas indesejadas.
    """
    return df.drop(columns=columns_to_drop)

def create_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria colunas novas para aprofundar análises.
    """
    df["positions_gained"] = df["grid"] - df["position"]
    df["is_podium"] = df["position"] <= 3
    df["is_top10"] = df["position"] <= 10
    df["race_efficiency"] = df["position"] / df["grid"]
    df["did_finish"] = df["status"] == "Finished"

    return df

def deduplicate_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Deleta dados duplicados se houver.
    """
    if df.duplicated().sum() > 0:
        df = df.drop_duplicates()
    else:
        return df
    
def handle_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """
    Faz a validação de dados nulos e faz o tratamento deles.
    """
    null_count = df.isna().sum().sum()

    if null_count > 0:
        df = df.fillna({
            "season": 0,
            "round": 0,
            "race_name": "unknown",
            "driver_name": "unknown",
            "constructor": "unknown",
            "grid": 0,
            "position": 0,
            "points": 0.0,
            "laps": 0,
            "status": "unknown",
            "time": "unknown",
            "fastest_lap": "unknown",
            "positions_gained": 0,
            "is_podium": "unknown",
            "is_top10": "unknown",
            "race_efficiency": 0.0,
            "did_finish": "unknown",

        }, inplace=True)
        return df
    else:
        print("No nullified fields.")
        return df

def rename_columns(df: pd.DataFrame, columns_to_rename: dict) -> pd.DataFrame:
    """
    Renomeia as colunas desejadas.
    """
    return df.rename(columns=columns_to_rename)

def data_transformation(df: pd.DataFrame) -> pd.DataFrame:
    """
    Faz o processo completo de transformação.
    """
    df = drop_columns(df, columns_to_drop=columns_to_drop)
    df = create_columns(df)
    df = deduplicate_data(df)
    df = handle_nulls(df)
    df = rename_columns(df, columns_to_rename=columns_to_rename)
    return df