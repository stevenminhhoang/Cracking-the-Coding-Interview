def char_number(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(c)

    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    else:
        return -1
#
# def palindrome_permutation(s):
#     table = [0 for i in range(ord('z') - ord('a') + 1)]
#     countodd = 0
#     for char in s:
#         x = char_number(char)
#         if x != -1:
#             table[x] += 1
#             if table[x] % 2 != 0:
#                 countodd += 1
#             else:
#                 countodd -= 1
#     return countodd <= 1

def palindrome_permutation(s):
    dic = {}
    countodd = 0
    for char in s:
        x = char_number(char)
        if x != -1:
            dic[x] = dic.get(x, 0) + 1
            
    for val in dic.values():
        if val % 2 != 0:
            countodd += 1

    return countodd <= 1

print(palindrome_permutation('Tact Coa')) # => True
print(palindrome_permutation('jhsabckuj ahjsbckj')) # => True
print(palindrome_permutation('Able was I ere I saw Elba')) # => True
print(palindrome_permutation('So patient a nurse to nurse a patient so')) # => False
print(palindrome_permutation('Random Words')) # => False
print(palindrome_permutation('Not a Palindrome')) # => False
print(palindrome_permutation('no x in nixon')) # => True
print(palindrome_permutation('azAZ')) # True
