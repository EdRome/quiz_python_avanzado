import time
import math
import logging
import argparse

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("execution_times.log"),
        logging.StreamHandler()
    ]
)


def timing_decorator(func):
    """Decorator measuring and registering the execution time of a function in a log file.
    
    Args:
        func (callable): Function to be decorated.
        
    Returns:
        callable: Function decorated with time measure.
    """
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        logging.info(fin-inicio)
        return resultado
    return wrapper

@timing_decorator
def calculate_factorial(n):
    return math.factorial(n)

parser = argparse.ArgumentParser(description='Ejercicio 2 - Decorador para Medir el Tiempo de Ejecución')
parser.add_argument("-n", type=int, default=50)

args = parser.parse_args()

opt1_value = args.n
_ = calculate_factorial(opt1_value)