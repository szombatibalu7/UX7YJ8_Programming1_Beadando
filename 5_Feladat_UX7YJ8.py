import itertools
from collections import defaultdict

s = "123456789"
h = defaultdict(list)
for v in itertools.product(["+", "-", ""], repeat=9):
    if v[0] != "+":
        e = "".join("".join(u) for u in zip(v, s))
        h[eval(e)].append(e)

for e in h[100]:
    print(e, "= 100")