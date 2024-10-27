import argparse

class instance_counter_metaclass(type):
    """Metaclass that count the number of instance created for a class."""
    
    def __new__(cls, name, bases, dct):
        # Initialize instance counter at 0
        c = super().__new__(cls, name, bases, dct)
        c.instance_count = 0
        return c
    
    def __call__(cls, *args, **kwargs):
        # Each time an instance is created, increment counter by 1
        instancia = super().__call__(*args, **kwargs)
        cls.instance_count += 1
        return instancia

class Person(metaclass=instance_counter_metaclass):
    def __init__(self, name):
        self.name = name

parser = argparse.ArgumentParser(description='Ejercicio 3 - Metaprogramación Contador de Instancias')
parser.add_argument("-l", nargs='+', default=['Alice', 'Bob'])

args = parser.parse_args()

list_value = args.l
_ = [Person(value) for value in list_value]
print("Num. Instancias creadas: ", Person.instance_count)
