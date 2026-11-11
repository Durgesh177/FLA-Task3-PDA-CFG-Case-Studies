"""Recursive-descent recognizer for a small arithmetic-expression CFG.

Grammar (EBNF):
    E  -> T (('+' | '-') T)*
    T  -> F (('*' | '/') F)*
    F  -> '-' F | '(' E ')' | IDENTIFIER | INTEGER

Whitespace is ignored. Identifiers use [A-Za-z_][A-Za-z0-9_]*.
Integer literals use decimal digits.
"""

import re

TOKEN_RE = re.compile(r"\s*(?:(\d+)|([A-Za-z_][A-Za-z0-9_]*)|(.))")


def tokenize(source: str):
    tokens = []
    position = 0
    while position < len(source):
        match = TOKEN_RE.match(source, position)
        if not match:
            raise ValueError("Invalid token")
        number, identifier, other = match.groups()
        token = number or identifier or other
        if token.isspace():
            position = match.end()
            continue
        if other and other not in "+-*/()":
            raise ValueError(f"Unexpected character: {other}")
        tokens.append(token)
        position = match.end()
    return tokens


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def peek(self):
        return self.tokens[self.index] if self.index < len(self.tokens) else None

    def consume(self, expected=None):
        token = self.peek()
        if token is None or (expected is not None and token != expected):
            raise ValueError(f"Expected {expected!r}, got {token!r}")
        self.index += 1
        return token

    def parse_expression(self):
        self.parse_term()
        while self.peek() in ("+", "-"):
            self.consume()
            self.parse_term()

    def parse_term(self):
        self.parse_factor()
        while self.peek() in ("*", "/"):
            self.consume()
            self.parse_factor()

    def parse_factor(self):
        token = self.peek()
        if token == "-":
            self.consume("-")
            self.parse_factor()
        elif token == "(":
            self.consume("(")
            self.parse_expression()
            self.consume(")")
        elif token is not None and (token.isdigit() or
                                    re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", token)):
            self.consume()
        else:
            raise ValueError(f"Expected identifier, integer or '(', got {token!r}")


def is_valid_expression(source: str) -> bool:
    try:
        tokens = tokenize(source)
        if not tokens:
            return False
        parser = Parser(tokens)
        parser.parse_expression()
        return parser.peek() is None
    except ValueError:
        return False


if __name__ == "__main__":
    for sample in ["a+b*c", "(a+b)*12", "-x/3", "a+", "(a+b", "2**3"]:
        print(f"{sample!r}: {'ACCEPT' if is_valid_expression(sample) else 'REJECT'}")
