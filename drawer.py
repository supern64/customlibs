# ASCII box generator
# generate_box() doesn't work with newlines yet
import time
template = """________________________________
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|______________________________|""" # FULL SIZE IS 32x8

# Start writing text on LINE 3, COLUMN 3, each LINE write until COLUMN 30, write until LINE 7
def generate_box(text):
    """Draws a 28x5 characters text box"""
    returning_lines = template.split("\n")
    writing_character = 0
    brk = 0
    for (n2, line) in enumerate(returning_lines): # row alignment
        if n2 >= 2 and n2 <= 6:
            for (n, char) in enumerate(list(returning_lines[n2])): # column alignment
                if n >= 2 and n <= 29:
                    current_split_line = list(returning_lines[n2])
                    try:
                        current_split_line[n] = text[writing_character]
                        returning_lines[n2] = "".join(current_split_line)
                    except IndexError:
                        brk = 1
                        break
                    writing_character = writing_character + 1
                else:
                    continue
            if brk == 1:
                break
        else:
            continue
    writing_character = 0
    brk = 0
    current_split_line = []
    retValue = "\n".join(returning_lines)
    returning_lines = []
    return retValue
def generate_generating_text_animation(text, timing=0.1):
    """Generates an animated text"""
    newline_split = text.split("\n")
    for e in newline_split:
        text_split = list(e)
        writing_character = 1
        for i in text_split:
            print("".join(text_split[0:writing_character]), end="\r")
            writing_character = writing_character + 1
            time.sleep(timing)
        print("")

    
