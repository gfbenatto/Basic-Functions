def reverse(n):
    """
    This function receives a number and shows the reverse 127 -> 721.
    """
    s = str(n)
    c = 0
    for x in range(len(s)):
        c += int(s[x]) * (10**x)
    return c

print(reverse(34456786))