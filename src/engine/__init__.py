import os.path

FONT_PATH = os.path.join('res', 'fonts')
FONT_CONFIG_EXTENSION = '.font.json'

window_dimensions = None
tile_dimensions = None
mouse_position = None

def parse_text_into_characters(text):
    characters = []
    is_escaping = False
    group = None
    for ch in text:
        if ch == '\\':
            if is_escaping:
                characters.append(ch)
                is_escaping = False
            else:
                is_escaping = True
        elif ch == '[':
            if is_escaping:
                characters.append(ch)
                is_escaping = False
            else:
                if group is not None:
                    raise ValueError('You cannot start a character group within another group.')
                group = ''
            is_escaping = False
        elif ch == ']':
            if is_escaping:
                characters.append(ch)
            else:
                if group is None:
                    raise ValueError('You cannot end a character group that you have not started.')
                characters.append(group)
                group = None
            is_escaping = False
        else:
            if is_escaping:
                raise ValueError('Invalid escape character \'' + ch + '\'.')
            if group is None:
                characters.append(ch)
            else:
                group += ch
            is_escaping = False
    if group is not None:
        raise ValueError('You started a character group but did not finish it.')
    return characters