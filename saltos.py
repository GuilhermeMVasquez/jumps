import sys

sys.setrecursionlimit(10**9)

def recur(n):
    if n < 0: return 0
    if n == 0: return 1
    if str[n] == '0': return 0
    return recur(n-1) + recur(n-2) + (1 if n-3 == 0 else 0) + ((recur(n-4) + recur(n-5)) if n-3 > 0 and str[n-3] == '1' else 0)

mem = {}
def recurMem(n):
    if n in mem: return mem[n]
    if n < 0: return 0
    if n == 0: return 1
    if str[n] == '0': return 0
    mem[n] = recur(n-1) + recur(n-2) + (1 if n-3 == 0 else 0) + ((recur(n-4) + recur(n-5)) if n-3 > 0 and str[n-3] == '1' else 0)
    return mem[n]

def noRecur(n):
    array = [0] * (n + 1)
    array[0] = 1
    for i in range(1, n + 1):
        if str[i] == '0':
            array[i] = 0
        else:
            array[i] = array[i-1] if i-1 >= 0 else 0
            array[i] += array[i-2] if i-2 >= 0 else 0
            array[i] += 1 if i-3 == 0 else 0
            if i-3 > 0 and str[i-3] == '1':
                array[i] += array[i-4] if i-4 >= 0 else 0
                array[i] += array[i-5] if i-5 >= 0 else 0
    return array[n]

str = sys.argv[1]
print("Recursao simples:    existem", recur(len(str)-1), "maneiras")
print("Recursao memorizada: existem", recurMem(len(str)-1), "maneiras")
print("Sem recursao:        existem", noRecur(len(str)-1), "maneiras")