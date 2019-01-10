# DelimLib
# Parsing dictionary from delimeters

def parse(text, delimeter=":", newline_delimeter="\n"):
    """Parses a delimiter divided text.
    text: The text to parse
    delimeter: The delimeter that seperates keys and values. Defaults to ":".
    newline_delimeter: The delimeters that seperates different lines. Defaults to '\n'"""
    if delimeter == newline_delimeter:
        raise ValueError("Delimeter cannot be the same as the Newline Delimeter.")
    parsedt = text.split(newline_delimeter)
    rtn = dict()
    for i in parsedt:
        b = i.split(delimeter)
        rtn[b[0].strip()] = b[1].strip()
    return rtn

def construct(dict, delimeter=": ", newline_delimeter="\n"):
    """Contruct a delimiter divided text.
    text: The dictionary to construct from
    delimeter: The delimeter that seperates keys and values. Defaults to ": ".
    newline_delimeter: The delimeters that seperates different lines. Defaults to '\n'"""
    if delimeter == newline_delimeter:
        raise ValueError("Delimeter cannot be the same as the Newline Delimeter.")
    l = []
    for i, (k, v) in enumerate(dict.items()):
        l.append(k + delimeter + v)
    return newline_delimeter.join(l)
