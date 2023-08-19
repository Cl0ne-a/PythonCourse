def check_polindrome(word) -> bool:
    return [w for w in word] == [w for w in word[::-1]]


print(check_polindrome("bammb"))