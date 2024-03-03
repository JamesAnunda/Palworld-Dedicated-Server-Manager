import re


def numeric_validate(test, action_type):
    if action_type == '0':
        return True
    if action_type == '1' and re.match(r'^([\s\d]+)$', test.strip()) is not None:
        return True
    return False

def hours_validate(test, action_type):
    if action_type == '0':
        return True
    if action_type == '1' and re.match(r'^(0?[0-9]|1[0-2])$', test.strip()) is not None:
        return True
    return False


def time_validate(text_after_change, action_type, reason):
    if action_type == '0':
        return True
    if action_type == '1' and re.match(r'^([\s\d:]+)$', text_after_change.strip()) is not None:
        return True
    if action_type == '-1' and reason == 'focusout' and not re.match(r'^(1[0-2]|0?[1-9]):[0-5][0-9]$', text_after_change.strip()):
        return False
    return False
