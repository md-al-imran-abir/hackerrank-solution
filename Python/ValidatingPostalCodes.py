# Validating Postal Codes

regex_integer_in_range = r"""
    ^[1-9] # matches the first digit to be between 1-9
    \d{5}$ # matches if the next five are digits and that's the end of the string
    """	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"""
    (?=(\d)\d\1{1}) # here we are using lookahead property with beckreference to find the repetitive digit pairs
    """	# Do not delete 'r'.
    # We wouldn't need lookahead if we could use the `regex` module instead of re. 
    # `regex.findall()` has an optional `overlapped` argument which allows to find the overlapped matches


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)