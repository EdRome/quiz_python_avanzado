import csv
import os
import argparse
import asyncio
from typing import List

async def single_csv_sum(filepath: str):
    """Sum values in the 'value' column inside a CSV file.

    Args:
        filepath (str): Rout to CSV file.

    Returns:
        int: Sum of values in column 'value'.
    """
    suma = 0
  
    # Execute I/O operation within a subprocess to avoid block at the async loop.
    def read_csv_file():
        with open(filepath, mode='r') as archivo:
            lector_csv = csv.DictReader(archivo)
            return sum([int(fila['value']) for fila in lector_csv])

    # Use run_in_executor to do the I/O operation as a concurrent process.
    suma = await asyncio.get_running_loop().run_in_executor(None, read_csv_file)
    return suma

async def async_csv_sum(file_paths: List[str]):
    """Calculate the sum of column 'value' inside multiple CSV files.

    Args:
        file_paths (List[str]): List of CSV filepaths.
  
    Returns:
        Dict[str, int]: A dictionary with the filename and its corresponding sum.
    """
    results = {}
    tasks = [single_csv_sum(file_path) for file_path in file_paths]
    sumas = await asyncio.gather(*tasks)
    results = {
        os.path.basename(ruta): suma
        for ruta, suma in zip(file_paths, sumas)
    }
    return results

parser = argparse.ArgumentParser(description='Ejercicio 4 - Análisis Asincrono de Archivos CSV')
parser.add_argument("-l", nargs='+', default=['./resources/csv/data1.csv', './resources/csv/data2.csv'])

args = parser.parse_args()

list_value = args.l
result = asyncio.run(async_csv_sum(list_value))
print(result)