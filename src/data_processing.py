"""Módulo para el procesamiento y almacenamiento de datos."""

import numpy as np


class DataProcessor:
    """Clase base para el procesamiento de datos."""

    def split_data(self, data, train_ratio):
        """Método para dividir los datos en conjuntos de entrenamiento y validación."""
        pass

    def save_npy_file(self, data, file_path):
        """Guarda los datos en un archivo .npy.

        Args:
            data (array): Datos a guardar.
            file_path (str): Ruta del archivo de salida.
        """
        np.save(file_path, data)


class ParquetDataProcessor(DataProcessor):
    """Clase para el procesamiento de datos en formato parquet."""

    def split_data(self, data, train_ratio):
        """Divide los datos en conjuntos de entrenamiento y validación.

        Args:
            data (DataFrame): Datos a dividir.
            train_ratio (float): Proporción de datos para el conjunto de entrenamiento.

        Returns:
            tuple: Datos de entrenamiento y validación.
        """
        pass
