def unique(string):
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        value = ord(char)
        # print(value)

        if char_set[value]:
            return False

        char_set[value] = True

    return True

print(unique('ABCA'))
