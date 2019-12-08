def pad_string(data, size, padding_character=' ', direction='left'):
    """This new function will determine if it will pad to the left or the right by using an if statement."""
    if direction == 'left':
        data.rjust(size, padding_character)
    elif data == 'right':
        data.ljust(size, padding_character)
    return data

def pad_left(data, size, padding_character=' '):
    """This new function will call pad_string and use it to pad to the left"""
    result_left = pad_string(data, size, padding_character, 'left')
    return result_left


def pad_right(data, size, padding_character=' '):
    """This new function will call pad_string and use it to pad to the left"""
    result_right = pad_string(data, size, padding_character, 'right')
    return result_right


# Output Test Code
print(len(pad_left('abc', 10)))
print(len(pad_right('abc', 10)))
print(pad_left('abc', 10, '0'))
print(pad_right('abc', 10, '0'))