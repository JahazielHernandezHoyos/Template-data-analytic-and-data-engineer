"""Script principal para ejecutar el flujo de trabajo."""

from src.data_cleaning import ParquetDataCleaner
from src.data_processing import ParquetDataProcessor
from src import utils
import config


def main():
    """Ejecuta el flujo de trabajo principal."""
    data_info = utils.read_csv(config.CSV_FILE)

    data_cleaner = ParquetDataCleaner()
    data_processor = ParquetDataProcessor()

    for index, row in data_info.iterrows():
        parquet_path = config.RAW_DATA_PATH + row["path"]
        processed_data = data_cleaner.clean(parquet_path)

        # Dividir y guardar los datos en archivos .npy
        train_data, val_data = data_processor.split_data(
            processed_data, config.TRAIN_RATIO
        )
        data_processor.save_npy_file(
            train_data,
            f"{config.NPY_DATA_PATH}{row['participant_id']}_{row['sequence_id']}_train.npy",
        )
        data_processor.save_npy_file(
            val_data,
            f"{config.NPY_DATA_PATH}{row['participant_id']}_{row['sequence_id']}_val.npy",
        )


if __name__ == "__main__":
    main()
