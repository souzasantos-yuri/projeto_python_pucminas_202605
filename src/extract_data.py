import pandas as pd
from pathlib import Path
    
def extract_data() -> pd.DataFrame:
    """
    Lê os dados raw do CSV.
    """
    base_dir = Path(__file__).parent.parent / "data" / "raw" / "f1_results.csv"
    return pd.read_csv(base_dir)