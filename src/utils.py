"""Módulo de utilidades."""

import pandas as pd


def read_csv(csv_path):
    """Lee un archivo CSV y devuelve un DataFrame.

    Args:
        csv_path (str): Ruta del archivo CSV.

    Returns:
        DataFrame: Datos leídos del archivo CSV.
    """
    df = pd.read_csv(csv_path)
    return df
