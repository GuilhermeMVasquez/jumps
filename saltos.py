from sys import argv

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

# def noRecur(str):


str = argv[1]
print("Recursao simples:", recur(len(str)-1))
print("Recursao memorizada:", recurMem(len(str)-1))
# print("Sem recursao:", noRecur(str))