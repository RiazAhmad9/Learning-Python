class Vault:
    def __init__(self, g=0, s=0, k=0):
        self.g = g
        self.s = s
        self.k = k

    def __str__(self):
        return f"{self.g} Galleons, {self.s} Sickles, {self.k} Knuts"

    def __add__(self, other):
        g = self.g + other.g
        s = self.s + other.s
        k = self.k + other.k
        return Vault(g, s, k)

p = Vault(100, 50, 25)
print(p)

w = Vault(25, 50, 100)
print(w)

total = p + w
print(total)