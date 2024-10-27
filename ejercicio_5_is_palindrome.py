def is_palindrome(word: str) -> bool:
    """Validate if a word is a palindrome.
    
    Args:
        word (str): Word to verify.
        
    Returns:
        bool: True if palindrome, False otherwise.
    """
    # Normalizar palabra (ignorar mayúsculas y minúsculas, y espacios)
    clean_word = word.replace(" ", "").lower()
    return clean_word == clean_word[::-1]