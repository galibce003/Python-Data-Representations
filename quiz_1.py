count = 0
vo = ['a','e','i','o','u']

x = "aaassseefffgggiiijjjoOOkkkuuuu"

for i in x:
    if i in vo:
        count+=1

print(count)





def demystify(n):
    n = n.replace('1', 'b',)
    n =  n.replace('l', 'a',)
    return n

print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))
