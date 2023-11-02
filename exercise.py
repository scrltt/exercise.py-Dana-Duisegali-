"""
This is called a 'docstring', it is used in the tests: do not modify it
The lines with '>>>' provide examples that you can try in the interpreter,
the expected result is the line below.

Examples:

>>> count_char("GAGCCTACTAACGGGAT", "G")
5

>>> count_char("", "G")
0


>>> count_char("G", "GAGCCTACTAACGGGAT")
Traceback (most recent call last):
...
AssertionError


>>> count_all_chars("GAGCCTACTAACGGGAT", "GA")
10

>>> count_all_chars("GAGCCTACTAACGGGAT", "AG")
10

>>> count_all_chars("GAGCCTACTAACGGGAT", "AA")
10


"""

def count_char(string: str, char: str) -> int:
    """Return the number of times `char` occurs in `string."""
    assert len(char) == 1
    count: int = 0
    for c in string:
        if c == char:
            count += 1  
    return count

def count_all_chars(string: str, chars: str) -> int:
    """Return the total number of times all the `chars` occur in `string."""
    total_count = 0
    for char in chars:
        total_count += count_char(string, char)  
    return total_count

# Do not change anything below
if __name__ == "__main__":
    import doctest
    import sys
    fail, _ = doctest.testmod()
    sys.exit(fail)
