import math
import re


def numeric_validate(test, action_type, min_val="0", max_val="100"):
    if action_type == '0':
        return True
    if action_type == '1':
        return re.match(r'^(\d+)$', test.strip()) is not None and int(min_val.strip()) <= int(test.strip()) <= int(max_val.strip())
    return False

def hours_validate(test, action_type, max_val="12"):
    if action_type == '0':
        return True
    if action_type == '1':
        return re.match(r'^\d{1,2}$', test.strip()) is not None and 0 < int(test.strip()) <= int(max_val.strip())
    return False

def minutes_validate(test, action_type, max_val="59"):
    if action_type == '0':
        return True
    if action_type == '1':
        count = str(int(math.log10(int(max_val.strip()))) + 1) if str(max_val.strip()).isdigit() else "2"
        return re.match(r'^\d{1,' + re.escape(count) + '}$', test.strip()) is not None and int(test.strip()) >= 0
    return False
