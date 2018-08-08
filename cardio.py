def longest_word(w1, w2, w3):
    if len(w1) >= len(w2) and len(w1) >= len(w3):
        return w1
    elif len(w2) >= len(w1) and len(w2) >= len(w3):
        return w2
    elif len(w3) >= len(w1) and len(w3) >= len(w2):
        return w3

longest = longest_word("rest","relax"," howmuchlonger")
print(longest)

def sum_to_n(n):
    total = 0
    for i in range(1,n+1):
        total = total +i
    return total
def sum_to_n(n):
    return (n*(n+1))/2

def is_triangle(a,b,c):
    sabc = a + b > c
    sacb = a + c > b
    sbca = b + c > a
    if sabc and sacb and sbca:
        return True
    else:
        return False


def rollDice(num):
    total = 0
    for i in range(num):
    total = total +
    random.randint(1,6)
return total
