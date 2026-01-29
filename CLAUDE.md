# CLAUDE.md

This file provides guidance for AI assistants working with this repository.

## Repository Overview

**Repository:** lewisitconsulting1/Test1
**Language:** Python 3.10+
**Description:** A collection of Python utility modules ("skills") covering common algorithms, data structures, and helper functions.

## Project Structure

```
Test1/
├── CLAUDE.md
└── skills/                  # Main package
    ├── __init__.py           # Re-exports all public APIs
    ├── strings.py            # String manipulation (palindrome, Caesar cipher, word frequency)
    ├── math_utils.py         # Math utilities (primes, Fibonacci, GCD/LCM, factorial, sieve)
    ├── file_handler.py       # File I/O helpers (text, JSON, CSV read/write)
    ├── data_structures.py    # Stack, Queue, LinkedList implementations
    └── sorting.py            # Sorting algorithms (bubble, insertion, merge, quick)
```

## Usage

```python
from skills import is_palindrome, fibonacci, Stack, merge_sort

is_palindrome("racecar")       # True
fibonacci(8)                   # [0, 1, 1, 2, 3, 5, 8, 13]

s = Stack()
s.push(42)

merge_sort([3, 1, 4, 1, 5])   # [1, 1, 3, 4, 5]
```

## Development Workflow

### Branching

- Feature branches should follow the naming convention: `claude/<description>-<id>`
- Create pull requests against the main branch

### Commits

- Use clear, descriptive commit messages
- Keep commits focused on a single logical change

### Adding a New Skill Module

1. Create a new `.py` file under `skills/`
2. Define an `__all__` list exporting public names
3. Import the module's exports in `skills/__init__.py`

## Build & Test

No build system or test framework has been configured yet. To run modules directly:

```bash
python -c "from skills import fibonacci; print(fibonacci(10))"
```

## Key Conventions

- Every module defines `__all__` to control its public API
- Functions return new values rather than mutating inputs (e.g. sorting functions return new lists)
- Type hints are used throughout
- Standard library only — no third-party dependencies
- Update this file as the project evolves

## Dependencies

None — all modules use the Python standard library only.
