import pandas as pd
from pathlib import Path

def load_data(df: pd.DataFrame) -> None:
    """
    Salva os dados em um arquivo CSV novo
    """
    output_path = Path(__file__).parent.parent / "data" / "processed" / "f1_results_processed.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, sep=",", index=False, encoding="utf-8")