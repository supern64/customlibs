# CSSParser
# Simple CSS to dict parser based on cssutils
# DOES NOT HANDLE @ RULES!!!!

import cssutils

def parse_file(filename, use_string=True):
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
            if use_string == True or use_string != False:
                parsed[selectorText][name] = property.value.replace('"', "").replace("'", "")
            else:
                parsed[selectorText][name] = property.value
    return parsed
def parse_string(string, use_string=True):
    """Parses a CSS sheet from a string. Returns a dict."""
    sheet = cssutils.parseString(string)
    parsed = {}
    for rule in sheet:
        if rule.selectorText.startswith(".") or rule.selectorText.startswith("#"):
            selectorText = rule.selectorText[1:]
        else:
            selectorText = rule.selectorText
        parsed[selectorText] = {}
        for property in rule.style:
            name = property.name
            if use_string == True or use_string != False:
                parsed[selectorText][name] = property.value.replace('"', "").replace("'", "")
            else:
                parsed[selectorText][name] = property.value
    return parsed
def construct_css_string(dic, use_string=True):
    """Constructs a CSS formatted string from a dictionary (You might have to put quotes in some locations!)"""
    string = ""
    for i, (k, v) in enumerate(dic.items()):
        if i == 0:
            string = string + "." + k + " {\n"
        else:
            string = string + "\n." + k + " {\n"
        for s, (c, j) in enumerate(v.items()):
            if use_string == True or use_string != False:
                string = string + "    " + c + ': "' + j + '";\n'
            else:
                string = string + "    " + c + ": " + j + ";\n"
        string = string + "}"
    return string
def construct_css_to_file(dic, filename, use_string=True):
    """Constructs a CSS formatted string from a dictionary then saves it to a file. (You might have to put quotes in some locations!)"""
    string = ""
    for i, (k, v) in enumerate(dic.items()):
        if i == 0:
            string = string + "." + k + " {\n"
        else:
            string = string + "\n." + k + " {\n"
        for s, (c, j) in enumerate(v.items()):
            if use_string == True or use_string != False:
                string = string + "    " + c + ': "' + j + '";\n'
            else:
                string = string + "    " + c + ": " + j + ";\n"
        string = string + "}"
    open(filename, "w+").write(string)
    return
