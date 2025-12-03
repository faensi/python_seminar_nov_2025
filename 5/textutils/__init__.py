"""
TextUtils - A text processing utilities package.

This package provides various utilities for text cleaning, formatting, and analysis.
"""

from .cleaning import remove_whitespace, remove_special_chars, normalize_text
from .formatting import capitalize_words, format_phone, format_currency
from .analysis import word_count, char_count, find_keywords
from .validators import validate_email, validate_phone, validate_text_length

__all__ = [
    # Cleaning functions
    'remove_whitespace',
    'remove_special_chars',
    'normalize_text',
    # Formatting functions
    'capitalize_words',
    'format_phone',
    'format_currency',
    # Analysis functions
    'word_count',
    'char_count',
    'find_keywords',
    # Validator functions
    'validate_email',
    'validate_phone',
    'validate_text_length',
]

__version__ = '0.1.0'

