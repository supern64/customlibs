# CSSParser
# Simple CSS to dict parser based on cssutils
# DOES NOT HANDLE @ RULES!!!!

import cssutils

def parse_file(filename):
    """Parses a CSS sheet from file. Returns a dict."""
    sheet = cssutils.parseFile(filename)
    parsed = {}
    for rule in sheet:
		if rule.selectorText.startswith(".") or rule.selectorText.startswith("#"):
			selectorText = rule.selectorText[1:]
		else:
			selectorText = rule.selectorText
		parsed[selectorText] = {}
		for property in rule.style:
	    	name = property.name
	    	parsed[selectorText][name] = property.value
    return parsed
def parse_text(string):
    """Parses a CSS sheet from a string. Returns a dict."""
    sheet = cssutils.parseString(filename)
    parsed = {}
    for rule in sheet:
		if rule.selectorText.startswith(".") or rule.selectorText.startswith("#"):
			selectorText = rule.selectorText[1:]
		else:
			selectorText = rule.selectorText
		parsed[selectorText] = {}
		for property in rule.style:
	    	name = property.name
	    	parsed[selectorText][name] = property.value
    return parsed
