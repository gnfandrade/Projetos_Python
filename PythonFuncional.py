def hackF(n, k):
    def uns(s):
        return s.count("1")
    b = []
    for x in range(2**n):
        b.append(bin(x))
    print(b)
    b.sort(key=uns, reverse=True)
    print(b)
    return b[k-1]




def hackF2(n, k):
    return sorted([bin(x) for x in range(2**n)], key=lambda s: s.count("1"), reverse=True) [k-1]

print(hackF(3, 5))