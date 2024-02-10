def search4vowels(phrase: str) -> set:
    """Display any vowels found in a supplied string."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Display set of letters from 'letters' found in a supplied phrase"""
    return set(letters).intersection(set(phrase))
