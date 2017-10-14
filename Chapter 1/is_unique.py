# def unique(string):
#     if len(string) > 128:
#         return False
#
#     char_set = [False for _ in range(128)]
#     for char in string:
#         value = ord(char)
#         # print(value)
#
#         if char_set[value]:
#             return False
#
#         char_set[value] = True
#
#     return True

def unique(string):
    unique_array = set()
    for c in string:
        if c in unique_array:
            return False
        else:
            unique_array.add(c)
    return True

print(unique('Steven'))
