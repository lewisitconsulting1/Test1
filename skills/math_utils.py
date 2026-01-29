"""Math utility functions."""

from __future__ import annotations

__all__ = [
    "fibonacci",
    "is_prime",
    "gcd",
    "lcm",
    "factorial",
    "sieve_of_eratosthenes",
]


def fibonacci(n: int) -> list[int]:
    """Return the first *n* Fibonacci numbers."""
    if n <= 0:
        return []
    seq = [0]
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
        seq.append(a)
    return seq


def is_prime(n: int) -> bool:
    """Return True if *n* is a prime number."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of *a* and *b*."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of *a* and *b*."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def factorial(n: int) -> int:
    """Return *n*! (n factorial). Raises ValueError for negative input."""
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def sieve_of_eratosthenes(limit: int) -> list[int]:
    """Return all prime numbers up to *limit* using the Sieve of Eratosthenes."""
    if limit < 2:
        return []
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, limit + 1, i):
                is_p[j] = False
    return [i for i, flag in enumerate(is_p) if flag]
