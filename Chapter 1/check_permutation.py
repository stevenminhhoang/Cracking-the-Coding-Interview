from collections import Counter
def check_permutation(a,b):
    counter = Counter()
    if len(a) != len(b):
        return False
    for char in a:
        counter[char] += 1

    for char in b:
        if counter[char] == 0:
            return False
        counter[char] -= 1
    return True

print(check_permutation("abbcd",'baccbd'))
