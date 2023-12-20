# multiply runs in O(1)
def multiply(x, y):
    # x and y are characters, we use a trick to get the index
    # of the character in the alphabet (a=0, b=1, c=2)
    i = ord(x) - 97
    j = ord(y) - 97
    mult_table = [
        ["c", "c", "a"],
        ["c", "b", "a"],
        ["a", "c", "b"]
    ]
    return mult_table[i][j]


# lookup runs in O(1) because the length of
# stringA and B are always <= 3
def lookup(string_a, string_b):
    string_res = ""
    for charA in string_a:
        for charB in string_b:
            char_res = multiply(charA, charB)
            if not string_res.__contains__(char_res):
                string_res += char_res
    return string_res


# getDelta runs in O(s)
def getDelta(s):
    res = []
    for i in range(1, s + 1):
        j = s + 1 - i
        res += [[i, j]]
    return res


# initTable runs in O(n) because we have n^2 cells
# and we fill only the diagonal
def initTable(x):
    n = len(x)
    t = [["" for _ in range(0, n)] for _ in range(0, n)]
    for i in range(0, n):
        t[i][i] = x[i]
    return t


# canParenthesis runs in O(n^3)
def fillTable(x):
    n = len(x)
    t = initTable(x)
    for s in range(1, n):
        delta = getDelta(s)
        for i in range(0, n - s):
            j = s + i
            for d in delta:
                z = t[i][j]
                z_prime = lookup(t[i][j - d[1]], t[i + d[0]][j])
                res = z
                for char in z_prime:  # This loop runs in O(3)
                    # because the length of z_prime is always <= 3
                    if not z.__contains__(char):
                        res += char
                t[i][j] = res
    return t


def canParenthesis(x, char="a"):
    if x == "":
        return False
    n = len(x)
    return fillTable(x)[0][n - 1].__contains__(char)


x = "abbbbc"
print(canParenthesis(x))
