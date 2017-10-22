def one_away(a, b):
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                if a[i+1:] != b[i+1:]:
                    return False
        return True
    elif len(a) - len(b) == 1:
        for i in range(len(b)):
            if a[i] != b[i]:
                if a[i+1:] != b[i:]:
                    return False
        return True
    elif len(b) - len(a) == 1:
        for i in range(len(a)):
            if a[i] != b[i]:
                if a[i:] != b[i+1:]:
                    return False
        return True
    else:
        return False

print(one_away("pal","palks"))
