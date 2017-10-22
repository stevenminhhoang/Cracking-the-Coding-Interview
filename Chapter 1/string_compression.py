def string_compression(s):
    count = 1
    compressed = []
    for i in range(len(s)-1):
        if s[i+1] == s[i]:
            count += 1
        if s[i+1] != s[i]:
            compressed.append(s[i] + str(count))
            count = 1

    # add last repeated character
    compressed.append(s[-1] + str(count))

    return min("".join(compressed), s, key=len)

print(string_compression("abcdef"))
print(string_compression("aabcccccaaa"))
