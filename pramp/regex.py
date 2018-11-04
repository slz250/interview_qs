def is_match(text, pattern):
    if text == '':
        if pattern == '.*':
            return True
        elif len(pattern) == 2 and pattern[-1] == '*':
            return True
        elif pattern == '':
            return True
        else:
            return False

    text_ndx = 0
    pattern_ndx = 0
    while pattern_ndx < len(pattern) and text_ndx < len(text):
        if pattern_ndx + 1 < len(pattern) and pattern[pattern_ndx + 1] == '*':
            pattern_ndx += 2
            text_ndx = max(0, len(text) - (len(pattern) - pattern_ndx))
        elif pattern[pattern_ndx] == '.' or (pattern[pattern_ndx] == text[text_ndx]):
            text_ndx += 1
            pattern_ndx += 1
        else:
            return False
    return pattern_ndx == len(pattern) and text_ndx == len(text)