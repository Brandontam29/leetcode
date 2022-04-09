def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    result = 0
    l = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1

        charSet.add(s[r])
        result = max(result, r - l + 1)

    return result


print("answer: ", lengthOfLongestSubstring("abcabcabb"))  # 3
print("answer: ", lengthOfLongestSubstring(" "))  # 1
print("answer: ", lengthOfLongestSubstring("pwwkew"))  # 3
