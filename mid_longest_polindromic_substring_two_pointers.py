def longest_polindromic(s: str) -> str:

    ans = ''

    for i in range(len(s)):

        l, r = i, i

        while l>=0 and r < len(s) and l <= r:
            if s[l] != s[r]:
                break
            if r - l + 1 > len(ans):
                ans = s[l:r+1]

            l -= 1
            r += 1

        l, r = i, i + 1

        while l >= 0 and r < len(s) and l <= r:
            if s[l] != s[r]:
                break
            if r - l + 1 > len(ans):
                ans = s[l:r + 1]

            l -= 1
            r += 1

    return ans


print(longest_polindromic("acasdsfsbregwgsdfghgerghffgffff"))

