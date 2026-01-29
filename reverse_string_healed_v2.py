"""
reverse_string_healed_v2.py
Automatically healed using canonical logic_reference.py.
Original reverse_string.py is preserved. This file is import-only and modular.
"""
def reverse_string(s):
    """
    @contract: Reverse the input string.
    @input: s (str)
    @output: str
    @example: 'abc' -> 'cba'
    @invariant: len(output) == len(s)
    """
    return s[::-1]

if __name__ == '__main__':
    test = 'hello'
    print('Reversed:', reverse_string(test))
