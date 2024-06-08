def issub(s:str, t: str) -> bool:
    stack = list(s)[::-1]
    for c in t:
        if stack and stack[-1] == c:
            stack.pop()
    return len(stack) == 0

s = "acb"
t = "ahcdsfb"

print(issub(s,t))