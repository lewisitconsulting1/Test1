"""String manipulation utilities."""

__all__ = [
    "reverse_string",
    "is_palindrome",
    "caesar_cipher",
    "word_frequency",
    "title_case",
]


def reverse_string(s: str) -> str:
    """Return the reversed version of a string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Check whether a string reads the same forwards and backwards (case-insensitive, ignoring spaces)."""
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
    """Encrypt or decrypt text using a Caesar cipher with the given shift."""
    if decrypt:
        shift = -shift
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def word_frequency(text: str) -> dict[str, int]:
    """Return a dictionary mapping each lowercase word to its occurrence count."""
    counts: dict[str, int] = {}
    for word in text.lower().split():
        word = "".join(ch for ch in word if ch.isalnum())
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def title_case(s: str) -> str:
    """Convert a string to title case, capitalising the first letter of every word."""
    return " ".join(w.capitalize() for w in s.split())
