from typing import Generator
import argparse

def prime_sequence_generator(n: int) -> Generator[int, None, None]:
    """Generate prime numbers until n limit
    
    Args:
        n (int): Integer limit to search for prime numbers
        
    Yields:
        int: Prime numbers until integer limit
    """
    def is_prime(n: int) -> bool:
        """Verify is a number is prime
        
        Args:
            n (int): Number to verify.
        
        Returns:
            bool: True if prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, n + 1):
        if is_prime(num):
            yield num


parser = argparse.ArgumentParser(description='Ejercicio 1 - Generador de Secuencias Primas Grandes')
parser.add_argument("-n", type=int, default=50)

args = parser.parse_args()

opt1_value = args.n
gen = prime_sequence_generator(opt1_value)
print("Resultado :", list(gen))