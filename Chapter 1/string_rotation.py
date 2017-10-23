def is_substring(s1, s2):
   return s2 in s1

def string_rotation(s1, s2):
    return is_substring(s1 + s1, s2)

print(string_rotation("waterbottle","erbottlewat"))
print(string_rotation("foo foo","foo bar"))
