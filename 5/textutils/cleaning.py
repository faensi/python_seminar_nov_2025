"""Text cleaning utilities."""

import re


def remove_whitespace(text: str) -> str:
    """Remove extra whitespace from text."""
    return ' '.join(text.split())


def remove_special_chars(text: str, keep_spaces: bool = True) -> str:
    """Remove special characters from text."""
    if keep_spaces:
        pattern = r'[^a-zA-Z0-9\s]'
    else:
        pattern = r'[^a-zA-Z0-9]'
    return re.sub(pattern, '', text)


def normalize_text(text: str) -> str:
    """Normalize text by removing extra whitespace and converting to lowercase."""
    return remove_whitespace(text).lower()

