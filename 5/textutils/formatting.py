"""Text formatting utilities."""

import re


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word."""
    return ' '.join(word.capitalize() for word in text.split())


def format_phone(phone: str) -> str:
    """Format phone number to (XXX) XXX-XXXX format."""
    digits = re.sub(r'\D', '', phone)
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return phone


def format_currency(amount: float, currency: str = 'EUR') -> str:
    """Format amount as currency string."""
    return f"{amount:,.2f} {currency}"

