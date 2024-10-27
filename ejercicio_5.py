import pytest
import argparse
from ejercicio_5_is_palindrome import is_palindrome

parser = argparse.ArgumentParser(description='Ejercicio 5 - Testeo Automatizado con Pytest')
parser.add_argument("-s", type=str, default='python')

args = parser.parse_args()

word = args.s

result = "es" if is_palindrome(word) else "no es"
print(f"La palabra '{word}' {result} palindromo")