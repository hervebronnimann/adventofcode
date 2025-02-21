from itertools import permutations

dat = """
279A
341A
459A
540A
085A
""".strip().split("\n")

dat2 = """
029A
980A
179A
456A
379A
""".strip().split("\n")

from functools import cache

dx = {"^": -1, "v": 1, "<": 0, ">": 0, "A": 0}
dy = {"^": 0, "v": 0, "<": -1, ">": 1, "A": 0}
loc = {
    "7": (0,0),
    "8": (0,1),
    "9": (0,2),
    "4": (1,0),
    "5": (1,1),
    "6": (1,2),
    "1": (2,0),
    "2": (2,1),
    "3": (2,2),
    "0": (3,1),
    "A": (3,2),
}
loc2 = {
    "^": (0,1),
    "A": (0,2),
    "<": (1,0),
    "v": (1,1),
    ">": (1,2),
}
@cache
# n downstream robots
# starting from position s
# moving to target position t
def f(s, t, n, is_first):
    if n < 0:
        return 1
    s0 = s
    t0 = t
    s=list(s)
    t=list(t)
    a = []
    while s[0]<t[0]:
        a.append("v")
        s[0]+=1
    while s[0]>t[0]:
        a.append("^")
        s[0]-=1
    while s[1]<t[1]:
        a.append(">")
        s[1]+=1
    while s[1]>t[1]:
        a.append("<")
        s[1]-=1
    a = "".join(a)
    perms = list(set(["".join(x) for x in permutations(a)]))
    ret = -1
    for l in perms:
        x, y = s0
        flag=False
        for c in l:
            x += dx[c]
            y += dy[c]
            if (is_first and (x,y)==(3,0)) or (not is_first and (x,y)==(0,0)):
                flag=True
                break
        if flag:
            continue
        l += "A"
        tot = 0
        lst = loc2["A"]
        for k in range(len(l)):
            tot += f(lst, loc2[l[k]], n-1, False)
            lst = loc2[l[k]]
        if ret<0 or ret>tot:
            ret=tot
    return ret


def solve():
    n = 25
    ans = 0
    for l in dat:
        tot = 0
        lst = loc["A"]
        for k in range(len(l)):
            tot += f(lst, loc[l[k]], n, True)
            lst = loc[l[k]]
        num = int(l[:-1])
        ans += tot*num
    print(ans)


solve()

