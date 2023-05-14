import itertools
import re

def solve(formula):
    """Given a formula like 'NUM + BER = PLAY', fill in digits to solve it.
    Generate all valid digit-filled-in strings."""
    return filter(valid, letter_replacements(formula))

def letter_replacements(formula):
    """All possible replacements of letters with digits in formula."""
    formula = formula.replace(' = ', ' == ') # Allow = or ==
    letters = cat(set(re.findall('[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        yield formula.translate(str.maketrans(letters, cat(digits)))

def valid(exp):
    """Expression is valid iff it has no leading zero, and evaluates to true."""
    try:
        return not leading_zero(exp) and eval(exp) is True
    except ArithmeticError:
        return False
    
cat = ''.join # Function to concatenate strings
    
leading_zero = re.compile(r'\b0[0-9]').search # Function to check for illegal number
x=input("Enter with space between words \n")
print(next(solve(x)))
