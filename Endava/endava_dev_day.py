def canFormPalindrome(st):
    count_dict = dict()
    for letter in st:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    odd = 0
    for count in count_dict.values():
        if count % 2 != 0 & 1:
            odd += 1
        if odd > 1:
            return False
    return True


s = canFormPalindrome("aaabbbb")
print(s)
