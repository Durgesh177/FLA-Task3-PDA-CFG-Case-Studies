# FLA Task 3 – PDA and CFG Case Studies

**Course:** 21CSC301T – Formal Language and Automata  
**Student:** Bennu Durgesh Naraharisetti  
**Register Number:** RA2411026050065

This repository demonstrates context-free grammars (CFGs) and pushdown automata (PDAs) through three case studies.

## Case studies

1. **Balanced brackets** – recognizes correctly nested parentheses, square brackets and curly braces using a stack.
2. **Arithmetic expressions** – recognizes expressions using a recursive-descent parser based on a CFG. It supports identifiers, integer literals, parentheses, unary minus, addition, subtraction, multiplication and division.
3. **Palindromes** – simulates a nondeterministic PDA over `{a,b}`, guessing the midpoint, pushing the first half and matching the second half. Both even- and odd-length palindromes are supported.

## Files

```text
FLA-Task3-PDA-CFG-Case-Studies/
├── README.md
├── balanced_parentheses.py
├── arithmetic_expression.py
├── palindrome_checker.py
├── cfg.py
├── pda.py
├── test_cases.py
├── requirements.txt
└── diagrams/
    ├── balanced_parentheses_pda.svg
    ├── arithmetic_expression_cfg.svg
    └── palindrome_pda.svg
```

## Run

Python 3.9+ is recommended. No third-party dependencies are required.

```bash
python balanced_parentheses.py
python arithmetic_expression.py
python palindrome_checker.py
python -m unittest -v
```

## CFG definitions

### Balanced brackets
The language of multiple bracket types is most naturally handled with a stack. For a single bracket type, a CFG is:
```
S → (S)S | ε
```
For multiple bracket types:
```
S → (S)S | [S]S | {S}S | ε
```

### Arithmetic expressions
The implementation uses the following precedence-aware grammar:
```
E  → T ((+ | -) T)*
T  → F ((* | /) F)*
F  → -F | (E) | identifier | integer
```
The repetition notation is EBNF shorthand. This grammar makes multiplication/division bind more tightly than addition/subtraction and gives operators of the same level left associativity.

### Palindromes over {a,b}
```
S → aSa | bSb | a | b | ε
```
This grammar generates even- and odd-length palindromes over the alphabet `{a,b}`.

## PDA model notes

- A PDA uses a stack to remember symbols that must be matched later.
- The palindrome recognizer is nondeterministic: it guesses where the first half ends. This is a standard NPDA strategy; the program checks all possible midpoint choices.
- The arithmetic-expression program is a CFG parser (recursive descent), not a PDA transition-table simulator.

## Scope

These are educational recognizers for the grammars and input alphabets stated above. They are not intended as general-purpose programming-language parsers or production validation libraries.
