"""Formal CFG definitions used in the Task 3 case studies.

Balanced brackets (multiple bracket types):
    G1 = ({S}, {(, ), [, ], {, }}, P1, S)
    S -> (S)S | [S]S | {S}S | ε

Arithmetic expressions (EBNF shorthand):
    E -> T ((+ | -) T)*
    T -> F ((* | /) F)*
    F -> -F | (E) | identifier | integer

Palindromes over {a,b}:
    G3 = ({S}, {a,b}, P3, S)
    S -> aSa | bSb | a | b | ε

The arithmetic grammar is implemented by recursive descent in
arithmetic_expression.py. The other two grammars describe the languages
recognized by their stack-based / NPDA-style recognizers.
"""

BALANCED_BRACKETS_PRODUCTIONS = (
    "S -> (S)S | [S]S | {S}S | ε",
)

ARITHMETIC_EXPRESSION_PRODUCTIONS = (
    "E -> T ((+ | -) T)*",
    "T -> F ((* | /) F)*",
    "F -> -F | (E) | identifier | integer",
)

PALINDROME_PRODUCTIONS = (
    "S -> aSa | bSb | a | b | ε",
)
