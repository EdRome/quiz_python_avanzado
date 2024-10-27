import os
import argparse
import multiprocessing
from typing import List, Dict

def count_words_single_file(file_path: str) -> int:
    """Count the words in a single text file.
    
    Args:
        file_path (str): Path to text file.
        
    Returns:
        int: Number of total words in a file.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        words = text.split()
        return len(words)

def parallel_word_count(file_paths: List[str]) -> Dict[str, int]:
    """Count the number of words on multiple text file using multiprocessing Pool.
    
    Args:
        file_paths (List[str]): List of text file paths.
        
    Returns:
        Dict[str, int]: Dictionary with the file name and the number of total words.
    """
    results = {}
    with multiprocessing.Pool() as pool:
        # Exectue the parallel word counting for each file
        countings = pool.map(count_words_single_file, file_paths)
        
        # Create the dictionary with the file name and its word counting.
        results = {os.path.basename(file_path): count for file_path, count in zip(file_paths, countings)}
            
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ejercicio 7 - Procesamiento Paralelo de Archivos de Texto')
    parser.add_argument("-l", nargs='+', default=['./resources/text/file1.txt', './resources/text/file2.txt'])

    args = parser.parse_args()

    list_value = args.l

    result = parallel_word_count(list_value)
    print(result)
