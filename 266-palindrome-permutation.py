# A String is called Palindrome if it reads the same backwards as well as forwards. For example, the String  can be read the same backwards as well as forwards.
# Now, a Permutation of a String S is some String K where S and K contain the same set of characters, however, these characters need not necessarily have the same positions.
# For Example, consider the String ABC. Here, the Strings :
# 1.ACB
# 2.BCA
# 3.BAC
# 4.CAB
# 5.CBA

# are all permutations of it.

# Now, given a String S consisting of lowercase English alphabets, you need to find out whether any permutation of this given String is a Palindrome. If yes, print "YES" (Without quotes) else, print "NO" without quotes.

# Input Format:
# The first and only line of input contains the String S.

# Output Format:
# Print the required answer on a single line


def permutationIsPalindrome(str: str) -> bool:
    mem = set()
    for s in str:
        if not s in mem:
            mem.add(s)
            continue

        mem.remove(s)

    return len(mem) <= 1


print(permutationIsPalindrome(
    "a"))
print(permutationIsPalindrome(
    "abcabc"))
print(permutationIsPalindrome(
    "aaaacc"))

print(permutationIsPalindrome(
    "asdfdfgjhfghjksdfgwsrtyfnbmfyuqqweproiuqweporuwoufdyghvzxlkcbxcvnmslkdjahfpalksjdpqioweyhosijfghnbxcvmbskjdhfpwairehgflskjfbnxcvmbnairofjwpeurah"))
