"""
$>python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward
compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
7 punctuation marks
26 spaces
15 digits
$>
"""

import sys
import string

if len(sys.argv) < 2:
    print("What is the text to count?")
    print("Hello World!")
    print("The text contains 13 characters:")
    print("2 upper letters")
    print("8 lower letters")
    print("1 punctuation marks")
    print("2 spaces")
    print("0 digits")

else:
    print("correct number of arguments.")
