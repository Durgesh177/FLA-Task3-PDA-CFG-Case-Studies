"""Nondeterministic PDA simulation for palindromes over alphabet {a,b}.

The NPDA guesses the midpoint. It pushes the first half onto its stack,
optionally consumes one middle symbol for odd-length strings, then pops
matching symbols while reading the second half.
"""


def _matches_with_stack(left: str, right: str) -> bool:
    if len(left) != len(right):
        return False
    stack = list(left)
    for symbol in right:
        if not stack or stack.pop() != symbol:
            return False
    return not stack


def is_palindrome_npda(value: str) -> bool:
    """Return True iff value is a palindrome over the alphabet {a, b}."""
    if any(symbol not in {"a", "b"} for symbol in value):
        return False

    # The nondeterministic transition may switch from push to match
    # at any input position. Try every possible midpoint and both parities.
    for midpoint in range(len(value) + 1):
        # Even-length branch: split exactly at midpoint.
        if _matches_with_stack(value[:midpoint], value[midpoint:]):
            return True

        # Odd-length branch: skip one central symbol.
        if midpoint < len(value):
            if _matches_with_stack(value[:midpoint], value[midpoint + 1:]):
                return True

    return False


if __name__ == "__main__":
    for sample in ["", "a", "abba", "aba", "aabbaa", "abab", "abc"]:
        print(f"{sample!r}: {'ACCEPT' if is_palindrome_npda(sample) else 'REJECT'}")
