"""Stack-based PDA for balanced (), [] and {} brackets."""

OPEN_TO_CLOSE = {"(": ")", "[": "]", "{": "}"}
CLOSERS = set(OPEN_TO_CLOSE.values())


def is_balanced(expression: str) -> bool:
    """Accept iff brackets are properly nested and all brackets match.

    Non-bracket characters are ignored, allowing examples such as
    'a*(b+c)' to be checked for bracket balance.
    """
    stack = []
    for symbol in expression:
        if symbol in OPEN_TO_CLOSE:
            stack.append(symbol)
        elif symbol in CLOSERS:
            if not stack or OPEN_TO_CLOSE[stack.pop()] != symbol:
                return False
    return not stack


if __name__ == "__main__":
    for sample in ["()", "([]{})", "([)]", "((x+y)*z)", "(()"]:
        print(f"{sample!r}: {'ACCEPT' if is_balanced(sample) else 'REJECT'}")
