import pytest
from ejercicio_5_is_palindrome import is_palindrome

def test_is_palindrome_single_words():
    assert is_palindrome("ana") == True
    assert is_palindrome("oso") == True
    assert is_palindrome("arenera") == True
    assert is_palindrome("reconocer") == True

def test_is_palindrome_with_spaces_and_upper_case():
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("Anita lava la tina") == True
    assert is_palindrome("Dabale arroz a la zorra el abad") == True

def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False

def test_is_not_palindrome():
    assert is_palindrome("palabra") == False
    assert is_palindrome("Python") == False
    assert is_palindrome("programacion") == False

def test_palindrome_special_cases():
    assert is_palindrome("") == True  # Una cadena vacía se considera un palíndromo
    assert is_palindrome("a") == True  # Una sola letra se considera un palíndromo
