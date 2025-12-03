"""Text analysis utilities."""


def word_count(text: str) -> int:
    """Count the number of words in text."""
    return len(text.split())


def char_count(text: str, include_spaces: bool = True) -> int:
    """Count the number of characters in text."""
    if include_spaces:
        return len(text)
    return len(text.replace(' ', ''))


def find_keywords(text: str, keywords: list) -> list:
    """Find which keywords appear in the text."""
    text_lower = text.lower()
    return [kw for kw in keywords if kw.lower() in text_lower]

