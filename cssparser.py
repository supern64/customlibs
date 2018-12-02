# CSSParser
# Simple CSS to dict parser based on cssutils

import cssutils

def parse_file(filename):
    """Parses a CSS sheet from file. Returns a dict."""
    sheet = cssutils.parseFile(filename)
    parsed = {}
    for rule in sheet:
	parsed[rule.selectorText[1:]] = {}
	for property in rule.style:
	    name = property.name
	    parsed[rule.selectorText[1:]][name] = property.value
    return parsed
def parse_text(string):
    """Parses a CSS sheet from a string. Returns a dict."""
    sheet = cssutils.parseString(filename)
    parsed = {}
    for rule in sheet:
	parsed[rule.selectorText[1:]] = {}
	for property in rule.style:
	    name = property.name
	    parsed[rule.selectorText[1:]][name] = property.value
    return parsed
