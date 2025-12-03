"""Text validation utilities."""

import re


def validate_phone(phone: str) -> bool:
    """Validate phone number format (10 digits)."""
    digits = re.sub(r'\D', '', phone)
    return len(digits) == 10


def validate_text_length(text: str, min_length: int = 1, max_length: int = None) -> bool:
    """Validate text length."""
    length = len(text)
    if length < min_length:
        return False
    if max_length is not None and length > max_length:
        return False
    return True

