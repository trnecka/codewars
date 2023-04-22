"""
Task assignment:

In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

    "one" => 1
    "twenty" => 20
    "two hundred forty-six" => 246
    "seven hundred eighty-three thousand nine hundred and nineteen" => 783919

Additional Notes:

    The minimum number is "zero" (inclusively)
    The maximum number, which must be supported is 1 million (inclusively)
    The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
    All tested numbers are valid, you don't need to validate the
"""


def parse_int(string: str) -> int:
    """
    >>> parse_int('zero')
    0
    >>> parse_int('one')
    1
    >>> parse_int('twenty')
    20
    >>> parse_int('fifty-four')
    54
    >>> parse_int('one hundred')
    100
    >>> parse_int("two hundred forty-six")
    246
    >>> parse_int("two thousand five hundred and fifty-six")
    2556
    >>> parse_int('five thousand')
    5000
    >>> parse_int("one thousand twenty-four")
    1024
    >>> parse_int("twenty-one thousand five hundred thirty")
    21530
    >>> parse_int("two hundred thousand five")
    200005
    >>> parse_int("seven hundred eighty-three thousand nine hundred and nineteen")
    783919
    >>> parse_int("twenty-four million one hundred one")
    24000101
    """
    numbers = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90
    }
    num = 0
    text_number = [n for n in string.split(' ') if not n == 'and']
    if text_number[-1] not in ['hundred', 'thousand', 'million']:
        num += sum([numbers[n] for n in text_number.pop().split('-')])

    if len(text_number) > 0 and text_number[-1] == 'hundred':
        num += numbers[text_number.pop(-2)] * 100
        text_number.pop()

    if len(text_number) > 0 and text_number[-1] == 'thousand':
        if not text_number[-2] == 'hundred':
            num += sum([numbers[n] for n in text_number.pop(-2).split('-')]) * 1000
        text_number.pop()

    if len(text_number) > 0 and text_number[-1] == 'hundred':
        num += numbers[text_number.pop(-2)] * 100000
        text_number.pop()

    if len(text_number) > 0 and text_number[-1] == 'million':
        num += sum([numbers[n] for n in text_number.pop(-2).split('-')]) * 1000000
        text_number.pop()

    return num


if __name__ == "__main__":
    import doctest
    doctest.testmod()
