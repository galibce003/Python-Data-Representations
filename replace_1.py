def demystify(n):
    n = n.replace('1', 'b',)
    n =  n.replace('l', 'a',)
    return n

print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))
