def is_palindrome(word):
    """Checks whether a word is a palindrome."""
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
